[Git]: https://git-scm.com/downloads
[PYTHON]: https://www.python.org/
[SQLALCHEMY]: https://www.sqlalchemy.org/
[FASTAPI]: https://fastapi.tiangolo.com/
[POSTGRESQL]: https://www.postgresql.org/

# logyca_test_backend

_RESTapi para prueba de logyca, api genera el calculo de números primos y número primos gemelos.
 con posiblidad de guardar en base de datos local_

### Pre-requisitos 📋

Tener instalado:

- [Git]
- [PYTHON]
- [SQLALCHEMY]
- [FASTAPI]
- [POSTGRESQL]

## Comenzando ⚡

1. Clonar el repositorio
```
https://github.com/JesusGalindoB/logyca_test_backend.git
```
2. Instalar dependencias
```
pip install -r requirements.txt
```

3. Levantar app
```
uvicorn main:app --reload
```
3. Endpoints
```
/prime_numbers/{n}
/twin_prime/{n}
/prime_numbers_db/{n}
/twin_primes_db/{n}

/docs/ --> documentación de la API.
```

## Construido con 🛠️

- [Git]
- [PYTHON]
- [SQLALCHEMY]
- [FASTAPI]
- [POSTGRESQL]
