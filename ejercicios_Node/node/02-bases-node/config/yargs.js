const argv = require("yargs")
  .option("b", {
    alias: "base",
    type: "number",
    demandOption: true,
    describe: "base a utilizar para la multiplicacion del numero"
  })
  .option("l", {
    alias: "listar",
    type: "boolean",
    default: false,
    describe: 'listado de la tabla a multiplicar'
  })
  .option("h", {
    alias: "hasta",
    type: "number",
    default: 10,
    describe: 'limite de la tabla a multiplicar'
  })
  .check((argv, options) => {
    if (isNaN(argv.b)) {
      throw "la base tiene que ser un numero";
    }
    return true;
  }).argv;

module.exports = argv;
