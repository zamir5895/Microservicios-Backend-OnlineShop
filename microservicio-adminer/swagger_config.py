swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "Administrador API",
        "description": "API para gestionar administradores",
        "version": "1.0.0",
        "contact": {
            "name": "Soporte",
            "url": "http://tu-app-soporte.com"
        }
    },
    "basePath": "/",
    "schemes": [
        "http"
    ]
}

swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'swagger',
            "route": '/swagger.json',
            "rule_filter": lambda rule: True,  
            "model_filter": lambda tag: True,  
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/swagger/"
}
