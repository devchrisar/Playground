const http = require('http');
const port = process.env.PORT || 8080
http.createServer((req, res) => {
    // res.write(200, {'Content-Type': 'application/json'})
    res.setHeader('Content-Disposition', 'attachment; filename=listado.csv')
    res.write(200, {'Content-Type': 'application/csv'})
    res.write( 'id, nombre\n');
    res.write( '1, Maria\n');
    res.write( '2, Juan\n');
    res.write( '3, Fernando\n');
    res.write( '4, Pedro\n');
    res.end();
})
.listen(port);
console.log(`listening on http://localhost:${port}`);