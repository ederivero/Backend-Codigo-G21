import express from "express";
import {
  registrarUsuario,
  login,
  actualizarUsuario,
  devolverUsuario,
} from "../controllers/usuario.controller.js";
import asyncHandler from "express-async-handler";
import { validarUsuario } from "../middlewares.js";

export const usuarioEnrutador = express.Router();

// Agregamos todas las rutas relacionadas al usuario
// asyncHandler > captura el controlador asincrono y lo espera para que si, tiene algun error lo podamos manejar en nuestro error handler
usuarioEnrutador.post("/registro", asyncHandler(registrarUsuario));
usuarioEnrutador.post("/login", asyncHandler(login));
usuarioEnrutador.put(
  "/actualizar-usuario",
  asyncHandler(validarUsuario),
  asyncHandler(actualizarUsuario)
);
usuarioEnrutador.get(
  "/usuario",
  asyncHandler(validarUsuario),
  asyncHandler(devolverUsuario)
);
