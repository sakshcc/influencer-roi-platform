# 🚀 Influencer ROI Intelligence Platform
### AI-Powered Marketing Analytics | Databricks Project 

[![Databricks](https://img.shields.io/badge/Databricks-Serverless-FF3621?style=for-the-badge&logo=databricks)](https://databricks.com)
[![Delta Lake](https://img.shields.io/badge/Delta_Lake-3.0-00ADD8?style=for-the-badge)](https://delta.io)
[![MLflow](https://img.shields.io/badge/MLflow-Tracked-0194E2?style=for-the-badge)](https://mlflow.org)
[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python)](https://python.org)

---

## 📌 Problem Statement

The influencer marketing industry reached **$24 billion in 2024**, yet brands waste **$1.3 billion annually** on fraudulent partnerships. The core problems are:

- **49%** of influencers have fake engagement (2024 data)
- Only **25%** of brands can accurately measure influencer ROI
- **67%** of marketers struggle to find the RIGHT influencers
- Traditional attribution models can't track multi-touch influencer impact

**Why AI is essential — not optional:**
Rule-based systems fail because influencer performance is non-linear, engagement patterns shift weekly, and fraud detection requires analyzing thousands of behavioural signals simultaneously. This platform uses 4 ML models to solve what rules cannot.

---

## 🎯 Solution

An end-to-end AI platform built on Databricks that:

| Capability | Model | Metric |
|---|---|---|
| Predicts Influencer ROI | XGBoost Regressor | R² = 0.53 |
| Detects Fake Engagement | Random Forest + Isolation Forest | 8/100 flagged |
| Matches Influencers to Brands | Cosine Similarity | Avg score = 0.66 |
| Attributes Revenue | Shapley Position-Based | $30.7M attributed |

**Business Impact:**
- 🚨 8 fraudulent influencers detected → **$96,000 savings**
- 📊 32,442 conversions attributed across campaigns
- 💰 $30.7M total attributed revenue tracked
- ✅ 92 safe influencers cleared for investment

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────┐
│              DATA SOURCES                    │
│  Kaggle 2024 Influencer Data (22,038 rows)  │
│  Synthetic: Campaigns, Posts, Conversions   │
└─────────────────┬───────────────────────────┘
                  ↓
┌─────────────────────────────────────────────┐
│           BRONZE LAYER (Raw)                 │
│  bronze_influencers  │  bronze_campaigns     │
│  bronze_posts        │  bronze_engagement    │
│  bronze_conversions                          │
│  Features: ACID, schema enforcement,         │
│  partitioning, time travel                   │
└─────────────────┬───────────────────────────┘
                  ↓
┌─────────────────────────────────────────────┐
│          SILVER LAYER (Cleaned)              │
│  silver_influencers  │  silver_campaigns     │
│  silver_posts        │  silver_fraud_features│
│  Features: Parsed metrics, engagement rates, │
│  fraud signals, campaign KPIs                │
└─────────────────┬───────────────────────────┘
                  ↓
┌─────────────────────────────────────────────┐
│           GOLD LAYER (Analytics)             │
│  gold_influencer_performance                 │
│  gold_campaign_roi                           │
│  gold_ml_features (Feature Store)           │
│  gold_influencer_scores (Predictions)        │
│  gold_brand_influencer_matches               │
│  gold_attribution_results                    │
│  gold_fraud_alerts                           │
│  gold_attribution_by_influencer              │
│  Features: OPTIMIZE + ZORDER, query < 2s    │
└─────────────────┬───────────────────────────┘
                  ↓
┌─────────────────────────────────────────────┐
│          ML PIPELINE (MLflow Tracked)        │
│  Model 1: XGBoost ROI Prediction            │
│  Model 2: Random Forest Fraud Detection     │
│  Model 2b: Isolation Forest Anomaly         │
│  Model 3: Cosine Similarity Brand Match     │
│  Model 4: Logistic Regression Attribution   │
└─────────────────┬───────────────────────────┘
                  ↓
┌─────────────────────────────────────────────┐
│       BATCH INFERENCE + ORCHESTRATION        │
│  Daily scoring of all influencers            │
│  6-task Databricks Job DAG                  │
│  Predictions stored in Gold layer            │
└─────────────────────────────────────────────┘
```

> 📸 <img width="733" height="138" alt="Screenshot 2026-03-19 at 10 19 13 AM" src="https://github.com/user-attachments/assets/c6aa4e67-b383-4bfe-a892-6daa68b6f03d" />


---

## 📊 Dataset

| Dataset | Source | Rows | Description |
|---|---|---|---|
| Influencer Profiles | Kaggle 2024 | 22,038 | Real influencer data — followers, engagement, country |
| Campaigns | Synthetic | 200 | D2C brand campaign simulations |
| Influencer Posts | Synthetic | 1,749 | Post-level performance metrics |
| Engagement Details | Synthetic | 15,769 | Comment sentiment, bot signals, velocity |
| Conversions | Synthetic | 32,442 | Customer conversion touchpoints |

**Kaggle Source:** [Top 100 Social Media Influencers 2024](https://www.kaggle.com/datasets/bhavyadhingra00020/top-100-social-media-influencers-2024-countrywise)

---

## 🗂️ Repository Structure

```
influencer-roi-platform/
├── README.md
├── requirements.txt
├── scripts/
│   └── generate_synthetic_data.py    # Synthetic data generator
├── notebooks/
│   ├── 01_bronze_ingestion.ipynb     # Bronze Delta tables
│   ├── 02_silver_cleaning.ipynb      # Silver cleaning pipeline
│   ├── 03_silver_fraud_features.ipynb # Fraud feature engineering
│   ├── 04_gold_layer.ipynb           # Gold layer + OPTIMIZE
│   ├── 05_model_roi.ipynb            # XGBoost ROI prediction
│   ├── 06_model_fraud.ipynb          # Fraud detection models
│   ├── 07_model_matching.ipynb       # Brand-influencer matching
│   ├── 08_model_attribution.ipynb    # Multi-touch attribution
│   ├── 09_batch_inference.ipynb      # Batch scoring pipeline
│   └── 10_sql_dashboards.ipynb       # SQL analytics dashboards
└── docs/
    └── screenshots/                  # Dashboard screenshots
```

---

## ⚙️ Setup Instructions

### Prerequisites
- Databricks account (Free Edition with Serverless)
- Python 3.9+ installed locally
- Kaggle account (free)

### Step 1 — Clone the repository
```bash
git clone https://github.com/sakshcc/influencer-roi-platform.git
cd influencer-roi-platform
```

### Step 2 — Install local dependencies
```bash
pip install pandas numpy faker scikit-learn kaggle
```

### Step 3 — Download Kaggle dataset
```bash
# Or download manually from Kaggle and place in data/raw/
kaggle datasets download bhavyadhingra00020/top-100-social-media-influencers-2024-countrywise
unzip *.zip -d data/raw/
```

### Step 4 — Generate synthetic data
```bash
python scripts/generate_synthetic_data.py
```
Expected output:
```
Campaigns:   200 rows
Posts:       1,749 rows  (Fraud rate: 6.9%)
Engagement:  15,769 rows
Conversions: 32,442 rows
```

### Step 5 — Upload to Databricks
1. Log in to [Databricks](https://databricks.com)
2. Go to **Catalog → Create Schema** → name: `influencer_platform`
3. Create **Volume** → name: `raw_data`
4. Upload all 5 CSV files to the volume
5. Import all notebooks from `notebooks/` folder into your Workspace

### Step 6 — Run notebooks in order
Run each notebook top-to-bottom in this sequence:

```
01 → 02 → 03 → 04 → 05 → 06 → 07 → 08 → 09 → 10
```

### Step 7 — Configure Databricks Job
1. Go to **Jobs & Pipelines → Create Job**
2. Name: `influencer_roi_pipeline`
3. Add 6 tasks in order (see Pipeline section below)
4. Schedule: Daily at 2:00 AM
5. Click **Run now** to execute immediately

---

## 🔄 Pipeline Explanation

### Bronze Layer — Raw Ingestion
Reads CSV files from Databricks Volume into Delta tables with:
- Schema enforcement on all tables
- Audit columns (`_ingestion_timestamp`, `_source_file`)
- Partitioning by date/platform
- **Time travel demo**: UPDATE → read Version 0 → RESTORE

### Silver Layer — Cleaning & Feature Engineering
Transforms raw data into analytics-ready tables:
- Parses follower/engagement counts
- Calculates engagement rate, CTR, conversion rate, post ROI
- Engineers fraud detection features: bot probability aggregation, spam comment ratio, like velocity analysis, commenter account age
- Campaign-level KPI aggregations

### Gold Layer — Business Intelligence
Produces denormalized, ML-ready tables:
- Joins influencer profiles with fraud features
- Builds central ML Feature Store (46 features)
- Runs `OPTIMIZE + ZORDER` on all Gold tables
- Creates empty inference table for batch scoring

### ML Models
All 4 models tracked in MLflow with parameters, metrics, and artifacts:

**Model 1 — ROI Prediction (XGBoost)**
- Features: engagement rate, CTR, conversion rate, budget, post count
- 3 runs with hyperparameter comparison
- Best: MAE=3.80, R²=0.53

**Model 2 — Fraud Detection (Random Forest + Isolation Forest)**
- Features: organic behavioural signals only (likes/comments ratio, revenue per like, velocity patterns)
- Supervised: Random Forest with `class_weight=balanced`
- Unsupervised: Isolation Forest for anomaly detection
- Result: 8 fraud influencers correctly identified

**Model 3 — Brand Matching (Cosine Similarity)**
- Builds normalized influencer profile vectors
- Compares against brand preference vectors
- Produces Top-10 recommendations per brand
- Average match score: 0.66

**Model 4 — Multi-Touch Attribution (Logistic Regression + Shapley)**
- Position-based Shapley weights: First=40%, Last=40%, Middle=20%
- $30.7M revenue attributed across 32,442 conversions
- Top influencer: INF_0020 with $530,850 attributed revenue

### Batch Inference
- Loads production models from MLflow Unity Catalog Registry
- Scores all 100 influencers on ROI + fraud simultaneously
- Generates budget recommendations: Reduce/Maintain/Increase/Max Investment
- Stores predictions in `gold_influencer_scores` Delta table

---

## 🔬 Delta Lake Implementation

| Feature | Implementation |
|---|---|
| ACID Transactions | All writes use Delta format with `mode=overwrite` |
| Schema Enforcement | `inferSchema` + `overwriteSchema` controls |
| Time Travel | UPDATE → version history → RESTORE demonstrated in notebook 01 |
| OPTIMIZE | Run on all 3 main Gold tables |
| ZORDER | By `influencer_id` and `campaign_id` for fast lookups |
| Partitioning | Bronze tables partitioned by date/platform |

> 📸 <img width="558" height="201" alt="Screenshot 2026-03-19 at 10 24 31 AM" src="https://github.com/user-attachments/assets/183dc222-f0a9-4916-9617-71632518ae56" />

---

## 📈 MLflow Experiment Tracking

4 experiments tracked with full parameter + metric logging:

| Experiment | Runs | Key Metric |
|---|---|---|
| /influencer_roi_prediction | 3 | Best MAE=3.80, R²=0.53 |
| /influencer_fraud_detection_v2 | 2 | RF + Isolation Forest |
| /influencer_brand_matching | 1 | Avg match score=0.66 |
| /influencer_attribution | 1 | AUC=0.50 (synthetic data) |

All models registered in **Unity Catalog Model Registry** with full versioning.

> 📸 **[INSERT SCREENSHOT: MLflow experiment runs comparison view]**
> 📸 **[INSERT SCREENSHOT: MLflow Model Registry showing registered models]**

---

## 📊 Key Business Insights

**1. Fraud Detection**
- 8% fraud rate detected (industry average: 8-15%) ✅
- Fraud accounts have 0.29x predicted ROI vs 17.39x for legitimate accounts
- Key fraud signals: revenue_per_like, avg_conversions, likes_to_conversions_ratio

**2. ROI by Influencer Tier**
- Run `10_sql_dashboards` Cell 10 to see full breakdown
- Micro-influencers (10K-100K) typically show highest engagement quality

**3. Brand-Influencer Matching**
- StyleHub has highest match scores (fashion = high engagement alignment)
- TechNova harder to match (tech influencers are rarer in dataset)

**4. Campaign Performance**
- 200 campaigns across 8 D2C brands analyzed
- Campaign performance labels: Outperforming / On Target / Underperforming

**5. Attribution**
- 32,442 conversions tracked with Shapley weights
- First and last touch get 40% credit each (industry standard)

> 📸 **[INSERT SCREENSHOT: SQL Dashboard Cell 2 — Executive KPI table]**
> 📸 **[INSERT SCREENSHOT: SQL Dashboard Cell 5 — Fraud monitor table]**
> 📸 **[INSERT SCREENSHOT: SQL Dashboard Cell 9 — Budget optimization table]**

---

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Cloud Platform | Databricks (Serverless) |
| Data Format | Delta Lake 3.0 |
| Processing | Apache Spark / PySpark |
| ML Framework | Scikit-learn, XGBoost |
| Experiment Tracking | MLflow 3.x |
| Model Registry | Databricks Unity Catalog |
| Storage | Databricks Volumes |
| Orchestration | Databricks Jobs (6-task DAG) |
| Language | Python 3.12 |

---

## 📋 Requirements

```
pandas>=1.5.0
numpy>=1.23.0
scikit-learn>=1.2.0
xgboost>=1.7.0
faker>=18.0.0
matplotlib>=3.6.0
seaborn>=0.12.0
mlflow>=2.3.0
imbalanced-learn>=0.10.0
```

---

## 🎬 Demo Video

> 📸 **[INSERT LINK: Your 10-minute presentation video]**

Video covers:
1. Problem statement — $1.3B fraud crisis
2. Architecture walkthrough — Bronze → Silver → Gold
3. Live Delta Lake time travel demo
4. MLflow experiment comparison
5. Fraud detection results — 8 influencers flagged
6. Batch inference — 92 safe + 8 fraud recommendations
7. SQL Dashboard walkthrough
8. Business impact summary

---

## 👤 Author

**Sakshi Chaudhari**
- Domain: Marketing & Customer Analytics
- Platform: Databricks Serverless (Free Edition)
- Project: Capstone 2024-2025

---

## 📄 License

MIT License — free to use for educational purposes.
