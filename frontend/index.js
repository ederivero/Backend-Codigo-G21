fetch("http://127.0.0.1:3000/login", {
  method: "POST",
  body: JSON.stringify({
    email: "ederiveroman@gmail.com",
    password: "Welcome123!",
  }),
  headers: { "Content-Type": "application/json" },
})
  .then((r) => r.json())
  .then((data) => {
    localStorage.setItem("JWT_TOKEN", data.content);
    // alert(data.message);
    // alert(data.content);
  });

fetch("http://127.0.0.1:3000/usuario", {
  method: "GET",
  headers: {
    Authorization: `Bearer ${localStorage.getItem("JWT_TOKEN")}`,
  },
})
  .then((r) => r.json())
  .then((data) => console.log(data));
