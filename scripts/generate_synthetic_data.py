import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import os

random.seed(42)
np.random.seed(42)
os.makedirs('data/synthetic', exist_ok=True)

# =============================================
# TABLE 1: CAMPAIGNS (200 rows)
# =============================================
brands = ['GlowSkin', 'FitFuel', 'TechNova', 'StyleHub',
          'WanderLux', 'HomeNest', 'PureGlow', 'ActiveEdge']
categories = ['beauty', 'fitness', 'tech', 'fashion',
              'travel', 'lifestyle', 'food', 'gaming']
objectives = ['awareness', 'conversion', 'engagement']
audiences = ['gen_z', 'millennial', 'gen_x', 'mixed']

campaigns = []
for i in range(200):
    start = datetime(2023, random.randint(1,12),
                     random.randint(1,28))
    budget = random.randint(5000, 100000)
    campaigns.append({
        'campaign_id': f'CAMP_{i+1:04d}',
        'brand_name': random.choice(brands),
        'product_category': random.choice(categories),
        'start_date': start.strftime('%Y-%m-%d'),
        'end_date': (start + timedelta(
            days=random.randint(14,60))).strftime('%Y-%m-%d'),
        'budget': budget,
        'influencer_spend': round(budget * random.uniform(0.4, 0.8)),
        'target_audience': random.choice(audiences),
        'campaign_objective': random.choice(objectives),
        'expected_roas': round(random.uniform(2.0, 8.0), 2),
        'num_influencers': random.randint(3, 15),
        'campaign_status': random.choice(
            ['completed','active','paused'])
    })

df_campaigns = pd.DataFrame(campaigns)
df_campaigns.to_csv('data/synthetic/campaigns.csv', index=False)
print(f'Campaigns: {len(df_campaigns)} rows')

# =============================================
# TABLE 2: INFLUENCER POSTS
# FIXED: Only 8% fraud rate (was 76% before)
# =============================================
post_types = ['reel', 'post', 'story', 'video', 'carousel']

# Pre-assign fraud status to influencers FIRST
# Only 8 out of 100 influencers are fraudulent
influencer_ids = [f'INF_{i:04d}' for i in range(1, 101)]
fraud_influencers = set(random.sample(influencer_ids, 8))  # exactly 8%
print(f'Fraud influencers: {len(fraud_influencers)} out of 100')

posts = []
for camp in campaigns:
    num_inf = camp['num_influencers']
    start_dt = datetime.strptime(camp['start_date'], '%Y-%m-%d')
    spend_per_inf = camp['influencer_spend'] / num_inf

    selected_influencers = random.choices(influencer_ids, k=num_inf)

    for inf_id in selected_influencers:
        is_fraud = inf_id in fraud_influencers

        if is_fraud:
            # Fraud accounts: high followers, fake engagement
            followers = random.randint(500000, 2000000)
            impressions = random.randint(5000, 20000)  # low real reach
            likes = random.randint(50000, 200000)      # fake high likes
            comments = random.randint(10, 100)         # very low comments
            shares = random.randint(5, 50)
            conversions = random.randint(0, 5)         # almost no sales
            revenue = round(conversions * random.uniform(10, 30), 2)
        else:
            # Legitimate accounts: realistic metrics
            followers = random.randint(10000, 1000000)
            impressions = int(followers * random.uniform(0.05, 0.35))
            likes = int(impressions * random.uniform(0.02, 0.12))
            comments = int(likes * random.uniform(0.03, 0.15))
            shares = int(likes * random.uniform(0.01, 0.06))
            conversions = random.randint(10, 500)
            revenue = round(conversions * random.uniform(30, 200), 2)

        posts.append({
            'post_id': f'POST_{len(posts)+1:06d}',
            'campaign_id': camp['campaign_id'],
            'influencer_id': inf_id,
            'post_date': (start_dt + timedelta(
                days=random.randint(0, 30))).strftime('%Y-%m-%d'),
            'post_type': random.choice(post_types),
            'impressions': impressions,
            'reach': int(impressions * random.uniform(0.7, 0.95)),
            'likes': likes,
            'comments': comments,
            'shares': shares,
            'saves': int(likes * random.uniform(0.01, 0.08)),
            'click_throughs': int(
                impressions * random.uniform(0.005, 0.05)),
            'conversions': conversions,
            'revenue_attributed': revenue,
            'is_fraud_account': int(is_fraud),
            'sponsored_tag': random.choice([0, 1]),
            'budget_allocated': round(spend_per_inf, 2)
        })

