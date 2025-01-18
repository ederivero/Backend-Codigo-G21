import express from "express";
import { generarURLFirmada } from "../controllers/imagen.controller.js";
import asyncHandler from "express-async-handler";

export const imagenEnrutador = express.Router();

imagenEnrutador.post("/generar-url", asyncHandler(generarURLFirmada));
