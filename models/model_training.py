from sklearn.linear_model import LinearRegression
import joblib

def train_model(X, y):
    model = LinearRegression()
    model.fit(X, y)
    joblib.dump(model, "models/linear_model.pkl")
    print("Model trained and saved.")
