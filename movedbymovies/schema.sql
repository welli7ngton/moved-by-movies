DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS user_movies;
DROP TABLE IF EXISTS movies;
DROP TABLE IF EXISTS purchases;
DROP TABLE IF EXISTS admin;

CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT NOT NULL,
  email TEXT UNIQUE NOT NULL,
  birth DATETIME NULL,
  password TEXT NOT NULL,
  bio TEXT NULL,
  cep TEXT NULL,
  city TEXT NULL,
  address TEXT NULL,
  street TEXT NULL,
  number TEXT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE user_movies (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  movie_id INTEGER NOT NULL,
  FOREIGN KEY (user_id) REFERENCES users(id),
  FOREIGN KEY (movie_id) REFERENCES movies(id)
);

CREATE TABLE movies (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  plot TEXT NULL,
  released TEXT NULL,
  runtime TEXT NULL,
  gender TEXT NULL,
  actors TEXT NULL,
  director TEXT NULL,
  poster TEXT NULL,
  totalSeasons TEXT NULL,
  country TEXT NULL,
  language TEXT NULL,
  awards TEXT NULL,
  imdbRating FLOAT,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE purchases (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER,
  movie_id INTEGER,
  purchase_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users(id),
  FOREIGN KEY (movie_id) REFERENCES movies(id)
);

CREATE TABLE admin (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER,
  FOREIGN KEY (user_id) REFERENCES users(id)
);

INSERT INTO users(username, email, password)
VALUES("welli7ngton", "wellington@admin.com", "scrypt:32768:8:1$lKJvDyRQRJKfJ6Me$6e870a499da612c9b9f501287e0f920fd307d721fa9da4f97a98298bbf522e9060c74e8447c4b39c46882bdcbeaab328b8b109225a131778817414c82e57decf");

INSERT INTO admin(user_id) VALUES(1);
