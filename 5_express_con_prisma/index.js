import express from "express";
// Esta libreria se agrega cuando creamos los tipos de prisma
// npx prisma migrate generate
// Cuando creamos una nueva migracion y se ejecuta en la bd
import Prisma from "@prisma/client";

const conexion = new Prisma.PrismaClient();
const servidor = express();

servidor.use(express.json());

servidor.post("/registro", async (req, res) => {
  try {
    const data = req.body; // {nombre: '', email: '', nickName: ''}

    // resultado > seria la ejecucion correcta de la funcion
    const resultado = await conexion.usuario.create({
      data, //: { nombre: data.nombre, email: data.email, nickName: data.nickName },
    });
    // ACA PONES TU MENSAJE
    return res.json({
      message: "Usuario creado exitosamente",
      content: resultado,
    });
  } catch (error) {
    // obtenemos el error de la ejecucion del proceso asincrono
    if (error instanceof Prisma.Prisma.PrismaClientValidationError) {
      return res.json({
        message: "error al hacer la peticion a la bd",
      });
    }
    return res.json({
      mesage: "Error al crear el usuario",
    });
  }
});

servidor.listen(process.env.PORT, () => {
  console.log(
    `Servidor corriendo exitosamente en el puerto ${process.env.PORT}`
  );
});
