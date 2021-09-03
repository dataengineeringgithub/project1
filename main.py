from fastapi import FastAPI
import uvicorn
import math
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

app = FastAPI()

@app.get("/")
def root():
    return "Welcome!"

@app.get("/get-item/{phone_number}")
def get_item(phone_number: str):
    coun = phonenumbers.parse(phone_number, "CH")
    
    country = geocoder.description_for_number(coun, "en")
    
    
    return country


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host ='0.0.0.0')



    
    

    
    
            
