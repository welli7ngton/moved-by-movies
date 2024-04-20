DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS movies;
DROP TABLE IF EXISTS purchases;
DROP TABLE IF EXISTS admin;
DROP TABLE IF EXISTS logs;

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
  uf TEXT NULL,
  is_admin INTEGER DEFAULT 0,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
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
  writer TEXT NULL,
  country TEXT NULL,
  language TEXT NULL,
  awards TEXT NULL,
  imdbRating FLOAT,
  price FLOAT NOT NULL DEFAULT 25.00,
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
  email TEXT NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE logs (
  admin_id INTEGER NOT NULL,
  type_operation TEXT NOT NULL,
  motivation TEXT NOT NULL,
  delete_date NOT NULL,
  FOREIGN KEY (admin_id) REFERENCES admin(id)
);

INSERT INTO users(username, email, password, is_admin)
VALUES("welli7ngton", "admin", "scrypt:32768:8:1$lKJvDyRQRJKfJ6Me$6e870a499da612c9b9f501287e0f920fd307d721fa9da4f97a98298bbf522e9060c74e8447c4b39c46882bdcbeaab328b8b109225a131778817414c82e57decf", 1);

INSERT INTO users(username, email, password)
VALUES("test", "test@test.com", "scrypt:32768:8:1$lKJvDyRQRJKfJ6Me$6e870a499da612c9b9f501287e0f920fd307d721fa9da4f97a98298bbf522e9060c74e8447c4b39c46882bdcbeaab328b8b109225a131778817414c82e57decf");

INSERT INTO admin(email, password) SELECT email, password FROM users WHERE id = 1;
