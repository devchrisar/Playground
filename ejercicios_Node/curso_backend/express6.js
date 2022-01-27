const express = require('express');

const app = express();

app.set("view engine", "ejs");

app.use("/assets", express.static("assets", {
    etag: false, //* protocolo para cachear
    maxAge: "1h", //* duracion total de cada copia en cache
})); //*middleware

app.get("/", function(req, res) {
    res.render("index");
})
app.listen(3000);