package com.example.microserviciosproductojava.Reseña.Domain;

import com.example.microserviciosproductojava.Producto.Domain.Producto;
import jakarta.persistence.*;
import lombok.Data;

@Data
@Entity
public class Reseña {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;
    private String comentario;
    private Integer calificacion;
    private int usuarioId;
    @ManyToOne
    @JoinColumn(name = "producto_id")
    private Producto producto;
}
