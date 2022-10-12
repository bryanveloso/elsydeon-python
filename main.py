import markovify

from fastapi import FastAPI

app = FastAPI()

with open("quotes.txt") as f:
    text = f.read()
model = markovify.NewlineText(text, state_size=2)


@app.get("/")
async def root():
    return {"message": "Hello world!"}


@app.get("/markov")
async def markov():
    return {"response": model.make_short_sentence(280)}
