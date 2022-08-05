#!/usr/bin/env sh
Color_Off="\033[0m" # Text Color Reset
Green="\033[0;32m"  # Green
Red="\033[0;31m"    # Red

DB_NAME="my_db"
DB_USERNAME="my_db_user"
DB_PASSWORD="password"

echo "${Green}Make sure your postgres database is running (see sql-development.md instruction)':${Color_Off}";



echo "${Green}Setting up Postgres Database${Color_Off}";

echo "Dropping '$DB_NAME' database. If this hangs, run the following command: killall -9 psql";
dropdb $DB_NAME --if-exists

echo "Removing any existing db user: $DB_USERNAME";
dropuser $DB_USERNAME --if-exists

echo "Creating database: $DB_NAME"
createdb "$DB_NAME"


echo "Setting up database schema..."
# Connect to `database` database & feed it the SQL script that sets up the postgres DB.
psql "$DB_NAME" < ./sql/setup-db-schema.sql

echo "Populating database with data (this may take a while)..."
psql "$DB_NAME" < ./sql/populate-db.sql -q



echo "Creating database user: $DB_USERNAME";
psql template1 -c "CREATE user $DB_USERNAME;"
psql template1 -c "ALTER user $DB_USERNAME password '$DB_PASSWORD';"


echo "Assigning ownership of $DB_NAME database to $DB_USERNAME"
psql template1 -c "GRANT ALL on DATABASE $DB_NAME to $DB_USERNAME;"
psql "$DB_NAME" -c "GRANT ALL on ALL tables IN SCHEMA public to $DB_USERNAME"

# echo "______________";
# echo "\n"