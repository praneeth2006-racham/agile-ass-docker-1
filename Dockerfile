FROM python:3.10-slim

# Set the working directory inside the container to /workspace
WORKDIR /workspace

# Copy requirements first to leverage Docker caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project structure into /workspace
COPY . .

# Run the calculator script from the root of the workspace
CMD ["python", "app/calculator.py"]
