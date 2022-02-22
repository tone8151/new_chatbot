from fastapi import FastAPI
from pydantic import BaseModel

from mainbot import MainBot  
from nega_posi import NegaPosi


app = FastAPI()

# リクエストbodyを定義
# class User(BaseModel):
#     user_id: int
#     name: str

class UserText(BaseModel):
    text: str

# @app.get("/hello/")
# async def index():
#     return {"yo": "Hello World"}


# @app.post("/user/")
# def create_user(user: User):
#     return {"res": "ok", "ID": user.user_id, "name": user.name}
    
@app.post("/user/")
def create_user(user_text: UserText):
    system = NegaPosi()
    bot = MainBot(system)
    reply: str = bot.run(user_text.text)
    return reply
    # return user_text.text