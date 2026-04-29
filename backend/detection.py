from sklearn.ensemble import IsolationForest
import pickle
import os
from preprocessing import preprocess
MODEL_PATH = "models/model.pkl"
def train_model(df):
    X = preprocess(df)
    model = IsolationForest(
        contamination=0.2,
        random_state=42
    )
    model.fit(X)
    os.makedirs("models", exist_ok=True)
    with open(MODEL_PATH, "wb") as f:
        pickle.dump(model, f)
_model_cache = None
def load_model():
    global _model_cache
    if _model_cache is not None:
        return _model_cache
    if not os.path.exists(MODEL_PATH):
        raise Exception("Model not found. Train it first.")
    with open(MODEL_PATH, "rb") as f:
        _model_cache = pickle.load(f)
    return _model_cache
def predict(df):
    model = load_model()
    X = preprocess(df)
    preds = model.predict(X)  
    scores = model.decision_function(X)  
    return preds, scores