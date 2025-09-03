from fastapi import FastAPI, Header, HTTPException, Depends
from pydantic import BaseModel
import joblib
import pandas as pd
import os

# -----------------------------
# Load the saved pipeline (relative path)
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "insurance_pipeline.pkl")

if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model file not found at {model_path}")

model = joblib.load(model_path)

# -----------------------------
# Initialize FastAPI app
# -----------------------------
app = FastAPI(title="Insurance Charges Prediction API")

# -----------------------------
# API Key setup
# -----------------------------
API_KEY = "mysecretkey123"  # Change this to your secret key

def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

# -----------------------------
# Define input schema for API
# -----------------------------
class InsuranceData(BaseModel):
    age: int
    sex: str
    bmi: float
    children: int
    smoker: str
    region: str

# -----------------------------
# Routes
# -----------------------------
@app.get("/")
def home():
    return {"message": "Welcome to the Insurance Charges Prediction API"}

@app.post("/predict", dependencies=[Depends(verify_api_key)])
def predict(data: InsuranceData):
    # Convert input to DataFrame
    input_df = pd.DataFrame([data.dict()])

    # Predict using the trained pipeline
    try:
        prediction = model.predict(input_df)[0]
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    return {"predicted_charges": round(float(prediction), 2)}

# -----------------------------
# Run with uvicorn if executed directly
# -----------------------------
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("fastapi_app:app", host="127.0.0.1", port=8000, reload=True)
