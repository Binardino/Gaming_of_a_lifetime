FROM postgres:16-alpine

RUN mkdir /docker-entrypoint-initdb.d/csv_file
COPY csv /docker-entrypoint-initdb.d/csv_file

# Expose the PostgreSQL port
EXPOSE 5432