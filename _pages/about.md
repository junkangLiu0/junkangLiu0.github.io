---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

Jun Kang Liu is a PhD candidate at Tianjin University, China, supervised by Prof. [Fanhua Shang](https://scholar.google.com.sg/citations?user=rk_HZTkAAAAJ&hl=en). During his doctoral studies, he focuses on research topics in federated learning, large-model fine-tuning, model fusion, and multimodal learning. His work aims to explore efficient, secure, and scalable learning paradigms for distributed intelligent systems, as well as to advance adaptive techniques for modern large-scale foundation models. 

# 🔥 News
- We release [**FedMuon**](https://arxiv.org/pdf/2510.27403), an highly efficient method for large vision language models with a two-stage design. It improves model efficiency by first conducting visual token merging in the encoding stage and then adopt KV Cache compression in the decoding stage. It could achieve about **2×** throughput across diffferent benchmarks and **3.21×** throughput boost when outputting longer sequences.

- We release [**DP-FedPGN**](https://arxiv.org/pdf/2510.27504), an efficient method for large vision language models by merging visual tokens. It could achieve about **2×** throughput and **1.7× - 2×** memory reduction with comparable performance through merging redundant visual tokens in some certain layers.

- We release [**ILoRA**](https://arxiv.org/pdf/2511.16069), an unified model with superior performance on both **continuous sign language recognition** and **sign language translation** tasks by using **only RGB inputs**.

- We release [**FedAdamW**](https://arxiv.org/pdf/2510.27486), which performs sign language recognition (SLR) with **pure skeleton inputs** but ahcieves comparable accuracy and much faster speed than recognition with RGB inputs.

# 📝 Publications 

## 📖 PrePrint
- [FedMuon: Accelerating Federated Learning with Matrix Orthogonalization](https://arxiv.org/pdf/2510.27403), **J Liu**, F Shang, J Zhou, H Liu, Y Liu, J Liu 2025.09. 

- [iLLaVA: An Image is Worth Fewer Than 1/3 Input Tokens in Large Multimodal Models](https://arxiv.org/pdf/2412.06263), **Lianyu Hu**, Fanhua Shang, Liang Wan, Wei Feng. 2024.12. [[code](https://github.com/hulianyuyy/iLLaVA)].

- [CorrNet+: Sign Language Recognition and Translation via Spatial-Temporal Correlation](https://arxiv.org/pdf/2404.11111.pdf), **Lianyu Hu**, Wei Feng, Liqing Gao, Zekang Liu, Liang Wan. 2024.04. [[code](https://github.com/hulianyuyy/CorrNet_Plus)].
  
- [Improving Continuous Sign Language Recognition with Adapted Image Models](https://arxiv.org/pdf/2404.08226.pdf), **Lianyu Hu**, Tongkai Shi, Liqing Gao, Zekang Liu, Wei Feng. 2024.04. [[code](https://github.com/hulianyuyy/AdaptSign)].

## 🖊️ Selected Publications ($\dagger$ denotes Corresponding Author)
- GReg: Geometry-Aware Region Refinement for Sign Language Video Generation. Tongkai Shi, **Lianyu Hu<sup>$\dagger$</sup>**, Fanhua Shang, Liqing Gao, Wei Feng. **<i>ICCV 2025</i>**.

- [Deep Correlated Prompting for Visual Recognition with Missing Modalities](https://arxiv.org/abs/2410.06558). **Lianyu Hu**, Tongkai Shi, Wei Feng, Fanhua Shang, Liang Wan. **<i>NeurIPS 2024</i>**. [[code](https://github.com/hulianyuyy/Deep_Correlated_Prompting)].
  
- [Pose-Guided Fine-Grained Sign Language Video Generation](https://arxiv.org/abs/2409.16709). Tongkai Shi, **Lianyu Hu**, Fanhua Shang, Jichao Feng, Peidong Liu, Wei Feng. **<i>ECCV 2024</i>**. [[code](https://github.com/shitongkai/PGMM)].
  
- [Spatial Temporal Aggregation for Efficient Continuous Sign Language Recognition](https://ieeexplore.ieee.org/document/10488467). **Lianyu Hu**, Liqing Gao, Zekang Liu, Wei Feng. **<i>IEEE Transactions on Emerging Topics in Computational Intelligence</i>**.

- [Dynamic Spatial-Temporal Aggregation for Skeleton-Aware Sign Language Recognition](https://arxiv.org/pdf/2403.12519.pdf). **Lianyu Hu**, Liqing Gao, Zekang Liu, Wei Feng. **<i>COLING 2024</i>**. [[code](https://github.com/hulianyuyy/DSTA-SLR)]. 

- [COMMA: Co-Articulated Multi-Modal Learning](https://arxiv.org/pdf/2401.00268.pdf). **Lianyu Hu**, Liqing Gao, Zekang Liu, Chi-Man Pun, Wei Feng. **<i>AAAI 2024</i>**. [[code](https://github.com/hulianyuyy/COMMA)].

- [Scalable Frame Resolution for Efficient Continuous Sign Language Recognition](https://www.sciencedirect.com/science/article/pii/S0031320323006015). **Lianyu Hu**, Liqing Gao, Zekang Liu, Wei Feng. **<i>Pattern Recognition</i>**.

- [AdaBrowse: Adaptive Video Browser for Efficient Continuous Sign Language Recognition](https://arxiv.org/pdf/2308.08327.pdf). **Lianyu Hu**, Liqing Gao, Zekang Liu, Chi-Man Pun, Wei Feng. **<i>ACMMM 2023 (Oral)</i>**. [[code](https://github.com/hulianyuyy/AdaBrowse)].

- [Skeleton-Based Action Recognition with Local Dynamic Spatial-Temporal Aggregation](https://www.sciencedirect.com/science/article/abs/pii/S0957417423011855). **Lianyu Hu**, Shenglan Liu, Wei Feng. **<i>Expert Systems with Applications</i>**. [[code](https://github.com/hulianyuyy/STGAT)]. (Previous name: Spatial Temporal Graph Attention Network for Skeleton-Based Action Recognition)

- [Continuous Sign Language Recognition with Correlation Network](https://arxiv.org/pdf/2303.03202.pdf). **Lianyu Hu**, Liqing Gao, Zekang Liu, Wei Feng. **<i>CVPR 2023</i>**. [[code](https://github.com/hulianyuyy/CorrNet)].

- [Self-Emphasizing Network for Continuous Sign Language Recognition](https://arxiv.org/pdf/2211.17081.pdf). **Lianyu Hu**, Liqing Gao, Zekang Liu, Wei Feng. **<i>AAAI 2023 (Oral)</i>**. [[code](https://github.com/hulianyuyy/SEN_CSLR)].

- [Temporal Lift Pooling for Continuous Sign Language Recognition](https://arxiv.org/abs/2207.08734).**Lianyu Hu**, Liqing Gao, Zekang Liu, Wei Feng. **<i>ECCV 2022</i>**. [[code](https://github.com/hulianyuyy/Temporal-Lift-Pooling)].

- [HFNet: A Novel Model for Human Focused Sports Action Recognition](https://dl.acm.org/doi/pdf/10.1145/3422844.3423052).**Lianyu Hu**, Liqing Gao, Zekang Liu, Wei Feng. **<i>ACMMM 2020 Workshop</i>**.

# 🎖 Honors and Awards
- 2025.06, Outstanding Graduate
- 2024.12, 优秀学生标兵（ten per year）
- 2024.10, National Scholarship
- 2023.10, National Scholarship

# 📖 Educations
- *2021-2025*, PhD in Computer Science and Technology, Tianjin Univerisity
- *2018-2021*, MEng in Computer Science and Technology, Dalian University of Technology
- *2014-2018*, BSc in Electronics and Information Engineering, Dalian University of Technology

<!--

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">CCOLING 2024</div><img src='images/500x300.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Dynamic Spatial-Temporal Aggregation for Skeleton-Aware Sign Language Recognition](https://arxiv.org/pdf/2403.12519.pdf)
[<img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" />](https://github.com/hulianyuyy/DSTA-SLR)

**Lianyu Hu**, Liqing Gao, Zekang Liu, Wei Feng
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">AAAI 2024</div><img src='images/500x300.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[COMMA: Co-Articulated Multi-Modal Learning](https://arxiv.org/pdf/2401.00268.pdf)
[<img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" />](https://github.com/hulianyuyy/COMMA)

**Lianyu Hu**, Liqing Gao, Zekang Liu, Chi-Man Pun, Wei Feng

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Pattern Recognition</div><img src='images/500x300.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Scalable Frame Resolution for Efficient Continuous Sign Language Recognition](https://www.sciencedirect.com/science/article/pii/S0031320323006015)

**Lianyu Hu**, Liqing Gao, Zekang Liu, Wei Feng
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ACMMM 2023 (Oral)</div><img src='images/500x300.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[AdaBrowse: Adaptive Video Browser for Efficient Continuous Sign Language Recognition](https://arxiv.org/pdf/2308.08327.pdf)
[<img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" />](https://github.com/hulianyuyy/AdaBrowse)

**Lianyu Hu**, Liqing Gao, Zekang Liu, Chi-Man Pun, Wei Feng

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Expert Systems with Applications</div><img src='images/500x300.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Skeleton-Based Action Recognition with Local Dynamic Spatial-Temporal Aggregation](https://www.sciencedirect.com/science/article/abs/pii/S0957417423011855)
[<img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" />](https://github.com/hulianyuyy/STGAT)

**Lianyu Hu**, Shenglan Liu, Wei Feng
- Previous name: Spatial Temporal Graph Attention Network for Skeleton-Based Action Recognition

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">CVPR 2023</div><img src='images/500x300.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Continuous Sign Language Recognition with Correlation Network](https://arxiv.org/pdf/2303.03202.pdf)
[<img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" />](https://github.com/hulianyuyy/CorrNet)

**Lianyu Hu**, Liqing Gao, Zekang Liu, Wei Feng

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">AAAI 2023 (Oral)</div><img src='images/500x300.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Self-Emphasizing Network for Continuous Sign Language Recognition](https://arxiv.org/pdf/2211.17081.pdf)
[<img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" />](https://github.com/hulianyuyy/SEN_CSLR)

**Lianyu Hu**, Liqing Gao, Zekang Liu, Wei Feng

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ECCV 2022</div><img src='images/500x300.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Temporal Lift Pooling for Continuous Sign Language Recognition](https://arxiv.org/abs/2207.08734)
[<img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" />](https://github.com/hulianyuyy/Temporal-Lift-Pooling)

**Lianyu Hu**, Liqing Gao, Zekang Liu, Wei Feng

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ACMMM 2020 Workshop</div><img src='images/500x300.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[HFNet: A Novel Model for Human Focused Sports Action Recognition](https://dl.acm.org/doi/pdf/10.1145/3422844.3423052)

**Lianyu Hu**, Liqing Gao, Zekang Liu, Wei Feng
</div>
</div>

-->
