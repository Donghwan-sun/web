# FastAPI 웹 백앤드 기초 구현
  - 회원가입 기능 구현
  - 로그인 기능 구현
  - 로그아웃 기능 구현

# Requirements
  - Python 3.10
  - fastapi
  - uvicorn
  - postgresql
  - fastapi-jwt-auth
  - python-dotenv
  - SQLAlchemy
  - psycopg2

# How to run the example:
  - 가상환경 설정 python -m venv ./venv
  - mkdir .env 설정
    ```
     DATABASE_PORT=
     POSTGRES_PASSWORD=
     POSTGRES_USER=
     POSTGRES_DB=
     POSTGRES_HOST=
     POSTGRES_HOSTNAME=
     ACCESS_TOKEN_EXPIRES_IN=
     REFRESH_TOKEN_EXPIRES_IN=
     JWT_ALGORITHM=
     CLIENT_ORIGIN=
     JWT_PRIVATE_KEY=
     JWT_PUBLIC_KEY=
    ```
  - terminal docker-compose up
  - python3 main.py