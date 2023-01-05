from fastapi import FastAPI
import joblib

app = FastAPI()
model = joblib.load("model.pkl")

@app.post("/predict")
def predict(data: list):
    return {"prediction": model.predict(data).tolist()}

@app.get("/health")
def health():
    return {"status": "ok"}
