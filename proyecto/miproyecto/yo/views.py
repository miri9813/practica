from django.shortcuts import render, HttpResponse
# Create your views here.
def principal(request):
    contenido = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Mi Perfil</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #e0f7fa;
                color: #007bb5;
            }
            .container {
                max-width: 600px;
                margin: 50px auto;
                padding: 20px;
                background-color: #ffffff;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            }
            h1 {
                color: #004d80;
            }
            .pasatiempos {
                margin: 10px 0;
            }
            
        </style>
    </head>
    <body>

        <div class="container">
            <h1>SOBRE MI</h1>
            <p><strong>Nombre:</strong> Myriam Berenice Garcia Calderon</p>
            <p><strong>Edad:</strong> 25</p>
            <div class="pasatiempos">
                <strong>Mis pasatiempos favoritos:</strong>
                <ul>
                    <li>Escuchar musica </li>
                    <li>Caminar mientras llueve </li>
                    <li>Programar</li>
                    
                </ul>
            </div>
        </div>

    </body>
    </html>
    """
    return HttpResponse(contenido)