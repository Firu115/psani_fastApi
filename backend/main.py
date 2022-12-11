from fastapi import FastAPI, Body, Depends
from fastapi.middleware.cors import CORSMiddleware
import random as rnd

from auth.auth_bearer import JWTBearer
from models import UserSchema, UserLoginSchema
from auth.auth_handler import signJWT, decodeJWT
from databaze_prikazy import *

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/ja", tags=["user"], dependencies=[Depends(JWTBearer())])
async def ja(token: str = Depends(JWTBearer())):
    return decodeJWT(token)


@app.post("/registrace", tags=["user"])
async def create_user(user: UserSchema = Body(...)):
    uzivatel_do_db(user)
    return signJWT(user)


@app.post("/prihlaseni", tags=["user"])
async def user_login(user: UserLoginSchema = Body(...)):
    if check_uziv(user):
        return signJWT(user)
    return {
        "error": "Wrong login details!"
    }


@app.get("/lekce")
async def getLekce():
    return dict(get_lekce())


@app.get("/cvic/{pismena}", dependencies=[Depends(JWTBearer())])
async def getText(pismena):
    if pismena in dict(get_lekce()).values():
        if True:
            return {'text': ["Kokosák ", "Vyšukanej ", "Děvka ", "No"], 'pismena': pismena}

        delka = 8  # 4 pro jedno slovo
        text = []
        slovo = ""
        for i in range(delka + 1):
            print(i)
            if i % 4 == 0 and i != 0:
                if i != delka: slovo += " "  # na konci nechci mezeru
                text.append(slovo)
                slovo = ""
            slovo += pismena[rnd.randint(0, len(pismena) - 1)]
        return {'text': text, 'pismena': pismena}
    else:
        return {"error": "Taková lekce bohužel neexistuje"}
