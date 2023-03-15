from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Request(BaseModel):
    origin_lat: float
    origin_lng: float
    destination_lat: float
    destination_lng: float
    haversine_distance: float
    hour: float


@app.post("/predict")
async def predict(request: Request):
    return {"origin_lat": request.origin_lat}
