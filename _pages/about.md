---
permalink: /
title: "刘俊康, Liu Junkang, Junkang Liu"
excerpt: "Federated Learning | Large Model Optimization | Privacy-Preserving Learning"
description: "刘俊康 , Junkang Liu  — PhD candidate at Tianjin University, focusing on federated learning, large-model optimization, model fusion, and privacy-preserving machine learning. All implementations are reproducible and resource-efficient, with most experiments runnable on a single RTX 4090 or RTX 2080 GPU."

keywords: [
  "Junkang Liu",
  "刘俊康",
  "Liu Junkang",
  "Federated Learning",
  "Large Model Optimization",
  "Optimizer",
  "Model Fusion",
  "Multimodal Learning",
  "Federated Optimization",
  "Machine Learning Research"
]
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
# **刘俊康 Junkang Liu | 天津大学 Tianjin University PHD**

**刘俊康, Junkang Liu** is a PhD candidate at **Tianjin University**, China, supervised by Prof. [Fanhua Shang](https://scholar.google.com.sg/citations?user=rk_HZTkAAAAJ&hl=en).  
His research interests include **federated learning**, **communication-efficient optimizers**, **large-model fine-tuning**, **model fusion**, and **multimodal learning**.  
He focuses on building **efficient, secure, and scalable distributed learning systems**, with an emphasis on optimization and generalization of modern large foundation models.

📧 Email: junkangliukk@gmail.com  
💬 WeChat: kk15653218567  
🔗 GitHub: <a href="https://github.com/junkangLiu0">https://github.com/junkangLiu0</a><br>
🎓 Google Scholar: <a href="https://scholar.google.com/citations?hl=zh-CN&user=N7pJWIoAAAAJ">https://scholar.google.com/citations?hl=zh-CN&user=N7pJWIoAAAAJ</a>
---

# 🔥 News
- **2026.2**: 🎉🎉 Our paper [**ILORA**](https://arxiv.org/abs/2511.16069) were accepted by **CVPR’26**！
- **2026.2**: 🎉🎉 Our paper [**DP-FedAdamW**](https://arxiv.org/abs/2602.19945) were accepted by **CVPR’26**！
- **2026.1**: 🎉🎉 Our paper [**LA-LORA**](https://arxiv.org/abs/2602.19926) were accepted by **ICLR’26**！
- **2025.10**: 🎉🎉 GitHub stars have passed 600！[**JunkangLiu**](https://github.com/junkangLiu0)
- **2025.10**: 🎉🎉 Our paper [**FedAdamW**](https://arxiv.org/pdf/2510.27486) were accepted by **AAAI’26**！
- **2025.7**: 🎉🎉 Our paper [**FedNSAM**](https://dl.acm.org/doi/abs/10.1145/3746027.3755226) were accepted by **ACM MM’25**！
- **2025.7**: 🎉🎉 Our paper [**FedBCG**](https://neurips.cc/virtual/2025/loc/san-diego/poster/115430) were accepted by **NeurIPS’25**！
- **2025.5**: 🎉🎉 Our paper [**FedSWA**](https://openreview.net/forum?id=HqmXiuFaOr) were accepted by **ICML’25**！
- **2024.7**: 🎉🎉 Our paper [**FedBCGD**](https://dl.acm.org/doi/abs/10.1145/3664647.3681094) were accepted by **ACM MM’24**！



# 📝 Publications 



## 🖊️ Selected Publications ($\dagger$ denotes Corresponding Author)

- **FedAdamW: A Communication-Efficient Optimizer for Federated Large Models**  
  **Junkang Liu**, Fanhua Shang, Hongying Liu, Yuanyuan Liu, Jin Liu, Kewen Zhu, Zhouchen Lin.  
  **AAAI 2026 (CCF-A)** [[paper](https://arxiv.org/abs/2510.27486)] [[code](https://github.com/junkangLiu0/FedAdamW)]
  
- **Improving Generalization in Federated Learning via Momentum-Based Stochastic Controlled Weight Averaging**  
   **Junkang Liu**, Yuanyuan Liu, Fanhua Shang, Hongying Liu, Jin Liu, Wei Feng.  
   **ICML 2025 (CCF-A)** [[paper](https://openreview.net/forum?id=HqmXiuFaOr)] [[code](https://github.com/junkangLiu0/FedSWA)]

- **FedBCGD: Communication-efficient Accelerated Block Coordinate Gradient Descent**  
  **Junkang Liu**, Fanhua Shang, Yuanyuan Liu, Hongying Liu, Yuangang Li, YunXiang Gong.  
   **ACM MM 2024 (CCF-A)** [[paper](https://dl.acm.org/doi/abs/10.1145/3664647.3681094)] [[code](https://github.com/junkangLiu0/FedBCGD)]

- **Local-Global Flatness Consistency in Federated Learning**  
 **Junkang Liu**, Fanhua Shang,  Yuxuan Tian, Hongying Liu,Yuanyuan Liu.   
 **ACM MM 2025 (CCF-A)**  [[paper](https://dl.acm.org/doi/abs/10.1145/3746027.3755226)] [[code](https://github.com/junkangLiu0/FedNSAM)]

- **ILoRA: Federated Learning with Low-Rank Adaptation for Heterogeneous Client Aggregation**   
  Junchao Zhou, **Junkang Liu**, Fanhua Shang.  
  **CVPR 2026 (CCF-A)**  [[paper](https://arxiv.org/abs/2511.16069)] [[code](#)]
  
- **DP-FedAdamW: An Efficient Optimizer for Differentially Private Federated Large Models**    
  Jin Liu, Ning Xi, Yinbin Miao, **Junkang Liu**$\dagger$.  
  **CVPR 2026 (CCF-A)**  [[paper](https://arxiv.org/abs/2602.19945)] [[code](https://github.com/junkangLiu0/FedAdamW)]

- **Rethinking LoRA for Privacy-Preserving Federated Learning in Large Models**     
  Jin Liu, Ning Xi, Yinbin Miao, **Junkang Liu**$\dagger$.  
  **ICLR 2026 (CCF-A)**  [[paper](https://arxiv.org/abs/2602.19926)] [[code](https://github.com/junkangLiu0/FedAdamW)]
  
- **High-Probability Bounds for Nonconvex Heavy-Tailed Learning**   
   Weixin An, Yuanyuan Liu, Fanhua Shang, Han Yu, **Junkang Liu**, Hongying Liu.      
 **NeurIPS 2025 (CCF-A)**  [[paper](https://neurips.cc/virtual/2025/loc/san-diego/poster/115430)]




## 📖 PrePrint
  
- **FedMuon: Accelerating Federated Learning with Matrix Orthogonalization**    
**Junkang Liu**, Fanhua Shang, Junchao Zhou, Hongying Liu, Yuanyuan Liu, Jin Liu.    
[[paper](https://arxiv.org/abs/2510.27403)] [[code](https://github.com/junkangLiu0/FedMuon)]

* **Taming Preconditioner Drift: Unlocking the Potential of Second-Order Optimizers for Federated Learning on Non-IID Data**  
  **Junkang Liu**, Fanhua Shang, Hongying Liu, Jin Liu, Weixin An, Yuanyuan Liu.  
  [[paper](https://arxiv.org/abs/2602.19271)] [[code](https://anonymous.4open.science/r/FedPAC-8B24)]

- **DP-FedPGN: Finding Global Flat Minima for Differentially Private Federated Learning via Penalizing Gradient Norm**        
  **Junkang Liu**, Yuxuan Tian, Fanhua Shang, Yuanyuan Liu, Hongying Liu, Junchao Zhou, Daorui Ding.  
  [[paper](https://arxiv.org/pdf/2510.27504)] [[code](https://github.com/junkangLiu0/DP-FedPGN)].

  
-  **Dynamic Differentially Private Online ADMM Algorithms with Running Average Gradients for Machine Learning**       
  Fanhua Shang, **Junkang Liu**, Weixin An, Hongying Liu. 
  
-  **IGFL:Combining Individual and Group Behaviors in Federated Learning Approaching Global Consistency**   
  Fanhua Shang, **Junkang Liu**, Weixin An, Hongying Liu. 
  
- **LSSCA: Differentially Private Federated Learning with Laplacian Smoothing and Stochastic Controlled Averaging**  
  Fanhua Shang, **Junkang Liu**, Weixin An, Hongying Liu. 
  
- **Towards Global Flat Minima in Sample-Level Private Federated Learning**  
  Jin Liu, Ning Xi, Yinbin Miao, **Junkang Liu**. 
  

- **LAVA: A UNIFIED FRAMEWORK FOR FINETUNING LANGUAGE AND VISION MODELSs**    
  Daorui Ding, Fanhua Shang, Tiancan Feng, **Junkang Liu**, Hongying Liu . 



# 🎖 Honors and Awards
- 2024.10, **National Scholarship**
- 2020.10, **National Scholarship**
- 2020.10, **Qingdao University Top Ten Outstanding Students Award**

# 📖 Educations
- *2025-*, PhD in Computer Science and Technology, Tianjin University
- *2022-2025*, Master in Computer Science and Technology, Xidian University 
- *2018-2022*, BSc in Mathematics, Qingdao University 

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
