FROM python:3.12-alpine
WORKDIR /app
COPY solution.py /app/solution.py
COPY s /app/s
ENTRYPOINT ["python", "/app/solution.py"]