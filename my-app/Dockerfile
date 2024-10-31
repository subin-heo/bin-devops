#First : Build Environment 컨테이너 1
FROM python:3.12-slim AS builder
WORKDIR /app

#poetry 설치
RUN pip install poetry
COPY pyproject.toml poetry.lock ./

#패키지 빌드
COPY . .
RUN poetry build -f wheel

#second: runtime environment 컨테이너 2
FROM python:3.12-slim
WORKDIR /app

#빌드된 .whl 파일 복사 설치
COPY --from=builder /app/dist/*.whl .
RUN pip install --no-cache-dir my_app-*.whl

#서버 실행
CMD ["uvicorn", "my_app.main:app", "--host", "0.0.0.0", "--port", "8000"]