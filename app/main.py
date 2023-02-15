from fastapi import FastAPI, Response
import foodemoji
import emoji
from dataclasses import dataclass
import os

EMOJI_LANG = os.getenv("EMOJI_LANG", "en")

@dataclass
class InputText:
    text: str

@dataclass
class EmojiText:
    emojifiedText: str

@dataclass
class Status:
    ok: bool

app = FastAPI()

@app.get("/status")
async def status():
    return Status(true)

@app.post("/emojify")
async def emojifiy(text: InputText):
    decoratedText = foodemoji.decorate(text.text)
    return EmojiText(emoji.emojize(decoratedText, language=EMOJI_LANG))
