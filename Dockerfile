ARG PYTHON_VERSION=3.11-slim

# ===== Base build stage =====
FROM python:${PYTHON_VERSION} AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    UVICORN_WORKERS=2 \
    UVICORN_PORT=8000 \
    UVICORN_HOST=0.0.0.0

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml README.md /app/
COPY src /app/src

RUN pip install --upgrade pip && \
    pip install -e .

# ===== Runtime stage (slim) =====
FROM python:${PYTHON_VERSION} AS runtime

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    UVICORN_WORKERS=2 \
    UVICORN_PORT=8000 \
    UVICORN_HOST=0.0.0.0

WORKDIR /app

# Create a non-root user
RUN useradd -ms /bin/bash appuser

# Copy installed site-packages and application code from build stage
COPY --from=base /usr/local/lib /usr/local/lib
COPY --from=base /usr/local/bin /usr/local/bin
COPY --from=base /app /app

EXPOSE 8000

# Basic healthcheck hitting FastAPI docs
HEALTHCHECK --interval=30s --timeout=5s --start-period=20s --retries=3 \
  CMD python -c "import socket; s=socket.socket(); s.settimeout(2); s.connect(('127.0.0.1', 8000)); s.close()" || exit 1

USER appuser

CMD ["uvicorn", "scipaper.main:app", "--host", "0.0.0.0", "--port", "8000"]


