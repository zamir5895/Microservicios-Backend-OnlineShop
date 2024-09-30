const CarritoService = require('../domain/services/CarritoService');
const mongoose = require('mongoose');

class CarritoController{
    //Creamos el carrito
    async createCarrito(req, res){
        try{
            const carrito = CarritoService.createCarrito(req.body);
            res.status(201).json(carrito);
        }catch(err){
            res.status(400).json({message: err.message});
            console.error(err);
        }
    }
    //Obtenemos todos los carritos
    async obtenerTodosLosCarritos(req,res){
        try{
            const carritos = await CarritoService.obtenerTodosLosCarritos();
            res.status(200).json(carritos);
        }catch(err){
            res.status(400).json({message: err.message});
        }
    }
    //Obtenemos un carrito por id
    async obtenerCarritoPorId(req,res){
        try{
            const {id} = req.params;
            const carrito = await CarritoService.obtenerCarritoPorId(id);
            res.status(200).json(carrito);
        }catch(err){
            res.status(400).json({message: err.message});
        }
    }
    //Obtener carritos por usuario
    async obtenerCarritosPorUsuario(req,res){
        try{
            const {usuarioId} = req.params;
            const carritos = await CarritoService.obtenerCarritosPorUsuario(usuarioId);
            res.status(200).json(carritos);
        }catch(err){
            res.status(400).json({message: err.message});
        }
    }
    //Modificar carrito a pagado
    async modificarCarritoPagado(req,res){
        try{
            const {id} = req.params;
            const carrito = await CarritoService.modificarCarritoPagado(id);
            res.status(200).json(carrito);
        }catch(err){
            res.status(400).json({message: err.message});
        }
    }
    //Eliminar carrito
    async eliminarCarrito(req,res){
        try{
            const {id} = req.params;
            await CarritoService.eliminarCarrito(id);
            res.status(204).end();
        }catch(err){
            res.status(400).json({message: err.message});
        }
    }
    //Editar el Id de DetalleCarrito
    async editarDetalleCarrito(req, res) {
        try {
            const { detallesCarritoId } = req.query;
            const { id } = req.params;
    
            // Verifica si el detallesCarritoId es un ObjectId válido
            if (!mongoose.Types.ObjectId.isValid(detallesCarritoId)) {
                return res.status(400).json({ message: "El detallesCarritoId no es un ObjectId válido" });
            }
    
            const carrito = await CarritoService.editarDetalleCarrito(id, detallesCarritoId);
            res.status(200).json(carrito);
        } catch (err) {
            res.status(400).json({ message: err.message });
        }
    }
    
}
module.exports = new CarritoController();