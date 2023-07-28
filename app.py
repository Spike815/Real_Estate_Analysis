from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, validator
from src.prediction import predict_new_data
from src.preprocessing import preprocess_new_data
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi import FastAPI, Request, status
from enum import Enum

app = FastAPI()

# Define what kind of inputs are expected and return error message if not match


class Type_property(str, Enum):
    HOUSE = "HOUSE"
    APARTMENT = "APARTMENT"


class Furnished(int, Enum):
    true = 1
    false = 0


class Terrace(int, Enum):
    true = 1
    false = 0


class Garden(int, Enum):
    true = 1
    false = 0


class Swimmingpool(int, Enum):
    true = 1
    false = 0


class State_of_the_building(str, Enum):
    good = "GOOD"
    new = "NEW"
    to_reno = "TO RENOVATE"
    just_reno = "JUST RENOVATED"
    to_rebuid = "TO REBUILD"

class Province(str, Enum):
    West_Vlaanderen = "West-Vlaanderen"
    Brussel="Brussel" 
    Antwerpen="Antwerpen"
    Oost_Vlaanderen="Oost-Vlaanderen"
    Liege="Liege"
    Vlaams_Brabant="Vlaams-Brabant"
    Hainaut="Hainaut"
    Brabant_wallon="Brabant wallon"
    Luxembourg="Luxembourg"
    Namur="Namur"
    Limburg="Limburg"

class Kitchen(str,Enum):
    Hyper_e = "Hyper equipped"
    Semi_e="Semi equipped"
    Not_e = "Not equipped"
    E = "Equipped"

class Property(BaseModel):
    type_of_property: Type_property
    number_of_bedrooms: int
    living_area: int
    furnished: Furnished
    terrace: Terrace
    terrace_area: int
    garden: Garden
    garden_area: int
    total_property_area: int
    total_land_area: int
    number_of_facades: int
    swimming_pool: Swimmingpool
    state_of_the_building: State_of_the_building
    province: Province
    kitchen: Kitchen
    digit: int


@app.get("/")
def read_root():
    return {"hello": 200}


@app.post("/predict/")
def predict(prop: Property):
    """ A route that takes required input and returns the predicted price.
    """
    dic = prop.model_dump()
    X = preprocess_new_data(dic)
    pred = predict_new_data(X)
    price = f"{int(pred)} euro"
    return {"status": 200,
            "prediction": price}


@app.exception_handler(RequestValidationError)
def validation_exception_handler(request: Request, exc: RequestValidationError):
    error_list = []
    for error in exc.errors():
        if error["type"] == "int_parsing":
            content = jsonable_encoder(
                {"Error": f'{error["loc"][1]} should be integer!'})
            error_list.append(content)
        elif error["type"] == "missing":
            content = jsonable_encoder(
                {"Error": f'{error["loc"][1]} value is missing!'})
            error_list.append(content)
        else:
            error_list = exc.errors()
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=error_list)
