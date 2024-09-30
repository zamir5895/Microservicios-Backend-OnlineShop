package com.example.microserviciosproductojava.Categoria.Application;

import com.example.microserviciosproductojava.Categoria.DTOS.RequestCategoria;
import com.example.microserviciosproductojava.Categoria.DTOS.ResponseCategoriaDto;
import com.example.microserviciosproductojava.Categoria.Domain.CategoriaService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/categoria")
public class CategoriaController {
    @Autowired
    private CategoriaService categoriaService;

    @PostMapping("/postear")
    public ResponseEntity<Void> publicarCategoria(@RequestBody RequestCategoria requestCategoria) {
        categoriaService.publicarCategoria(requestCategoria);
        return ResponseEntity.ok().build();
    }
    @PatchMapping
    public ResponseEntity<Void> actualizarCategoria(@RequestParam Integer id, @RequestBody RequestCategoria requestCategoria) {
        categoriaService.actualizarCategoria(id, requestCategoria);
        return ResponseEntity.ok().build();
    }
    @DeleteMapping("/{id}")
    public ResponseEntity<Void> eliminarCategoria(@PathVariable Integer id) {
        categoriaService.eliminarCategoria(id);
        return ResponseEntity.ok().build();
    }

    @GetMapping("/{id}")
    public ResponseEntity<ResponseCategoriaDto> obtenerCategoria(@PathVariable Integer id) {
        return ResponseEntity.ok(categoriaService.obtenerCategoria(id));
    }
    @GetMapping("/all")
    public ResponseEntity<Page<ResponseCategoriaDto>> obtenerCategorias(@RequestParam int page, @RequestParam int size) {
        return ResponseEntity.ok(categoriaService.obtenerCategorias(page, size));
    }

    @GetMapping("/nombre")
    public ResponseEntity<Page<ResponseCategoriaDto>> obtenerCategoriasPorNombre(@RequestParam String nombre, @RequestParam int page, @RequestParam int size) {
        return ResponseEntity.ok(categoriaService.obtenerCategoriasPorNombre(nombre, page, size));
    }


}
