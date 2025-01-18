import { conexion } from "../conexion.js";
import { crearEquipoSerializer } from "./serializers/equipo.serializer.js";
import { paginationSerializer } from "../utils.js";

export const crearEquipo = async (req, res) => {
  const dataValidada = crearEquipoSerializer.parse(req.body);

  const nuevoEquipo = await conexion.equipo.create({ data: dataValidada });

  return res.json({
    message: "Equipo creado exitosamente",
    content: nuevoEquipo,
  });
};

export const listarEquipos = async (req, res) => {
  console.log(req.query);
  // PAGINACION
  const { page, perPage } = req.query;
  let skip, take;
  if (page && perPage) {
    // skip > cuantos elemento se debe se saltar
    skip = (Number(page) - 1) * Number(perPage);
    // take > cuantos elementos se debe tomar luego de saltarse
    take = Number(perPage);
  }

  const filtros = {};
  if (req.query.nombre) {
    // Si queremos hacer la busqueda mediante una similitud del resultado usamos contains
    filtros.nombre = { contains: req.query.nombre };
  }
  if (req.query.estadio) {
    filtros.estadio = { contains: req.query.estadio };
  }

  // Crear el controlador para listar todos los equipos
  // Cualquier usuario (identificado o no) puede acceder a esta informacion
  const equipos = await conexion.equipo.findMany({
    where: filtros,
    skip,
    take,
  });

  const totalEquipos = await conexion.equipo.count({
    where: filtros,
  });

  const pageInfo = paginationSerializer(
    totalEquipos,
    Number(page),
    Number(perPage)
  );
  return res.json({
    content: equipos,
    pageInfo,
  });
};
``;
