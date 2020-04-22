FROM postgres

## Automatically create a user that owns a database
ENV POSTGRES_DB wwv
ENV POSTGRES_USER wwv
ENV POSTGRES_PASSWORD wwv

# Run the rest of the commands as the ``postgres`` user
USER postgres

# Expose the PostgreSQL port
EXPOSE 5432

# Final step: add the migrations and base data
COPY ./migrations  /docker-entrypoint-initdb.d
# COPY ./data/*_file /docker-entrypoint-initdb.d/
