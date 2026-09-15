FROM python:3.12-alpine
WORKDIR /app
COPY solution.py .
ENTRYPOINT ["python", "/app/solution.py"]