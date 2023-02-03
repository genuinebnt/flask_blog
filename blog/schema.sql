DROP TABLE USERS IF EXISTS;
DROP TABLE POSTS IF EXISTS;

CREATE TABLE USERS(
    ID INT PRIMARY KEY AUTOINCREMENT,
    USERNAME TEXT UNIQUE NOT NULL,
    PASSWORD TEXT NOT NULL
);

CREATE TABLE POSTS(
    ID INT PRIMARY KEY AUTOINCREMENT,
    AUTHOR_ID INT NOT NULL,
    TITLE TEXT NOT NULL,
    BODY TEXT NOT NULL,
    CREATED_AT TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (AUTHOR_ID) REFERENCES USERS(ID)
)