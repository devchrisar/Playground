const express = require("express");
const app = express();

app.use(express.json({}));
app.use(express.urlencoded({ extended: false }));
const places = [
    {
        'title': 'mi casa',
        'description': 'mi casita',
        'address': 'al lado de la esquina',
    },
    {
        'title': 'mi casa',
        'description': 'mi casita',
        'address': 'al lado de la esquina',
    },
    {
        'title': 'mi casa',
        'description': 'mi casita',
        'address': 'al lado de la esquina',
    }
]

app.get("/",(req, res) => 
{
    res.json(places);
})

app.post("/",(req,res) =>
{
    res.json(req.body);
})

app.use(express.static('public'));

const port = 3000;
app.listen(port, function()
{
    console.log('Server running on port: ' + port);
})