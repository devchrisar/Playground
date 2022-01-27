const argv = require('./config/yargs');
const colors = require('colors');
const { crearArchivo } = require('./helpers/multiplicar');
// const [ , , arg3 = 'base=5' ] = process.argv;
// const [ , base=5 ] = arg3.split('=');
// console.log('base: yargs', argv.b)
crearArchivo( argv.b, argv.l, argv.h )
    .then( nombreArchivo => console.log(nombreArchivo.red,'creado'.red))
    .catch( err => console.log(err));