package com.example.microserviciosproductojava;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

@RestController
@CrossOrigin(origins = "*", allowedHeaders = "*")

public class Controller {

    @GetMapping("/")
    public String welcome() {
        return "Bienvenido al microservicio de Producto";
    }
}
