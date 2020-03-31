FROM mysql:5.7
# Add a database

EXPOSE 3306

COPY ./CreateTables.sql /docker-entrypoint-initdb.d
