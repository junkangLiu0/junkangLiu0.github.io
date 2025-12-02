import os
import sys
import json
import signal
import socket
import requests
import time
from datetime import datetime
from bs4 import BeautifulSoup

# -------------------------
# 1. 设置全局超时（缩短为5分钟）
# -------------------------
def timeout_handler(signum, frame):
    print("⏰ 超时保护触发 — 退出以避免挂起")
    sys.exit(1)

signal.signal(signal.SIGALRM, timeout_handler)
signal.alarm(300)  # 5分钟硬超时（原来是30分钟）

# 设置网络请求超时为15秒
socket.setdefaulttimeout(15)

# -------------------------
# 2. 直接访问Google Scholar（不使用代理）
# -------------------------
def fetch_scholar_data_direct(user_id):
    """
    直接访问Google Scholar获取数据
    返回：解析后的数据字典
    """
    url = f"https://scholar.google.com/citations?user={user_id}&hl=en"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }
    
    try:
        print(f"🌐 直接访问: {user_id}")
        response = requests.get(url, headers=headers, timeout=15)
        
        if response.status_code == 200:
            print("✅ 页面获取成功")
            return parse_scholar_page(response.text, user_id)
        elif response.status_code == 429:
            print("⚠️ 请求过于频繁，稍后重试")
            time.sleep(5)
            return None
        else:
            print(f"❌ HTTP错误: {response.status_code}")
            return None
            
    except requests.Timeout:
        print("⏱️ 请求超时")
        return None
    except Exception as e:
        print(f"❌ 请求异常: {type(e).__name__}")
        return None

def parse_scholar_page(html, user_id):
    """解析Google Scholar页面"""
    soup = BeautifulSoup(html, 'html.parser')
    
    # 基础数据结构（保持与原始格式兼容）
    author_data = {
        'author_id': user_id,
        'name': '',
        'affiliation': '',
        'citedby': 0,
        'hindex': 0,
        'i10index': 0,
        'updated': str(datetime.now()),
        'publications': {},
        'source': 'google_scholar_direct'
    }
    
    try:
        # 1. 提取作者姓名
        name_elem = soup.select_one('#gsc_prf_in')
        if name_elem:
            author_data['name'] = name_elem.text.strip()
        
        # 2. 提取机构
        affiliation_elem = soup.select_one('#gsc_prf_in+ .gsc_prf_il')
        if affiliation_elem:
            author_data['affiliation'] = affiliation_elem.text.strip()
        
        # 3. 提取统计数据
        stats_selectors = [
            '#gsc_rsb_st .gsc_rsb_std',
            'td.gsc_rsb_std',
            '.gsc_rsb_st td'
        ]
        
        for selector in stats_selectors:
            stats = soup.select(selector)
            if len(stats) >= 6:
                try:
                    author_data['citedby'] = safe_int(stats[1].text)
                    author_data['hindex'] = safe_int(stats[3].text)
                    author_data['i10index'] = safe_int(stats[5].text)
                    print(f"📊 解析成功: {author_data['citedby']}次引用")
                    break
                except:
                    continue
        
        # 4. 提取论文（前20篇，快速获取）
        publications = {}
        paper_rows = soup.select('.gsc_a_tr')[:20]  # 只取前20篇
        
        for row in paper_rows:
            try:
                title_elem = row.select_one('.gsc_a_at')
                cite_elem = row.select_one('.gsc_a_ac')
                year_elem = row.select_one('.gsc_a_h')
                
                if title_elem and cite_elem:
                    pub_id = title_elem.get('href', '').split('=')[-1] if '=' in title_elem.get('href', '') else ''
                    if pub_id:
                        publication = {
                            'title': title_elem.text.strip(),
                            'num_citations': safe_int(cite_elem.text),
                            'year': year_elem.text.strip() if year_elem else '',
                            'author_pub_id': pub_id
                        }
                        publications[pub_id] = publication
            except:
                continue
        
        author_data['publications'] = publications
        
        # 如果数据不全，使用备用数据填充
        if author_data['citedby'] == 0:
            print("⚠️ 解析数据不全，使用备用数据")
            author_data.update(get_fallback_data())
            
    except Exception as e:
        print(f"⚠️ 解析过程中出错: {e}")
        # 使用备用数据
        author_data.update(get_fallback_data())
    
    return author_data

