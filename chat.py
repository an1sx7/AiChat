from google import genai
from dotenv import load_dotenv
import os
from fastapi import FastAPI 
from pydantic import BaseModel
app=FastAPI()

load_dotenv()

client = genai.Client(api_key=os.getenv("API_KEY"))

class Text(BaseModel):
    text:str


@app.post('/send')
def chat(text:Text):
    #res=model.generate_content(item.text)
    res = client.models.generate_content(
    model="gemini-2.5-flash", contents=text.text
)
    return { "response":res.text }