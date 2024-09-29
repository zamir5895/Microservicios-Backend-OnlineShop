package com.example.microserviciosproductojava.Producto.Domain;

import com.example.microserviciosproductojava.Categoria.Domain.Categoria;
import com.example.microserviciosproductojava.Reseña.Domain.Reseña;
import jakarta.persistence.*;
import lombok.Data;

import java.util.List;

@Data
@Entity
public class Producto {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int id;
    private String nombre;
    private Double precio;
    private Integer stock;
    private String descripcion;
    @ManyToOne
    @JoinColumn(name = "categoria_id")
    private Categoria categoria;
    @OneToMany(mappedBy = "producto", cascade = CascadeType.ALL)
    private List<Reseña> reseñas;

}
