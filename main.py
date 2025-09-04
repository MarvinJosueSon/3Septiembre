import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi primera ventana")
ventana.geometry("800x400")

etiqueta = tk.Label(ventana, text="Ingresa el primer numero:")
etiqueta.pack(pady=5)
entrada = tk.Entry(ventana)
entrada.pack(pady=5)

etiquetaDos= tk.Label(ventana, text="Ingresa el segundo numero:")
etiquetaDos.pack(pady=5)
entradaDos = tk.Entry(ventana)
entradaDos.pack(pady=5)

etiquetaTres= tk.Label(ventana, text="Resultado:")
etiquetaTres.pack(pady=5)




def suma():
    num1 = float(entrada.get())
    num2 = float(entradaDos.get())
    return num1 + num2
def resta():
    num1 = float(entrada.get())
    num2 = float(entradaDos.get())
    return num1-num2
def multiplicacion():
    num1 = float(entrada.get())
    num2 = float(entradaDos.get())
    return num1*num2
def division():
    num1 = float(entrada.get())
    num2 = float(entradaDos.get())
    if num2==0:
        etiquetaTres.config(text="ERROR NO SE PUEDE DIVIDIR EN 0")
    return num1/num2

def Sumar():
    resultado=suma()
    etiquetaTres.config(text=f"Resultado: {resultado}")
def Restar():
    resultado = resta()
    etiquetaTres.config(text=f"Resultado: {resultado}")
def Multiplicacion():
    resultado = multiplicacion()
    etiquetaTres.config(text=f"Resultado: {resultado}")
def Division():
    resultado = division()
    etiquetaTres.config(text=f"Resultado: {resultado}")



def limpiar():
    entrada.delete(0, tk.END)
    entradaDos.delete(0, tk.END)
    etiquetaTres.config(text="Resultado:")

botonsumar = tk.Button(ventana, text="SUMA", command=Sumar)
botonsumar.pack(pady=5)
botonresta = tk.Button(ventana, text="RESTA", command=Restar)
botonresta.pack(pady=5)
botonmultiplicacion = tk.Button(ventana, text="MULTIPLICACION", command=Multiplicacion)
botonmultiplicacion.pack(pady=5)
botondivision = tk.Button(ventana, text="DIVISION", command=Division)
botondivision.pack(pady=5)



boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar)
boton_limpiar.pack(pady=5)

boton_salir = tk.Button(ventana, text="Salir", command=ventana.quit)
boton_salir.pack(pady=5)

ventana.mainloop()