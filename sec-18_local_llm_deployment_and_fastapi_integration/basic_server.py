
# create apis using fastapi

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/contact-us")
def contact():
    return {"email": "ben_here@gmail.com"}
