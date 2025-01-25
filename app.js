process.env['NODE_TLS_REJECT_UNAUTHORIZED'] = 0
const express = require('express')
const pg = require('pg')
const cors = require('cors')

const app = express()
app.use(express.json())
// Definiendo los cors
app.use(
  cors({
    methods: ['GET', 'POST'], // '*'
    origin: '*', //["http://mifrontend.com", "http://localhost:8080"], // '*'
    allowedHeaders: ['Authorization', 'Content-Type', 'Accept'], // '*'
  })
)

app.route('/').get((req, res) => {
  return res.json({
    content: process.env,
    message: 'Bienvenido a mi API',
  })
})

const conexion = new pg.Pool({
  // connectionString: `pg://${process.env.RDS_USERNAME}:${process.env.RDS_PASSWORD}@${process.env.RDS_HOSTNAME}:${process.env.RDS_PORT}/${process.env.RDS_DB_NAME}`,
  host: process.env.RDS_HOSTNAME,
  port: process.env.RDS_PORT,
  database: process.env.RDS_DB_NAME,
  user: process.env.RDS_USERNAME,
  password: process.env.RDS_PASSWORD,
  ssl: true,
})

app
  .route('/productos')
  .get(async (req, res) => {
    const result = await conexion.query('SELECT * FROM productos')
    const registros = result.rows

    return res.json({
      content: registros,
    })
  })
  .post(async (req, res) => {
    const data = req.body
    const nuevoProducto = await conexion.query('INSERT INTO productos (nombre, precio) VALUES ($1,$2) RETURNING *', [
      data.nombre,
      data.precio,
    ])

    const resultado = nuevoProducto.rows

    return res.json({
      message: 'Producto creado exitosamente',
      content: resultado,
    })
  })

app.listen(process.env.PORT, () => {
  console.log(`Servidor corriendo en el puerto ${process.env.PORT}`)

  Promise.all([
    conexion.query('CREATE TABLE IF NOT EXISTS productos (id SERIAL PRIMARY KEY, nombre TEXT, precio FLOAT)'),
  ]).then(() => {
    console.log('Las tablas fueron creadas exitosamente')
  })
})
