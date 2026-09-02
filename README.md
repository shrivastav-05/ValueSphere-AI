# Customer Lifetime Value & Profitability Prediction

An end-to-end **Data Science and Machine Learning system** that analyzes customer purchasing behavior, measures historical profitability, estimates Customer Lifetime Value (CLV), predicts future customer profit, and converts predictions into actionable business decisions.

> **Business Question:** Which customers are worth investing in, how much future profit can they generate, and what should the business do next?

---

## Project Overview

Businesses often know how much revenue a customer generated historically, but revenue alone does not indicate whether a customer is actually valuable.

A customer may generate high revenue while also producing high discounts, shipping costs, marketing costs, or return costs.

This project therefore focuses on **customer-level profitability and future value**, combining:

**Customer Analytics + RFM Segmentation + Profitability Analysis + CLV + Machine Learning + Business Recommendations**

---

## Business Problem

The system helps answer:

* Which customers are genuinely profitable?
* Which customers have high lifetime value?
* Which customers are likely to generate future profit?
* Which customers are becoming inactive?
* Which customers may create future losses?
* Which customers should be retained or upsold?
* Which customers require monitoring?

---

## Project Objectives

* Analyze historical customer purchasing behavior
* Build customer-level features from transaction data
* Perform RFM customer segmentation
* Measure customer profitability
* Estimate Customer Lifetime Value
* Create a future 6-month profit target
* Predict future customer profitability using Machine Learning
* Segment customers based on predicted future value
* Generate business recommendations
* Build a reusable customer intelligence pipeline

---

# Machine learning Workflow

```text
Transaction-Level Data
        ↓
Data Cleaning & Validation
        ↓
Customer-Level Aggregation
        ↓
Feature Engineering
        ↓
RFM Analysis
        ↓
Profitability Analysis
        ↓
CLV Estimation
        ↓
Future 6-Month Profit Target
        ↓
Train/Test Split
        ↓
Random Forest Regression
        ↓
Model Evaluation
        ↓
Future Value Segmentation
        ↓
Business Decision Engine
```

---

# Customer Feature Engineering

Transaction-level information is aggregated into customer-level behavioral and profitability features.

| Feature                 | Description                               |
| ----------------------- | ----------------------------------------- |
| `past_orders`           | Historical number of orders               |
| `past_revenue`          | Historical revenue                        |
| `past_profit`           | Historical profit                         |
| `past_discount`         | Historical discount amount                |
| `past_shipping_cost`    | Historical shipping cost                  |
| `past_marketing_cost`   | Historical marketing cost                 |
| `past_return_cost`      | Historical return cost                    |
| `past_returns`          | Number of returned orders                 |
| `past_quantity`         | Historical quantity purchased             |
| `past_avg_order_value`  | Average order value                       |
| `past_avg_satisfaction` | Average customer satisfaction             |
| `past_return_rate`      | Historical return rate                    |
| `past_profit_margin`    | Historical profit margin                  |
| `past_recency_days`     | Days since the customer's latest purchase |

These features allow the model to capture both **customer behavior and economic value**.

---

# RFM Customer Segmentation

Customers are analyzed using the classic **RFM framework**.

### Recency

How recently did the customer purchase?

### Frequency

How frequently does the customer purchase?

### Monetary Value

How much revenue did the customer generate?

Customers are grouped into business-oriented segments such as:

* **VIP Customer**
* **Loyal Customer**
* **Potential Customer**
* **At Risk Customer**
* **Low Value Customer**

RFM segmentation provides an interpretable view of customer behavior before applying predictive modeling.

---

# Customer Profitability

Unlike revenue-only analysis, customer profitability considers relevant business costs.

```text
Customer Profit
=
Revenue
− Discounts
− Shipping Cost
− Marketing Cost
− Return Cost
```

This helps distinguish between:

**High Revenue Customers**
and
**High Profit Customers**

which are not always the same.

---

# Customer Lifetime Value

