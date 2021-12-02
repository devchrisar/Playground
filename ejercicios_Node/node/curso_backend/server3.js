const express = require('express');
const sqlite3 = require('sqlite3');

const app = express();

app.use(express.urlencoded({extended: true}));


let db = new sqlite3.Database('backend');

app.post('/pendientes', function(req, res) {
    db.run(`INSERT INTO tasks(description) VALUES(?)`, req.body.description);
    res.send("insercion");
});

app.listen(3000);

process.on('SIGINT', function(){
    console.log('servidor cerrado');
    db.close();
    process.exit();
})