import express from "express";
import { usuarioEnrutador } from "./routes/usuario.routes.js";
import { equipoEnrutador } from "./routes/equipo.routes.js";
import { ZodError } from "zod";
import { Prisma } from "@prisma/client";
import cors from "cors";

const servidor = express();
// CORS para poder permitir peticiones a mi backend
servidor.use(cors({ origin: ["http://127.0.0.1:5500"] }));

servidor.use(express.json());

// Agregamos las rutas de nuestros enrutadores
servidor.use(usuarioEnrutador);
servidor.use(equipoEnrutador);

servidor.use((error, req, res, next) => {
  // Aca manejaremos los errores que podamos tener en toda nuestra aplicacion
  // Para manejar el error global se tiene que declara LUEGO de todas las rutas sino evitara que ingrese al controlador adecuado
  if (error instanceof ZodError) {
    return res.status(400).json({
      message: "Error al recibir la informacion",
      content: error.errors,
    });
  }

  if (error instanceof Prisma.PrismaClientKnownRequestError) {
    // la clase PrismaClientKnownRequestError tiene la propiedad meta en la cual almacena el modelo que emitio el error al no encontrar la coincidencia en la bd
    return res.status(404).json({
      message: `El ${error.meta.modelName} no existe`,
    });
  }

  return res.status(400).json({
    message: "Error al hacer la peticion",
  });
});

servidor.listen(process.env.PORT, () => {
  console.log(
    `Servidor corriendo exitosamente en el puerto ${process.env.PORT}`
  );
});
