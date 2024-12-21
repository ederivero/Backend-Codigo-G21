const email = document.getElementById("email");
const resetPasswordBtn = document.getElementById("reset-password-btn");
const BACKEND_URL = "http://127.0.0.1:5000";

resetPasswordBtn.addEventListener("click", (e) => {
  e.preventDefault();
  const correo = email.value;

  // Con esto desactivamos el boton para evitar hacer clicks repetitivos
  resetPasswordBtn.disabled = true;

  resetearPassword(correo)
    .then((resultado) => {
      console.log(resultado);
    })
    .catch((e) => {
      console.error(e);
    });
});

const resetearPassword = async (correo) => {
  const body = { correo: correo };
  const resultado = await fetch(`${BACKEND_URL}/forgot-password`, {
    method: "POST",
    body: JSON.stringify(body), // Convertir nuestro json de javascript a un JSON que pueda recibir el backend,
    headers: {
      "Content-Type": "application/json", // Indicar el tipo de informacion que estoy enviando en el body
    },
  });
  const respuesta = await resultado.json();

  return respuesta;
};
