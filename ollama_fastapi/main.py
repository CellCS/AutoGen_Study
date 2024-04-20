from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
import json
import requests

app = FastAPI(debug=True)

class Itemexample(BaseModel):
    name: str
    prompt: str
    instruction: str
    is_offer: Union[bool, None] = None

class Item(BaseModel):
    model: str
    prompt: str

urls =["http://localhost:11434/api/generate"]

headers = {
    "Content-Type": "application/json"
}


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/model/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/chat/{llms_name}")
def update_item(llms_name: str, item: Item):
    if llms_name == "llama3":
        url = urls[0]
        payload = {
            "model": "llama3",
            "prompt": "Why is the sky blue?",
            "stream": False
        }
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        if response.status_code == 200:
            return {"data": response.text, "llms_name": llms_name}
        else:
            print("error:", response.status_code, response.text)
            return {"item_name": item.model, "error": response.status_code, "data": response.text}
    return {"item_name": item.model, "llms_name": llms_name}


#uvicorn main:app --reload

# http://127.0.0.1:8000/items/5?q=somequery
# http://127.0.0.1:8000/chat/llama3

# curl --location 'http://127.0.0.1:8000/chat/llama3' \
# --header 'Content-Type: application/json' \
# --data '{
#   "model": "llama3",
#   "prompt": "Why is the sky blue?"
# }
# '