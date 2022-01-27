require('dotenv').config();
const express = require('express');
const hbs = require('hbs');

const app = express();
const port = process.env.PORT || 8080;
//handlebars
app.set('view engine', 'hbs');
hbs.registerPartials(__dirname + '/views/partials')
// Servir contenido estático
app.use( express.static('public') );
app.get('/', (req, res) => {
    res.render('home', {nombre: 'Christopher Arias', titulo: 'curso de node'});
})
app.get('/generic', (req, res) => {
    res.render('generic', {nombre: 'Christopher Arias', titulo: 'curso de node'});
})
app.get('/elements', (req, res) => {
    res.render('elements', {nombre: 'Christopher Arias', titulo: 'curso de node'});
})
app.get('*', (req, res) => {
    res.send('404 | Page Not Found');
})
app.listen(port, () => {
    console.log(`listening on => http://localhost:` + port);
});