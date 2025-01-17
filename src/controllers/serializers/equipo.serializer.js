import { z } from "zod";

export const crearEquipoSerializer = z.object({
  nombre: z.string(),
  estadio: z.string().optional(),
  imagenId: z.number().optional(),
});
