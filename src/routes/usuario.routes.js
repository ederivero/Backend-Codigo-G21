import express from "express";
import { registrarUsuario } from "../controllers/usuario.controller.js";

export const usuarioEnrutador = express.Router();

// Agregamos todas las rutas relacionadas al usuario
usuarioEnrutador.post("/registro", registrarUsuario);
