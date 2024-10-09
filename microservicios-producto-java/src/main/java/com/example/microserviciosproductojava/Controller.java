package com.example.microserviciosproductojava;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@CrossOrigin(origins = "*", allowedHeaders = "*", methods = {RequestMethod.GET, RequestMethod.POST, RequestMethod.PUT, RequestMethod.DELETE})

public class Controller {

    @GetMapping("/")
    public String welcome() {
        return "Bienvenido al microservicio de Producto";
    }
}
