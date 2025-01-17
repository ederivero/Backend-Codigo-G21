import { conexion } from "../conexion.js";
import { crearEquipoSerializer } from "./serializers/equipo.serializer.js";

export const crearEquipo = async (req, res) => {
  const dataValidada = crearEquipoSerializer.parse(req.body);

  const nuevoEquipo = await conexion.equipo.create({ data: dataValidada });

  return res.json({
    message: "Equipo creado exitosamente",
    content: nuevoEquipo,
  });
};
