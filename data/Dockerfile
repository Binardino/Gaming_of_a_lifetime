FROM postgres:latest

# Copy the init.sql file to the container
# Add initialization scripts
COPY init.sql /docker-entrypoint-initdb.d/

# Set environment variables
ENV POSTGRES_USER=myuser
ENV POSTGRES_PASSWORD=mypassword
ENV POSTGRES_DB=mydatabase

# Mount a volume for persistent data
VOLUME /var/lib/postgresql/data

# Expose the PostgreSQL port
EXPOSE 5432