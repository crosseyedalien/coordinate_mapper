FROM postgres

## Automatically create a user that owns a database
ENV POSTGRES_DB cmapper
ENV POSTGRES_USER cmapper
ENV POSTGRES_PASSWORD cmapper

# Run the rest of the commands as the ``postgres`` user
USER postgres

# Expose the PostgreSQL port
EXPOSE 5432

# Final step: add the migrations and base data
COPY ./migrations  /docker-entrypoint-initdb.d
# COPY ./data/*_file /docker-entrypoint-initdb.d/
