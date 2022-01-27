const express = require('express');
const sqlite3 = require('sqlite3');
const Sequelize = require('sequelize');

const app = express();

app.use(express.urlencoded({extended: true}));


const sequelize = new Sequelize('backend',null,null,
{
    dialect: 'sqlite',
    Storage: './backend'
});

app.post('/pendientes', function(req, res) {
    // db.run(`INSERT INTO tasks(description) VALUES(?)`, req.body.description);
    res.send("insercion");
});

app.listen(3000);
