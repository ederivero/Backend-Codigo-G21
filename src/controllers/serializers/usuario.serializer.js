import { z } from "zod";
import { TipoUsuario } from "@prisma/client";

// Todos los valores son requeridos por defecto a no ser que coloquemos la propiedad 'optional()'
export const registrarUsuarioSerializer = z.object({
  email: z.string().email(),
  password: z
    .string()
    .regex(
      /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!*&%?])[A-Za-z\d@$!*&%?]{8,}$/
    ),
  tipoUsuario: z.enum([
    TipoUsuario.ADMIN,
    TipoUsuario.MODERADOR,
    TipoUsuario.USUARIO,
  ]),
  nombre: z.string().optional(),
  apellido: z.string().optional(),
});

export const loginSerializer = z.object({
  email: z.string().email(),
  password: z.string(),
});

export const actualizarUsuarioSerializer = z.object({
  nombre: z.string().optional(),
  apellido: z.string().optional(),
});
