CREATE DATABASE docker;
CREATE USER docker with encrypted password '1234';
GRANT ALL PRIVILEGES ON DATABASE docker TO docker;