FROM postgres:latest

RUN mkdir /docker-entrypoint-initdb.d/csv_file
COPY csv /docker-entrypoint-initdb.d/csv_file

# Set environment variables
ENV POSTGRES_USER=${POSTGRES_USER}
ENV POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
ENV POSTGRES_DB=${POSTGRES_DB}
ENV POSTGRES_PORT=${POSTGRES_PORT}
#bind mount
VOLUME /db_data/db

# Expose the PostgreSQL port
EXPOSE ${POSTGRES_PORT}