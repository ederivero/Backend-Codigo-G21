import JWT from "jsonwebtoken";
import { conexion } from "./conexion.js";

export const validarUsuario = async (req, res, next) => {
  // Si la informacion luego de validarla cumple con todo, entonces dejaremos pasar al siguien controlador con la funcion next

  // La informacion de las cabecera de la peticion
  const { authorization } = req.headers;

  if (!authorization) {
    return res.status(403).json({
      message: "Se necesita una token para realizar esta peticion",
    });
  }

  // En el header de authorization debe de enviar la token en el siguiente formato Bearer xxxx.yyyy.zzzz
  const token = authorization.split(" ")[1];
  // ['Bearer', 'xxxx.yyyy.zzz']

  if (!token) {
    return res.status(403).json({
      message: "El formato de la token debe ser Bearer YOUR_TOKEN",
    });
  }

  // El payload devolvera toda la informacion que le colocamos al momento de crear la token
  const payload = JWT.verify(token, process.env.SECRET_KEY);
  const usuarioEncontrado = await conexion.usuario.findUniqueOrThrow({
    where: { id: payload.usuarioId },
  });

  // Dentro del req (request) podemos agregar informacion
  req.user = usuarioEncontrado;
  next();
};
