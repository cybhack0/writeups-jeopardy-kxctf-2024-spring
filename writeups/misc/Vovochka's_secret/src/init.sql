CREATE TABLE users(
    telegram_id int,
    status_code int
);

CREATE TABLE secrets(
    id SERIAL,
    name varchar(100),
    creation_time timestamp,
    secret varchar(100),
    password varchar(100)
)
-- The flag was sent to the bot as the first secret