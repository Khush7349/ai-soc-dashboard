import pandas as pd
import os
from detection import train_model
DATA_PATH = "data/logs.csv"
def main():
    print("🚀 Starting model training...")
    if not os.path.exists(DATA_PATH):
        print("❌ logs.csv not found in data/")
        return
    df = pd.read_csv(DATA_PATH)
    if df.empty:
        print("❌ Dataset is empty")
        return
    print(f"📊 Loaded {len(df)} records")
    train_model(df)
    print("✅ Model trained successfully")
    print("📁 Saved at: models/model.pkl")
if __name__ == "__main__":
    main()