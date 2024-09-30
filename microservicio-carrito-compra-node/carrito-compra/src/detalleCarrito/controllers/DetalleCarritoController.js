const DetalleCarritoService = require('../domain/services/DetalleCarritoService');
const mongoose = require('mongoose');

class DetalleCarritoController{
    async crearDetalleCarrito(req, res){
        try{
            const detalleCarrito = await DetalleCarritoService.crearDetalleCarrito(req.body);
            res.status(201).json(detalleCarrito);
        }
        catch(err){
            res.status(400).json({message: err.message});
            console.error(err);
        }
    }
    async agregarProducto(req, res){
        try{
            const {id} = req.params;
            const producto = req.body;
            const detalleCarrito = await DetalleCarritoService.agregarProducto(id, producto);
            res.status(200).json(detalleCarrito);
        }catch(err){
            res.status(400).json({message: err.message});
        }
    }
    async obtenerTodosLosDetallesCarrito(req,res){
        try{
            const detallesCarrito = await DetalleCarritoService.obtenerTodosLosDetallesCarrito();
            res.status(200).json(detallesCarrito);
        }catch(error){
            res.status(400).json({message: error.message});
        }
    }
    async obtenerDetalleCarritoPorId(req,res){
        try{
            const {id} = req.params;
            const detalleCarrito = await DetalleCarritoService.obtenerDetalleCarritoPorId(id);
            res.status(200).json(detalleCarrito);
        }catch(error){
            res.status(400).json({message: error.message});
        }
    }

    async eliminarProducto(req,res){
        try{
            const {id} = req.params;
            const {productoid} = req.params;
            const detalleCarrito = await DetalleCarritoService.eliminarProducto(id, productoid);
            res.status(200).json(detalleCarrito);
        }catch(error){
            res.status(400).json({message: error.message});
        }
    }
    async eliminarDetalleCarrito(req,res){
        try{
            const {id} = req.params;
            await DetalleCarritoService.eliminarDetalleCarrito(id);
            res.status(204).end();
        }catch(error){
            res.status(400).json({message: error.message});
        }
    }

    async editarCantidadProducto(req,res){
        try{
            const {id} = req.params;
            const {productoid} = req.params;
            const {cantidad} = req.body;
            const detalleCarrito = await DetalleCarritoService.editarCantidadProducto(id, productoid, cantidad);
            res.status(200).json(detalleCarrito);
        }catch(error){
            res.status(400).json({message: error.message});
        }
    }
    async obtenerProductoByDetalleCarritoIdAndProductoId(req,res){
        try{
            const {id} = req.params;
            const {productoid} = req.params;
            const detalleCarrito = await DetalleCarritoService.obtenerProductoByDetalleCarritoIdAndProductoId(id, productoid);
            res.status(200).json(detalleCarrito);
        }catch(error){
            res.status(400).json({message: error.message});
        }
    }

}
module.exports = new DetalleCarritoController();