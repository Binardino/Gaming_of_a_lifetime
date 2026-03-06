FROM python:3.11

# Variables d’environnement propres
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

#set environment variables for streamlit
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

# Update Linux and upgrade pip in one layer
RUN apt-get update && \
    apt-get clean && \
    apt-get install -y --no-install-recommends \
        gcc g++ curl cmake build-essential \
        libssl-dev libffi-dev default-libmysqlclient-dev && \
    rm -rf /var/lib/apt/lists/*

# Install Poetry
ENV POETRY_VERSION=2.2.1
RUN pip install --upgrade pip poetry==${POETRY_VERSION}

# Desactivate virtualenvs Poetry (Docker = venv)
RUN poetry config virtualenvs.create false

# Create non-root user
RUN useradd -m -d /home/gaming_reader -s /bin/bash gaming_reader && \
    mkdir -p /home/gaming_reader/.streamlit

# Set HOME environment variable
ENV HOME=/home/gaming_reader

#set working directory to /app level
WORKDIR /app

# Copy Poetry files (Docker cache optimised)
COPY pyproject.toml poetry.lock* ./

# Installer dependencies
RUN poetry install --only main --no-root --no-interaction --no-ansi

#COPY all contents
COPY . .

# Create user with a home directory
RUN chown -R gaming_reader:gaming_reader /app /home/gaming_reader

#Expose port 8501
EXPOSE 8501

# Switch to user
USER gaming_reader

# HEALTHCHECK instruction tells Docker how to test a container check whether still working
HEALTHCHECK --interval=30s --timeout=5s --start-period=15s --retries=3 \
    CMD curl --fail http://localhost:8501/_stcore/health || exit 1

#run app in Streamlit
ENTRYPOINT ["streamlit", "run", "home_page.py", "--server.port=8501", "--server.address=0.0.0.0"]