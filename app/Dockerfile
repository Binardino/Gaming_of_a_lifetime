FROM python:3.11

# Variables d’environnement propres
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Update Linux and upgrade pip in one layer
RUN apt-get update && \
    apt-get clean && \
    apt-get install -y gcc g++ curl && \
    apt-get install -y default-libmysqlclient-dev && \
    apt-get install -y cmake build-essential libssl-dev libffi-dev && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --upgrade pip

# Install Poetry
ENV POETRY_VERSION=2.2.1
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"

# Desactivate virtualenvs Poetry (Docker = venv)
RUN poetry config virtualenvs.create false

#set working directory to /app level
WORKDIR /app

# Copy Poetry files (Docker cache optimised)
COPY pyproject.toml poetry.lock* ./

# Installer dependencies
RUN poetry install --only main --no-root --no-interaction --no-ansi

#COPY all contents
COPY . .

#Expose port 8501
EXPOSE 8501

#set environment variables for streamlit
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

# Create user with a home directory
RUN useradd -m -d /home/gaming_reader -s /bin/bash gaming_reader && \
    mkdir -p /home/gaming_reader/.streamlit && \
    chown -R gaming_reader:gaming_reader /home/gaming_reader

# Switch to user
USER gaming_reader

# Set HOME environment variable
ENV HOME=${USER_HOME}

# HEALTHCHECK instruction tells Docker how to test a container check whether still working
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

#run app in Streamlit
ENTRYPOINT ["streamlit", "run", "home_page.py", "--server.port=8501", "--server.address=0.0.0.0"]