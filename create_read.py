from sqlalchemy.orm import Session
from utilities import prime_number_generator, twin_prime_generator
from models import PrimeNumber, PrimeTwin


def get_prime_numbers(db: Session, base_number: int):
    return db.query(PrimeNumber).filter(PrimeNumber.base_number == base_number).first()


def create_prime_numbers(db: Session, base_number: int):
    prime_numbers = prime_number_generator(base_number)
    db_number = PrimeNumber(base_number=base_number, result=prime_numbers)
    db.add(db_number)
    db.commit()
    db.refresh(db_number)
    return db_number


def get_prime_twin(db: Session, base_number: int):
    return db.query(PrimeTwin).filter(PrimeTwin.base_number == base_number).first()


def create_prime_twin(db: Session, base_number: int):
    prime_twin_list = twin_prime_generator(base_number)
    db_number = PrimeTwin(base_number=base_number, result=prime_twin_list)
    db.add(db_number)
    db.commit()
    db.refresh(db_number)
    return db_number
