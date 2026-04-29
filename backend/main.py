from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import os
from agents import analyze_logs
app = FastAPI(
    title="AI SOC Dashboard API",
    version="1.0"
)
DATA_PATH = "data/logs.csv"
@app.get("/")
def root():
    return {"status": "AI SOC API running"}
@app.get("/analyze")
def analyze():
    try:
        if not os.path.exists(DATA_PATH):
            raise HTTPException(status_code=404, detail="Log file not found")
        df = pd.read_csv(DATA_PATH)
        if df.empty:
            raise HTTPException(status_code=400, detail="Log file is empty")
        results = analyze_logs(df)
        return {
            "total_logs": len(df),
            "alerts": results
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
class LogInput(BaseModel):
    logs: list
@app.post("/analyze")
def analyze_custom(data: LogInput):
    try:
        df = pd.DataFrame(data.logs)
        if df.empty:
            raise HTTPException(status_code=400, detail="No logs provided")
        results = analyze_logs(df)
        return {
            "total_logs": len(df),
            "alerts": results
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))