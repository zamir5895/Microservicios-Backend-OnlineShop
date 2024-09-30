require('dotenv').config();
const express = require('express');
const mongoose = require('mongoose'); // Agregar mongoose
const app = express();
const CarritoController = require('./src/carrito/controllers/CarritoController');

app.use(express.json()); // express.json() ya maneja el body parsing

// Definir rutas de carrito
app.post('/api/carrito/postear', CarritoController.createCarrito);
app.get('/api/carrito/all', CarritoController.obtenerTodosLosCarritos);
app.get('/api/carrito/:id', CarritoController.obtenerCarritoPorId);
app.get('/api/carrito/usuario/:usuarioId', CarritoController.obtenerCarritosPorUsuario);
app.put('/api/carrito/pagado/:id', CarritoController.modificarCarritoPagado);
app.delete('/api/carrito/:id', CarritoController.eliminarCarrito);
app.put('/api/carrito/detalles/:id', CarritoController.editarDetalleCarrito);

// Conexión a MongoDB sin opciones deprecadas
mongoose.connect(process.env.MONGO_URI)
  .then(() => {
    console.log('Conectado a MongoDB');
  })
  .catch(err => {
    console.error('Error al conectarse a MongoDB:', err.message);
  });

const port = process.env.PORT || 3000;
app.listen(port, () => {
    console.log(`Server running on port ${port}`);
});
