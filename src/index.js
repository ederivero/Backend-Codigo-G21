import express from 'express'
import mongoose from 'mongoose'

const servidor = express()
servidor.use(express.json())

// Si usamos un contenedor en una aplicacion entonces debemos inidicar el nombre del contenedor y no la ip ya que no esta dentro de un proceso local
// Sucede cuando el proyecto esta dentro del mismo contenedor de la base de datos
mongoose
  .connect('mongodb://usuario:root@127.0.0.1:27017/pruebas?authSource=admin')
  .then(() => {
    console.log('Base de datos conectada exitosamente')
  })
  .catch((e) => {
    console.error('Error al conectarse a la base de datos')
    console.log(e)
  })

const ProductoModel = mongoose.model('productos', {
  nombre: mongoose.Schema.Types.String,
  precio: {
    type: mongoose.Schema.Types.Decimal128,
    min: 0,
    max: 100,
    required: true,
  },
})

servidor.route('/productos').post(async (req, res) => {
  // TODO: agregar validacion con ZOD
  const data = req.body
  const nuevoProducto = new ProductoModel({ nombre: data.nombre, precio: data.precio }) // new ProductoModel(data)
  // OTRA FORMA DE CREAR
  // const nuevoProducto = await ProductoModel.create(data)
  // Usando el segundo metodo no es necesario mandar a llamar al metodo save ya que este lo crea defrente

  // Este metodo crea mas de un registro en la tabla
  // await ProductoModel.insertMany([])

  // Crea el nuevo registro en la base de datos
  const resultado = await nuevoProducto.save()
  // Convierte la informacion a un JSON legible
  resultado.toJSON()

  return res.json({
    message: 'Producto creado exitosamente',
    content: resultado.toJSON(),
  })
})

servidor.listen(process.env.PORT, () => {
  console.log(`Servidor corriendo exitosamente en el puerto ${process.env.PORT}`)
})
