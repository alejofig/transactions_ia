prompt = """
Dame un objeto json con los valores de la transacción. No uses caracteres especiales y convierte el numero a numerico. Agrega un campo que sea la categoría según el lugar de la compra. Que todas las llaves queden en minuscula y sin espacio
Los keys deben ser:
{
  "fecha": ,
  "hora": ,
  "valor_transaccion":,
  "clase_movimiento": ,
  "lugar_transaccion": ,
  "categoria": ,
  "tarjeta":,
  "banco":,
}
El formato de fecha debe ser yyyy-mm-dd
Solo dame el JSON
"""