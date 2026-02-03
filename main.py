from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
import uuid, os

app = FastAPI()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class Text(BaseModel):
    text: str

@app.post("/tts")
def tts(req: Text):
    filename = f"{uuid.uuid4()}.mp3"

    audio = client.audio.speech.create(
        model="gpt-4o-mini-tts",
        voice="alloy",
        input=req.text,
        response_format="mp3"
    )

    with open(filename, "wb") as f:
        f.write(audio)

    return {"audio_url": f"https://SENIN-RENDER-URL/{filename}"}
