from pydantic import BaseModel, Field, EmailStr


class UserSchema(BaseModel):
    jmeno: str = Field(...)
    email: EmailStr = Field(...)
    heslo: bytes = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "jmeno": "Joe Doe",
                "email": "joe@xyz.com",
                "heslo": "ne"
            }
        }


class UserLoginSchema(BaseModel):
    jmeno_nebo_email: str = Field(...)
    heslo: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "jmeno_nebo_email": "joe@xyz.com",
                "heslo": "ne"
            }
        }
