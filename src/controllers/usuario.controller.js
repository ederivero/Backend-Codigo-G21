import { registrarUsuarioSerializer } from "./serializers/usuario.serializer.js";

export const registrarUsuario = async (req, res) => {
  const data = req.body;
  // Valida si la informacion es valida o no
  const dataValidada = registrarUsuarioSerializer.parse(data);
  console.log(dataValidada);

  return res.json({
    message: "Usuario registrado exitosamente",
  });
};
