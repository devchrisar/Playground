const express = require('express');

const app = express();

app.get("/", function(req, res) {
    res.sendFile('html/index.html', 
    {
        root: __dirname
    });
})
app.listen(3000);