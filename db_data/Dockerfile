FROM postgres:latest

# Copy the init.sql file to the container
# Add initialization scripts
COPY init.sql /docker-entrypoint-initdb.d/

# Set environment variables
ENV POSTGRES_USER=${POSTGRES_USER}
ENV POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
ENV POSTGRES_DB=${POSTGRES_DB}
ENV POSTGRES_HOST=${POSTGRES_HOST}
ENV POSTGRES_PORT=${POSTGRES_PORT}

# Mount a volume for persistent data
#VOLUME /var/lib/postgresql/data

# Expose the PostgreSQL port
EXPOSE ${POSTGRES_PORT}