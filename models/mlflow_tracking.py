import mlflow

mlflow.set_tracking_uri("http://127.0.0.1:5000")
mlflow.set_experiment("Apparel Forecasting")

with mlflow.start_run():
    mlflow.log_param("model", "Linear Regression")
    mlflow.log_metric("rmse", 0.05)
    mlflow.sklearn.log_model(model, "model")
