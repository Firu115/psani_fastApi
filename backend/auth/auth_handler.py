# This file is responsible for signing , encoding , decoding and returning JWTS
import time
from typing import Dict

import jwt
from decouple import config
import databaze_prikazy;

JWT_SECRET = config("secret")
JWT_ALGORITHM = "HS256"


def token_response(token: str):
    return {
        "access_token": token
    }


# function used for signing the JWT string
def signJWT(user) -> Dict[str, str]:
    if hasattr(user, 'jmeno_nebo_email'):
        if databaze_prikazy.check(user.jmeno_nebo_email) == "email":  # email
            email = user.jmeno_nebo_email
        else:
            email = databaze_prikazy.get_email_by_jmeno(user.jmeno_nebo_email)[0][0]
    else:
        email = user.email

    payload = {
        "email": email,
        "expires": time.time() + 604_800  # týden
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return token_response(token)


def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}
