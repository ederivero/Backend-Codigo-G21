const BASE_URL = "http://127.0.0.1:5000";
const contenedor = document.getElementById("contenedor");

const queryParams = new URLSearchParams(window.location.search);
let valorPassword1 = "";
let valorPassword2 = "";

if (!queryParams.get("token")) {
  const parrafo = document.createElement("p");
  parrafo.innerText = "La token es invalida o no existe";
  contenedor.appendChild(parrafo);
} else {
  fetch(`${BASE_URL}/validar-token`, {
    method: "POST",
    body: JSON.stringify({ token: queryParams.get("token") }),
    headers: {
      "Content-Type": "application/json",
    },
  })
    .then((respuesta) => {
      return respuesta.json();
    })
    .then((contenido) => {
      console.log(contenido);
      const div = document.createElement("div");
      div.innerHTML = `<form>
  <div class="mb-3">
    <label for="password1" class="form-label">Nueva contraseña</label>
    <input type="password" class="form-control" id="password1">
  </div>
  <div class="mb-3">
    <label for="password2" class="form-label">Repita su contraseña</label>
    <input type="password" class="form-control" id="password2">
  </div>
  <button type="submit" class="btn btn-primary" id="change-password">Cambiar password</button>
</form>`;
      contenedor.appendChild(div);
      const changePwd = document.getElementById("change-password");
      changePwd.addEventListener("click", eventoCambiarPassword);

      const password1 = document.getElementById("password1");
      password1.addEventListener("change", cambioValorPassword1);
      const password2 = document.getElementById("password2");
      password2.addEventListener("change", cambioValorPassword2);
    })
    .catch((error) => {
      console.error(error);
    });
}

const cambioValorPassword1 = (e) => {
  valorPassword1 = e.target.value;
};

const cambioValorPassword2 = (e) => {
  valorPassword2 = e.target.value;
};
const eventoCambiarPassword = (e) => {
  e.preventDefault();
  if (valorPassword1 != valorPassword2) {
    Swal.fire({
      title: "Contraseñas invalidas!",
      text: "Las contraseñas que ingresaste no coinciden",
      icon: "error",
      confirmButtonText: "Entendido",
    });
  } else {
    fetch(`${BASE_URL}/reset-password`, {
      method: "POST",
      body: JSON.stringify({
        token: queryParams.get("token"),
        password: valorPassword1,
      }),
      headers: { "Content-Type": "application/json" },
    })
      .then((respuesta) => {
        return respuesta.json();
      })
      .then((resultado) => {
        console.log(resultado);
        Swal.fire({
          title: "Contraseña actualizada exitosamente",
          text: "Tu contraseña ha sido modificada exitosamente",
          icon: "success",
          confirmButtonText: "Entendido",
        }).then(() => {
          // Cambiamos el endpoint de nuestra pagina y le ponemos el login
          window.location.pathname = "/frontend/login";
        });
      })
      .catch((error) => {
        Swal.fire({
          title: "Error al actualizar la contraseña",
          text: "Hubo un error al actualizar la contraseña, intentelo nuevamente",
          icon: "error",
          confirmButtonText: "Entendido",
        });
      });
  }
};
