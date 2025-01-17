import express from "express";
import asyncHandler from "express-async-handler";
import { crearEquipo } from "../controllers/equipo.controller.js";
import { validarAdmin, validarUsuario } from "../middlewares.js";
export const equipoEnrutador = express();

equipoEnrutador
  .route("/equipo")
  .post(
    asyncHandler(validarUsuario),
    asyncHandler(validarAdmin),
    asyncHandler(crearEquipo)
  );
