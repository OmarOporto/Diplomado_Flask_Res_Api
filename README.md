El proyecto puede realizar:

POST /usuarios/add                  ==> PARA PODER AGREGAR USUARIOS.....:
{
    "name": "poner nombre"
    "age": "INTEGER"
    "id": "12312312de-123123" ## numeros al azaar con letras max 4 separaciones
}

GET /usuarios/                      ==> MOSTRARA TODOS LOS USUARIOS

GET /usuarios/edad-promedio/        ==> MOSTRARA LA EDAD PROMEDIO

GET /usuarios/status/               ==> MOSTRARA LA INFORMACION DE STATUS SOLICITADA

DELETE /usuarios/delete/<id>        ==> SE DEBE COLOCAR EL ID DESEADO A ELIMINAR AL FINAL

PUT /usuarios/update/<id>           ==> PARA EL UPDATE SE DEBE COLOCAR EL ID DESEADO Y ENVIAR:


{
    "name": "poner nombre"
    "age": "INTEGER"
}