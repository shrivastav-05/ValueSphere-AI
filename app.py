from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load saved model
model = joblib.load("customer_profit_final_model.pkl")

# Load feature list
features = joblib.load("customer_profit_model_features.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    data = {
        "past_orders": float(request.form["past_orders"]),
        "past_revenue": float(request.form["past_revenue"]),
        "past_profit": float(request.form["past_profit"]),
        "past_discount": float(request.form["past_discount"]),
        "past_shipping_cost": float(request.form["past_shipping_cost"]),
        "past_marketing_cost": float(request.form["past_marketing_cost"]),
        "past_return_cost": float(request.form["past_return_cost"]),
        "past_returns": float(request.form["past_returns"]),
        "past_quantity": float(request.form["past_quantity"]),
        "past_avg_order_value": float(request.form["past_avg_order_value"]),
        "past_avg_satisfaction": float(
            request.form["past_avg_satisfaction"]
        ),
        "past_return_rate": float(
            request.form["past_return_rate"]
        ),
        "past_profit_margin": float(
            request.form["past_profit_margin"]
        ),
        "past_recency_days": float(
            request.form["past_recency_days"]
        )
    }

    customer = pd.DataFrame([data])

    prediction = model.predict(
        customer[features]
    )[0]

    # Simple value classification
    if prediction > 10000:
        future_value = "High Future Value"
    elif prediction > 5000:
        future_value = "Medium Future Value"
    elif prediction > 0:
        future_value = "Low Future Value"
    else:
        future_value = "Future Loss Risk"

    # Business recommendation
    if (
        prediction > 10000
        and data["past_recency_days"] <= 60
    ):
        recommendation = "Retain & Upsell"

    elif (
        prediction > 0
        and data["past_recency_days"] > 120
    ):
        recommendation = "Retention Campaign"

    elif data["past_profit_margin"] < 0:
        recommendation = "Loss Risk"

    elif prediction > 0:
        recommendation = "Growth Opportunity"

    else:
        recommendation = "Monitor"

    return render_template(
        "index.html",
        prediction=prediction,
        future_value=future_value,
        recommendation=recommendation
    )


if __name__ == "__main__":
    app.run(debug=True)