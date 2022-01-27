const sqlite3 = require('sqlite3');

let db = new sqlite3.Database('backend');

db.run('CREATE TABLE tasks(id INT AUTO_INCREMENT, description VARCHAR(255))');

db.close();