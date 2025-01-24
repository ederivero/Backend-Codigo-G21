const tbody = document.getElementById("table-body");
const crear = document.getElementById("btn-crear-producto");
const BACKEN_URL =
  "http://catalogo-nodejs-eduardo-env.eba-9kbbzyvk.us-west-2.elasticbeanstalk.com";
// TU URL

fetch(`${BACKEN_URL}/productos`)
  .then((r) => r.json())
  .then(({ content }) => {
    console.log(content);
    for (const producto of content) {
      const fila = document.createElement("tr");
      fila.innerHTML = `<td>${producto.id}</td><td>${producto.nombre}</td><td>${producto.precio}</td>`;
      tbody.appendChild(fila);
    }
  });

crear.addEventListener("click", (e) => {
  e.preventDefault();
  fetch(`${BACKEN_URL}/productos`, {
    method: "POST",
    body: JSON.stringify({
      nombre: "Producto",
      precio: 10.2,
    }),
    headers: {
      "Content-Type": "application/json",
    },
  })
    .then((r) => r.json())
    .then((resultado) => {
      alert(resultado.message);
    });
});
