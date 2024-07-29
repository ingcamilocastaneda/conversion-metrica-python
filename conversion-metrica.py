#Paso 1. Solicitar al usuario las medidas de la pieza del mueble en cms

medida_en_cms = float(input("Por favor, ingrese las medidas de la pieza del mueble (En cms): "))

#2. Convertir las medidas de centimetros a pulgadas

medida_en_pulgadas = medida_en_cms / 2.54

#3. Mostrar las medidas convertidas en pulgadas al usuario

print("Las medidas en pulgadas de la pieza ingresadas son: ", medida_en_pulgadas)