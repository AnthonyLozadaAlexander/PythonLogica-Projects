def mostrarLinea():
    print("==============================================================="  )

total = 0.0
mensaje = "n/a"
descuento = 0.0
mostrarLinea()
print("                 Caja Super Mercado")
mostrarLinea()


on = False
while(not on):
    total = float(input("El Total De La Compra Es De: "))

    if(total <= 0):
        print("\nError: Debe Ser Mayor a Cero")
        print("Vuelva a Ingresar El Total\n")
        continue
    else:
        on = True

if(total >= 50 and total <= 100):
    descuento =  (total * 0.10)
    mensaje = "Se aplico un descuento del 10%"
    
elif(total > 100):
    descuento = (total * 0.20)
    mensaje = "Se aplico un descuento del 20%"
    

print(f"Total: {total} $")
print(f"Descuento Aplicable: {descuento}")
