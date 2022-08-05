DROP TABLE IF EXISTS Users;
CREATE TABLE Users (
  id serial NOT NULL,
  PRIMARY KEY ("id"),
  username VARCHAR(21)
);