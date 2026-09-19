FROM python:3.12-alpine
WORKDIR /app
COPY solution.py .
COPY s .
ENTRYPOINT ["python", "/app/solution.py"]