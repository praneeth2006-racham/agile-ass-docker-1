FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
# Keep the container alive or run tests/app as needed
CMD ["python", "app/calculator.py"]
