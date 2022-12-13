CREATE DATABASE docker;
CREATE USER docker with encrypted password '1234';
GRANT ALL PRIVILEGES ON DATABASE docker TO docker;
-- CREATE TABLE customer_clustering(
--     -- id SERIAL,
--     Год_рождения INTEGER,
--     Уровень_образования varchar(50),
--     Семейное_положение TEXT,
--     Доход double precision,
--     Маленькие_дети BIGINT,
--     Подростки BIGINT,
--     Регистрация DATE,
--     Последняя_закупка BIGINT,
--     Вино BIGINT,
--     Фрукты BIGINT,
--     Мясо BIGINT,
--     Рыба BIGINT,
--     Сладкое BIGINT,
--     Золото BIGINT,
--     Покупки_со_скидкой BIGINT,
--     Покупки_через_сайт BIGINT,
--     Покупки_из_каталогa BIGINT,
--     Покупки_в_магазине BIGINT,
--     Посещение_сайта_за_месяц BIGINT,
--     Реклама_3 BIGINT,
--     Реклама_4 BIGINT,
--     Реклама_5 BIGINT,
--     Реклама_1 BIGINT,
--     Реклама_2 BIGINT,
--     Жалобы TEXT,
--     Последняя_рекламная_компания TEXT

-- );
-- set datestyle = euro;
-- -- COPY customer_clustering FROM '/etc/customer_clustering.csv' WITH (FORMAT csv);
-- COPY customer_clustering FROM '/etc/customer_clustering.csv' DELIMITER ',' CSV HEADER;