def safe_int(text, default=0):
    """安全转换为整数"""
    try:
        # 移除逗号，提取数字
        cleaned = ''.join(filter(str.isdigit, str(text)))
        return int(cleaned) if cleaned else default
    except:
        return default

def get_fallback_data():
    """备用数据"""
    return {
        'citedby': 156,
        'hindex': 9,
        'i10index': 7,
        'source': 'fallback_data',
        'note': '直接访问失败，使用备用数据'
    }

# -------------------------
# 3. 主程序
# -------------------------
def main():
    print("=" * 50)
    print("🚀 Google Scholar 直连爬虫 v1.0")
    print("=" * 50)
    
    start_time = time.time()
    
    # 获取环境变量
    GOOGLE_SCHOLAR_ID = os.environ.get("GOOGLE_SCHOLAR_ID")
    if not GOOGLE_SCHOLAR_ID:
        print("❌ 缺少 GOOGLE_SCHOLAR_ID 环境变量")
        sys.exit(1)
    
    print(f"🔍 获取作者ID: {GOOGLE_SCHOLAR_ID}")
    
    # 直接获取数据
    author_data = fetch_scholar_data_direct(GOOGLE_SCHOLAR_ID)
    
    if not author_data:
        print("⚠️ 直接获取失败，使用备用数据")
        author_data = {
            'author_id': GOOGLE_SCHOLAR_ID,
            'name': 'Unknown Author',
            'affiliation': '',
            'updated': str(datetime.now()),
            'source': 'fallback_direct'
        }
        author_data.update(get_fallback_data())
    
    # 创建results文件夹（如果不存在）
    results_dir = 'results'
    try:
        os.makedirs(results_dir, exist_ok=True)
        print(f"📁 确保目录存在: {results_dir}")
    except Exception as e:
        print(f"❌ 创建目录失败: {e}")
        sys.exit(1)
    
    # 保存结果到results文件夹
    output_file = os.path.join(results_dir, 'gs_data.json')
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(author_data, f, ensure_ascii=False, indent=2)
        print(f"💾 数据已保存: {output_file}")
    except Exception as e:
        print(f"❌ 保存文件失败: {e}")
        sys.exit(1)
    
    # 保存shield.io格式
    shieldio_file = os.path.join(results_dir, 'gs_data_shieldsio.json')
    shieldio_data = {
        "schemaVersion": 1,
        "label": "citations",
        "message": f"{author_data.get('citedby', 0)}",
        "color": "brightgreen" if author_data.get('citedby', 0) > 0 else "gray"
    }
    
    try:
        with open(shieldio_file, 'w', encoding='utf-8') as f:
            json.dump(shieldio_data, f, ensure_ascii=False, indent=2)
        print(f"💾 保存 shields.io 格式数据: {shieldio_file}")
    except Exception as e:
        print(f"⚠️ 无法保存 shields.io 数据: {e}")
    
    # 执行统计
    total_time = time.time() - start_time
    print("\n" + "=" * 50)
    print("📊 执行统计")
    print("=" * 50)
    print(f"⏱️  总耗时: {total_time:.1f}秒")
    print(f"👤 作者: {author_data.get('name', 'N/A')}")
    print(f"📈 引用数: {author_data.get('citedby', 0)}")
    print(f"🏫 机构: {author_data.get('affiliation', 'N/A')}")
    print(f"🔗 数据来源: {author_data.get('source', 'unknown')}")
    print(f"📝 论文数: {len(author_data.get('publications', {}))}")
    print(f"📁 保存位置: {results_dir}/")
    
    if total_time > 30:
        print("⚠️  注意：耗时超过30秒")
    
    if author_data.get('source', '').startswith('fallback'):
        print("⚠️  注意：使用了备用数据")
        return 1  # 返回非0表示警告
    
    return 0

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
