import joblib
from pathlib import Path

MODEL_PATH = Path("models/saved/prompt_injection_model.pkl")

model = None


def load_model():
    global model
    if model is None:
        model = joblib.load(MODEL_PATH)
    return model


def predict_prompt(text: str) -> int:
    loaded_model = load_model()
    prediction = loaded_model.predict([text])[0]
    return int(prediction)