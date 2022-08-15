CREATE TABLE "users" (
  "id" SERIAL UNIQUE PRIMARY KEY,
  "name" varchar(128) NOT NULL,
  "username" varchar(128) NOT NULL UNIQUE,
  "city" varchar(128) NOT NULL,
  "occupation" varchar(128) NOT NULL,
  "password" varchar(128) NOT NULL
);

INSERT INTO "users" ("name", "username", "city", "occupation", "password") VALUES
  ('vlad', 'vvrud', 'kyiv', 'coder', '12345678'),
  ('rick', 'pickle_rick', 'seatle', 'student', '12345678'),
  ('plumbus', 'pmbus', 'unknown', 'item', '12345678'),
  ('morty', 'old_morty', 'new york', 'scientist', '12345678');