The project estimates Customer Lifetime Value using customer purchasing behavior, including factors such as:

* Average Order Value
* Purchase Frequency
* Customer Tenure
* Historical Profitability

CLV provides an estimate of the customer's economic value over the expected customer relationship.

---

# Machine Learning

## Model

**Random Forest Regressor**

The model predicts:

```text
Future 6-Month Customer Profit
```

### Target Variable

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

---

# Model Performance

### Baseline Model

Initial Random Forest performance:

```text
R² = -0.018
```

The initial result indicated that the model was not sufficiently capturing the relationship between historical customer behavior and future profitability.

### Improved Model

After improving the customer behavioral data and feature relationships:

```text
R² ≈ 0.40
```

# Future Customer Value Classification

Predicted future profit is converted into business-oriented value segments:

```text
High Future Value
Medium Future Value
Low Future Value
Future Loss Risk
```

This converts a continuous ML prediction into an easier-to-use business decision.

---

# Business Decision Engine

| Customer Condition                        | Recommended Action     |
| ----------------------------------------- | ---------------------- |
| High future value                         | **Retain & Upsell**    |
| Strong potential                          | **Growth Opportunity** |
| Positive potential but declining activity | **Retention Campaign** |
| Predicted negative profitability          | **Loss Risk**          |
| Uncertain / moderate value                | **Monitor**            |

The goal is not simply to predict profit, but to turn the prediction into an **actionable customer strategy**.

---

# Final Customer Intelligence System

```text
Historical Customer Behaviour
             ↓
      Feature Engineering
             ↓
        ML Prediction
             ↓
   Future 6-Month Profit
             ↓
       CLV Estimation
             ↓
    Future Value Segment
             ↓
   Business Recommendation
```

For a customer, the system can produce:

```text
Predicted Future Profit
Estimated CLV
Customer Value Segment
Business Recommendation
```

---

# Key Business Insights

### High-Value Customers

Customers with strong historical profitability and high predicted future value can be prioritized for retention and upselling.

### Retention Opportunities

Customers with positive future potential but declining recent activity can be targeted with re-engagement strategies.

### Growth Opportunities

Customers showing repeated purchasing behavior and positive profitability can be targeted for cross-selling and upselling.

### Loss Risk

Customers with potentially negative future profitability can be identified for cost optimization or targeted intervention.

### Strategic Benefit

The project moves customer analysis from:

```text
Historical Reporting
        ↓
Predictive Customer Intelligence
        ↓
Actionable Business Decisions
```

---

# Technologies Used

* **Python**
* **Pandas**
* **NumPy**
* **Scikit-learn**
* **Matplotlib**
* **Seaborn**
* **Joblib**
* **Jupyter Notebook**
* **Power BI** *(planned dashboard stage)*

# How to Run

## 1. Install Dependencies

```bash
pip install pandas numpy matplotlib seaborn scikit-learn joblib jupyter
```

## 2. Start Jupyter Notebook

```bash
jupyter notebook
```

## 3. Open

```text
Customer_Lifetime_Value.ipynb
```

Run the notebook cells sequentially to reproduce the analysis and machine learning workflow.

---

# Future Scope

* Power BI executive dashboard
* Flask/FastAPI prediction API
* Customer churn prediction
* Personalized marketing recommendations
* Product-level profitability analysis
* Time-series customer revenue forecasting
* Model monitoring
* Automated customer alerts
* Advanced probabilistic CLV models

---

# Project Outcome

This project demonstrates an end-to-end **customer profitability and predictive analytics workflow**.

It combines:

**Data Engineering + Feature Engineering + RFM Analysis + Profitability Analytics + CLV + Machine Learning + Business Decision Making**

to answer a practical business question:

> **Which customers are worth investing in, how much future profit can they generate, and what action should the business take?**

# Author

**Shivam Shrivastav**

BCA Student | Data Analytics & Machine Learning

If you find this project useful, consider giving the repository a ⭐.
