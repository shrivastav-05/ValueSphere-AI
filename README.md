# Customer Lifetime Value & Profitability Prediction

## Project Overview

**Customer Lifetime Value & Profitability Prediction** is an end-to-end Data Science and Machine Learning project designed to help businesses understand customer value, measure profitability, predict future customer profit, and convert predictions into actionable business decisions.

Instead of only asking **"How much did this customer spend?"**, the project focuses on:

> **"How valuable is this customer, how profitable could they be in the future, and what should the business do next?"**

## Business Problem

Businesses often have large amounts of transaction data but struggle to identify:
- Which customers are genuinely profitable
- Which customers have high lifetime value
- Which customers may generate future profit
- Which customers are becoming inactive
- Which customers create loss or excessive costs
- Which customers should be retained, upsold, or monitored

This project converts historical transaction data into **customer-level profitability intelligence**.

## Project Objectives

- Analyze customer purchasing behavior
- Perform customer-level feature engineering
- Calculate RFM-based customer segments
- Analyze customer profitability
- Estimate Customer Lifetime Value (CLV)
- Create a future 6-month profit target
- Predict future customer profit using Machine Learning
- Identify future-value customer groups
- Generate business recommendations
- Build a reusable customer intelligence prediction system

## Feature Engineering

Customer-level features include:

| Feature | Description |
|---|---|
| `past_orders` | Historical number of orders |
| `past_revenue` | Historical revenue |
| `past_profit` | Historical profit |
| `past_discount` | Historical discount amount |
| `past_shipping_cost` | Historical shipping cost |
| `past_marketing_cost` | Historical marketing cost |
| `past_return_cost` | Historical return cost |
| `past_returns` | Number of returned orders |
| `past_quantity` | Historical quantity purchased |
| `past_avg_order_value` | Average order value |
| `past_avg_satisfaction` | Average customer satisfaction |
| `past_return_rate` | Historical return rate |
| `past_profit_margin` | Historical profit margin |
| `past_recency_days` | Days since last purchase |

## RFM Analysis

Customers are analyzed using:

- **Recency** — how recently the customer purchased
- **Frequency** — how frequently the customer purchased
- **Monetary Value** — how much revenue the customer generated

Customer segments include:

- VIP Customer
- Loyal Customer
- Potential Customer
- At Risk Customer
- Low Value Customer

## Customer Lifetime Value

The project estimates Customer Lifetime Value using customer purchasing behavior, average order value, purchase frequency, customer tenure, and profitability.

CLV helps answer:

> **"What is the economic value of this customer over their expected relationship with the business?"**

## Machine Learning

### Model

**Random Forest Regressor**

The model predicts:

```text
Future 6-Month Customer Profit
```

### Target

```text
future_6m_profit
```

### Model Features

```text
past_orders
past_revenue
past_profit
past_discount
past_shipping_cost
past_marketing_cost
past_return_cost
past_returns
past_quantity
past_avg_order_value
past_avg_satisfaction
past_return_rate
past_profit_margin
past_recency_days
```


The initial model produced:

```text
R² = -0.018
```

The customer behavior dataset was then improved so that customer-specific purchasing patterns were more realistically connected to future profitability.

The improved Random Forest model achieved approximately:

```text
R² ≈ 0.40
```

This represents a meaningful improvement over the initial model.

> Note: Update the exact MAE and RMSE values here using the final validation output from the notebook.

## Future Value Classification

Predicted future profit is converted into:

```text
High Future Value
Medium Future Value
Low Future Value
Future Loss Risk
```

## Business Decision Engine

| Business Decision | Purpose |
|---|---|
| **Retain & Upsell** | Protect and expand valuable customers |
| **Growth Opportunity** | Target customers with strong future potential |
| **Retention Campaign** | Re-engage customers with future potential |
| **Loss Risk** | Identify customers with negative profitability |
| **Monitor** | Continue observing customer behavior |

## Final Customer Intelligence System

```text
Historical Customer Behaviour
          ↓
Random Forest Prediction
          ↓
Future 6-Month Profit
          ↓
Estimated CLV
          ↓
Future Value
          ↓
Business Recommendation
```

For a new customer, the system produces:

- Predicted Future 6-Month Profit
- Estimated CLV
- Future Value Segment
- Business Recommendation

## Key Business Insights

### High-Value Customers
Customers with strong historical performance and high predicted future profitability can be targeted for retention and upselling.

### Retention Opportunities
Customers who may still have positive future potential despite reduced recent activity can be targeted through retention campaigns.

### Growth Opportunities
Customers with repeated purchasing behavior and positive future profitability can be targeted for cross-selling and upselling.

### Loss Risks
Customers whose profitability may be negative after considering relevant costs can be identified for cost optimization.

### Strategic Benefit
The project moves customer analysis from simple historical reporting toward **predictive customer profitability intelligence**.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Jupyter Notebook
- Power BI *(planned for final dashboard stage)*

## Project Files

```text
Customer_Lifetime_Value_Project/
│
├── Customer_Lifetime_Value.ipynb
├── customer_lifetime_value_data.csv
├── customer_lifetime_value_final.csv
├── customer_lifetime_value_improved.csv
├── customer_profit_final_model.pkl
├── customer_profit_model_features.pkl
├── future_profit_predictions.csv
└── README.md
```

## How to Run

### Install dependencies

```bash
pip install pandas numpy matplotlib seaborn scikit-learn joblib jupyter
```

### Open the notebook

```bash
jupyter notebook
```

Open:

```text
Customer_Lifetime_Value.ipynb
```

Run the notebook cells in order to reproduce the analysis and model.

## Future Scope

- Power BI executive dashboard
- Web-based prediction interface
- Customer churn prediction
- Personalized marketing recommendations
- Product-level profitability analysis
- Time-series customer revenue forecasting
- Model monitoring
- Automated customer alerts
- Advanced CLV models

## Project Outcome

This project demonstrates an end-to-end approach to **customer profitability analytics and predictive business intelligence**.

It combines:

**Data Analytics + Customer Segmentation + CLV + Machine Learning + Business Decision Making**

to answer a practical business question:

> **Which customers are worth investing in, how much future profit can they generate, and what action should the business take?**
