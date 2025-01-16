import express from "express";
import { usuarioEnrutador } from "./routes/usuario.routes.js";

const servidor = express();
servidor.use(express.json());

// Agregamos las rutas de nuestros enrutadores
servidor.use(usuarioEnrutador);

servidor.listen(process.env.PORT, () => {
  console.log(
    `Servidor corriendo exitosamente en el puerto ${process.env.PORT}`
  );
});
