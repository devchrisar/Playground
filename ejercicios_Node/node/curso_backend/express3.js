const express = require('express');
const app = express();

app.use(express.urlencoded({ extended: true }));
app.use(express.json());

app.get("/saludo", function(req, res) 
{
    res.send(`Hello World! ${req.query.name}`);
});

app.post("/", function(req, res) 
{
    res.send(`Hello World! ${req.body.name}`);
});

app.listen(3000);