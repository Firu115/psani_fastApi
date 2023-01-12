import random

from fastapi import FastAPI, Body, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import random as rnd

from auth.auth_bearer import JWTBearer
from models import UserSchema, UserLoginSchema
from auth.auth_handler import signJWT, decodeJWT
from databaze_prikazy import *

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:5174', 'http://localhost:5173'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.get('/api/ja', tags=['user'], dependencies=[Depends(JWTBearer())])
async def ja(token: str = Depends(JWTBearer())):
    print("nkdsnfjsjf")
    return get_uziv_info(decodeJWT(token)['email'])


@app.post('/api/registrace', tags=['user'])
async def create_user(user: UserSchema = Body(...)):
    existuje = get_jmeno_by_email(user.email)
    if existuje:
        raise HTTPException(
            status_code=409,
            detail='Tento email už je zaregistrovaný'
        )
    # uzivatel_do_db(user)
    return signJWT(user)


@app.post('/api/prihlaseni', tags=['user'])
async def user_login(user: UserLoginSchema = Body(...)):
    c = check_uziv(user)
    if c == True:
        return signJWT(user)
    elif c == 'uziv':
        return {'error': 'Špatný uživatel'}
    else:
        return {'error': 'Špatné heslo'}


@app.get('/api/lekce')
async def getLekceASplnene(token: str = Depends(JWTBearer(False))):  # aby to bylo nepovinny
    if token is None:
        return {'lekce': dict(get_lekce()), 'dokoncene': []}
    uziv = decodeJWT(token)
    return {'lekce': dict(get_lekce()), 'dokoncene': get_splnene_lekce(uziv['email'])}


@app.get('/api/lekce/{pismena_lekce}')
async def getCviceniVLekci(pismena_lekce, token: str = Depends(JWTBearer(False))):
    try:
        cviceni = get_cviceni_v_lekci(pismena_lekce)
        dokonceno = get_splnene_cviceni_v_lekci(decodeJWT(token)['email'], pismena_lekce)

        return {"cviceni": cviceni, "dokonceno": dokonceno}
    except:
        return {'error': 'Taková lekce bohužel neexistuje'}


@app.get('/api/cvic/{pismena_lekce}/{cislo}', dependencies=[Depends(JWTBearer())])
async def getText(pismena_lekce: str, cislo: int):
    if pismena_lekce in dict(get_lekce()).values():
        cviceni_v_lekci = get_cviceni_v_lekci(pismena_lekce)
        print(cviceni_v_lekci, cislo)
        if len(cviceni_v_lekci) > cislo-1:
            if cviceni_v_lekci[cislo-1][1] is None: # pokud je to lekce se slovy
                slova = list(cviceni_v_lekci[cislo-1][2].split(","))[:-1]
                delka = 20
                text = []
                for i in range(delka + 1):
                    text.append(random.choice(slova) + " ")
                text[len(text) - 1] = text[len(text) - 1][:-1]
            else:
                delka = 20 * 4  # 4 pro jedno slovo
                text = []
                slovo = ''
                for i in range(delka + 1):
                    if i % 4 == 0 and i != 0:
                        if i != delka: slovo += ' '  # na konci textu nechci mezeru
                        text.append(slovo)
                        slovo = ''
                    slovo += random.choice(pismena_lekce)
            return {'text': text, 'pismena': pismena_lekce}
        else:
            return {'error': 'Takové cvičení bohužel neexistuje'}
    else:
        return {'error': 'Taková lekce bohužel neexistuje'}