df_posts = pd.DataFrame(posts)
df_posts.to_csv('data/synthetic/influencer_posts.csv', index=False)
fraud_rate = df_posts['is_fraud_account'].mean()
print(f'Posts: {len(df_posts)} rows')
print(f'Fraud rate: {fraud_rate:.1%} (target: ~8%)')

# =============================================
# TABLE 3: ENGAGEMENT DETAILS
# FIXED: Proper bot signals for fraud accounts
# =============================================
sentiments = ['positive', 'neutral', 'negative', 'spam']
engagement_rows = []

for _, post in df_posts.iterrows():
    is_fraud = bool(post['is_fraud_account'])
    n_detail_rows = random.randint(3, 15)

    for j in range(n_detail_rows):
        if is_fraud:
            sentiment = random.choices(
                sentiments, weights=[0.05, 0.05, 0.05, 0.85])[0]
            commenter_followers = random.randint(0, 50)
            commenter_age = random.randint(1, 30)
            like_velocity = random.randint(10000, 80000)
            spike = 1
            bot_prob = round(random.uniform(0.75, 0.99), 3)
        else:
            sentiment = random.choices(
                sentiments, weights=[0.5, 0.3, 0.15, 0.05])[0]
            commenter_followers = random.randint(100, 5000)
            commenter_age = random.randint(180, 2000)
            like_velocity = random.randint(10, 500)
            spike = 0
            bot_prob = round(random.uniform(0.0, 0.15), 3)

        engagement_rows.append({
            'engagement_id': f'ENG_{len(engagement_rows)+1:08d}',
            'post_id': post['post_id'],
            'comment_sentiment': sentiment,
            'commenter_follower_count': commenter_followers,
            'commenter_account_age_days': commenter_age,
            'like_velocity_per_hour': like_velocity,
            'engagement_spike_detected': spike,
            'bot_probability': bot_prob
        })

df_eng = pd.DataFrame(engagement_rows)
df_eng.to_csv('data/synthetic/engagement_details.csv', index=False)
print(f'Engagement: {len(df_eng)} rows')

# =============================================
# TABLE 4: CONVERSIONS
# FIXED: Only from legitimate influencers
# =============================================
conversions_rows = []
legit_posts = df_posts[
    (df_posts['conversions'] > 0) &
    (df_posts['is_fraud_account'] == 0)]

for _, post in legit_posts.iterrows():
    n_convs = min(int(post['conversions']), 20)
    for k in range(n_convs):
        touchpoints = random.randint(1, 4)
        order_val = round(random.uniform(20, 500), 2)
        conversions_rows.append({
            'conversion_id': f'CONV_{len(conversions_rows)+1:07d}',
            'post_id': post['post_id'],
            'campaign_id': post['campaign_id'],
            'influencer_id': post['influencer_id'],
            'order_value': order_val,
            'customer_ltv': round(order_val * random.uniform(2, 8), 2),
            'touchpoint_number': touchpoints,
            'discount_code_used': random.choice([0, 0, 0, 1]),
            'attribution_weight': round(1.0 / touchpoints, 4),
            'conversion_date': post['post_date']
        })

df_conv = pd.DataFrame(conversions_rows)
df_conv.to_csv('data/synthetic/conversions.csv', index=False)
print(f'Conversions: {len(df_conv)} rows')
print(f'\nAll synthetic data regenerated with correct fraud rate!')
print(f'Summary:')
print(f'  Campaigns:   {len(df_campaigns)}')
print(f'  Posts:       {len(df_posts)}')
print(f'  Engagement:  {len(df_eng)}')
print(f'  Conversions: {len(df_conv)}')
print(f'  Fraud rate:  {fraud_rate:.1%}')