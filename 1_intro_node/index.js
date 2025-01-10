// Haciendo la importacion en commonJS
const { multiplicar, restar, sumar } = require("./funciones");

console.log("Hola mundo");

const nombre = "Eduardo";
// Indica que su valor puede cambiar
let habilitado = true;

habilitado = false;
habilitado = true;
habilitado = false;

console.log(habilitado);
