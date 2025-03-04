-- create
-- user server
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON hbtn_0d_tvshows.* TO 'user_0d_1'@'localhost';