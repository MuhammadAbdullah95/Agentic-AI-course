from fastapi import FastAPI
from schema import SignUp, UserInfo

app = FastAPI()



@app.post("/signup", response_model=UserInfo)
def signup(user: SignUp):
    return user
