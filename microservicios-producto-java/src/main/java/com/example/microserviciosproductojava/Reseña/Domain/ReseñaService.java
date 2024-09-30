package com.example.microserviciosproductojava.Reseña.Domain;

import com.example.microserviciosproductojava.Producto.DTOS.ProductoResponseDTO;
import com.example.microserviciosproductojava.Producto.Domain.Producto;
import com.example.microserviciosproductojava.Producto.Infrastructure.ProductoRepository;
import com.example.microserviciosproductojava.Reseña.DTOS.PostReseñadto;
import com.example.microserviciosproductojava.Reseña.DTOS.ResponseReseñadto;
import com.example.microserviciosproductojava.Reseña.Infrastructure.ReseñaRepository;
import lombok.NoArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageImpl;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.stream.Collectors;

@Service
@NoArgsConstructor
public class ReseñaService {
    @Autowired
    private ReseñaRepository reseñaRepository;

    @Autowired
    private ProductoRepository productoRepository;

    public void crearReseña(PostReseñadto post){
        Reseña reseña = new Reseña();
        Producto producto = productoRepository.findById(post.getProductoId()).orElseThrow(()-> new RuntimeException("Producto no encontrado"));
        reseña.setCalificacion(post.getCalificacion());
        reseña.setComentario(post.getComentario());
        reseña.setUsuarioId(post.getUsuarioId());
        reseña.setProducto(producto);
        reseñaRepository.save(reseña);
        producto.getReseñas().add(reseña);
        producto.setCantidadReseñas(producto.getCantidadReseñas() + 1);
        productoRepository.save(producto);
    }
    public Page<ResponseReseñadto> ObtenerReseñasPorProducto(Integer productoId, int page, int size){
        Pageable pageable = PageRequest.of(page, size);
        Page<Reseña> reseñas = reseñaRepository.findAllByProductoId(productoId, pageable);
        List<ResponseReseñadto> responseReseñadtos = reseñas.getContent().stream()
                .map(this::converToDto).collect(Collectors.toList());
        return new PageImpl<>(responseReseñadtos, pageable, reseñas.getTotalElements());
    }

    public ResponseReseñadto ObtenerReseñaPorProducto(Integer productoId, Integer reseñaId){
        Reseña reseña = reseñaRepository.findById(reseñaId).orElseThrow(()-> new RuntimeException("Reseña no encontrada"));
        if(reseña.getProducto().getId() != productoId){
            throw new RuntimeException("Reseña no encontrada");
        }
        return converToDto(reseña);
    }
    public void EliminarReseña(Integer productoId, Integer reseñaId){
        Reseña reseña = reseñaRepository.findById(reseñaId).orElseThrow(()-> new RuntimeException("Reseña no encontrada"));
        if(reseña.getProducto().getId() != productoId){
            throw new RuntimeException("Reseña no encontrada");
        }
        Producto producto = reseña.getProducto();
        producto.getReseñas().remove(reseña);
        producto.setCantidadReseñas(producto.getCantidadReseñas() - 1);
        productoRepository.save(producto);
        reseñaRepository.delete(reseña);
    }
    public Double ObtenerPromedio(Integer productoId){
        double promedio = reseñaRepository.findAllByProductoId(productoId, PageRequest.of(0, Integer.MAX_VALUE))
                .getContent()
                .stream()
                .mapToDouble(Reseña::getCalificacion)
                .average()
                .orElse(0.0);
        return promedio;
    }

    public void ActualizarReseña(Integer productoId, Integer reseñaId, PostReseñadto post){
        Reseña reseña = reseñaRepository.findById(reseñaId).orElseThrow(()-> new RuntimeException("Reseña no encontrada"));
        if(reseña.getProducto().getId() != productoId){
            throw new RuntimeException("Reseña no encontrada");
        }if(post.getCalificacion() != null){
            reseña.setCalificacion(post.getCalificacion());
        }
        if(!post.getComentario().isEmpty()) {
            reseña.setComentario(post.getComentario());
        }
        reseñaRepository.save(reseña);
    }



    private ResponseReseñadto converToDto(Reseña reseña){
        ResponseReseñadto responseReseñadto = new ResponseReseñadto();
        responseReseñadto.setCalificacion(reseña.getCalificacion());
        responseReseñadto.setComentario(reseña.getComentario());
        responseReseñadto.setId(reseña.getId());
        responseReseñadto.setUsuarioId(reseña.getUsuarioId());
        return responseReseñadto;
    }



}
