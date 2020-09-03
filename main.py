# FastAPI
from fastapi import FastAPI, Path, status, Depends
from pydantic import BaseModel

# Database
from database import engine, SessionLocal
from sqlalchemy.orm import Session
import models 
from create_read import (
    get_prime_numbers, 
    create_prime_numbers, 
    get_prime_twin, 
    create_prime_twin
)

# Utilities
from utilities import prime_number_generator, twin_prime_generator

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/prime_numbers/{n}", status_code=status.HTTP_200_OK)
def prime_numbers(n: int = Path(..., ge=1)):
    prime_numbers = prime_number_generator(n)

    response_object = {
        "results": prime_numbers
    }
    return response_object


@app.get("/twin_primes/{n}", status_code=status.HTTP_200_OK)
def twin_prime(n: int = Path(..., ge=1)):
    twin_prime_list = twin_prime_generator(n)

    response_object = {
        "results": twin_prime_list
    }
    return response_object


@app.get("/prime_numbers_db/{n}", status_code=status.HTTP_200_OK)
def prime_numbers_db(n: int = Path(..., ge=1), db: Session = Depends(get_db)):
    get_result = get_prime_numbers(db, base_number=n)
    
    if get_result:
        return{
            "results": get_result.result
        }
    else:
        create_in_db = create_prime_numbers(db, n).result
        return {
            "results": create_in_db
        }


@app.get("/twin_primes_db/{n}", status_code=status.HTTP_200_OK)
def twin_primes_db(n: int = Path(..., ge=1), db: Session = Depends(get_db)):
    get_result = get_prime_twin(db, base_number=n)
    
    if get_result:
        return{
            "results": get_result.result
        }
    else:
        create_in_db = create_prime_twin(db, n).result
        return {
            "results": create_in_db
        }
