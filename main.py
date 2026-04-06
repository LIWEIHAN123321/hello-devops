from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TextInput(BaseModel):
    text: str

@app.get("/")
def root():
    return {"message": "Hello DevOps"}

@app.post("/predict")
def predict(data: TextInput):
    text = data.text.lower()
    if "good" in text or "love" in text or "great" in text:
        result = "positive"
    elif "bad" in text or "hate" in text or "terrible" in text:
        result = "negative"
    else:
        result = "neutral"
    return {"text": data.text, "sentiment": result}