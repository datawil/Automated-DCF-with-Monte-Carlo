# Stage 1: Build
FROM python:3.9-slim as builder

WORKDIR /app
COPY requirements.txt .

RUN pip install --user --no-cache-dir -r requirements.txt

# Stage 2: Runtime
FROM python:3.9-slim

WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY . .

# Ensure scripts in .local are usable
ENV PATH=/root/.local/bin:$PATH

# Corrected command for your new structure
CMD ["uvicorn", "api.fastapi_app:app", "--host", "0.0.0.0", "--port", "8000"]