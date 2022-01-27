const express = require('express');
const path = require('path');
const Cors = require('cors');
//? rutas
const user = require("../routes/user.routes");

class Server {
    constructor() {
        this.app = express();
        this.port = process.env.PORT;
        //? Middlewares
        this.middlewares();
        //? rutas 
        this.routes();
    }

    middlewares() {
        //? cors
        this.app.use( Cors() );
        //? lectura y parse del body 
        this.app.use(express.json());
        //? consumir carpeta publica
        this.app.use(express.static("public") );
    }

    routes() {
        this.app.use('/api/usuarios',user);
    }

    listen() {
        this.app.listen(this.port, () =>{ 
            console.log('sever running on port',this.port);
        });
    }
}

module.exports = Server;