import os
import sys
import json
import signal
import socket
from datetime import datetime
from scholarly import scholarly, ProxyGenerator
from fp.fp import FreeProxy 
# -------------------------
# 1. Setup global timeouts
# -------------------------
# Exit the script entirely after 30 minutes (1800s)
def timeout_handler(signum, frame):
    print("⏰ Timeout reached — exiting to avoid hang.")
    sys.exit(1)

signal.signal(signal.SIGALRM, timeout_handler)
signal.alarm(1800)  # 30-minute hard timeout

# Limit each network request to 30s
socket.setdefaulttimeout(30)

# -------------------------
# 2. Optional proxy setup (avoids Google blocking)
# -------------------------
try:
    # Manually get a working free proxy
    proxy_list = FreeProxy(country_id=['US', 'BR'], timeout=1, rand=True).get_proxy_list(repeat=1)

    pg = ProxyGenerator()
    pg.SingleProxy(http=proxy, https=proxy)
    scholarly.use_proxy(pg)
    
    print(f"✅ Proxy setup successful: {proxy}")
except Exception as e:
    print(f"⚠️ Proxy setup failed or skipped: {e}")

# -------------------------
# 3. Fetch author info
# -------------------------
GOOGLE_SCHOLAR_ID = os.environ.get("GOOGLE_SCHOLAR_ID")
if not GOOGLE_SCHOLAR_ID:
    print("❌ Missing GOOGLE_SCHOLAR_ID environment variable.")
    sys.exit(1)

print(f"🔍 Fetching author ID: {GOOGLE_SCHOLAR_ID}")

try:
    author = scholarly.search_author_id(GOOGLE_SCHOLAR_ID)
except Exception as e:
    print(f"❌ Error fetching author ID: {e}")
    sys.exit(1)

# Only fetch basic info + citation indices first
try:
    scholarly.fill(author, sections=['basics', 'indices', 'counts'])
    print(f"✅ Fetched base info for {author.get('name', 'Unknown Author')}")
except Exception as e:
    print(f"❌ Error during author fill: {e}")
    sys.exit(1)

# Optional: limit how many publications you expand
pubs = author.get('publications', [])
if pubs:
    max_pubs = min(200, len(pubs))  # limit to 200 for speed
    print(f"📚 Expanding {max_pubs} publications (of {len(pubs)} total)...")
    filled_pubs = {}
    for pub in pubs[:max_pubs]:
        try:
            scholarly.fill(pub)
            filled_pubs[pub['author_pub_id']] = pub
        except Exception as e:
            print(f"⚠️ Skipping a publication due to error: {e}")
else:
    filled_pubs = {}

author['publications'] = filled_pubs
author['updated'] = str(datetime.now())

# -------------------------
# 4. Save results
# -------------------------
os.makedirs('results', exist_ok=True)

with open('results/gs_data.json', 'w', encoding='utf-8') as f:
    json.dump(author, f, ensure_ascii=False, indent=2)
print("💾 Saved results/gs_data.json")

shieldio_data = {
    "schemaVersion": 1,
    "label": "citations",
    "message": f"{author.get('citedby', 0)}",
}
with open('results/gs_data_shieldsio.json', 'w', encoding='utf-8') as f:
    json.dump(shieldio_data, f, ensure_ascii=False, indent=2)
print("💾 Saved results/gs_data_shieldsio.json")

print("✅ Done — citation data updated successfully.")
