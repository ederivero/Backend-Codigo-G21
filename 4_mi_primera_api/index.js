import express from "express";

const servidor = express();
// Configurar lo que podemos recibir por el body
// express.json() > indicamos que el contenido que podemos recibir por el body puede ser en formato application/json
servidor.use(express.json());
// Sera otro formato para recibir informacion por el body en formato x-www-url-encoded
// DEPRECADO: ya no se recomienda utilizar
// servidor.use(express.urlencoded());
// Para recibir por el body puro texto
servidor.use(express.text());

servidor.get("/", (req, res) => {
  res.json({
    message: "Bienvenido a mi API",
  });
});

servidor.post("/crear-usuario", (req, res) => {
  // req.body es todo el cuerpo que me envia el cliente
  console.log(req.body);

  res.json({
    message: "Usuario creado exitosamente",
  });
});

// Puerto a utilizar: 3000
servidor.listen(3000, () => {
  console.log("Servidor corriendo exitosamente");
});
