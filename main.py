# Biblioteca:

class Libros:

    def __init__(self, autor, titulo, genero):
        self.autor = autor
        self.titulo = titulo
        self.genero = genero

    def __str__(self):
        return f"Autor: {self.autor}, Titulo: {self.titulo}, Genero: {self.genero}"
    
libro1 = Libros("JR rouwling", "Harry potter y la piedra filosofal", "fantasia \n")
libro2 = Libros("Dan Brown", "El Código Da Vinci", "Ficción, Fábula \n")
libro3 = Libros("Antoine de Saint-Exupéry", "El Principito", "infantil \n")

lista = [libro1, libro2, libro3]

def mostrar_menu_principal():
    print("-----------------------------")
    print("-    Elija una opción       -")
    print("-   1: listar libros        -")
    print("-   2: recomendar un libro  -")
    print("-   3: salir...             -")
    print("-----------------------------")

def Biblioteca():
        mostrar_menu_principal()
        while True:
            opcion = int(input("menu de opciones: "))

            if opcion == 1:
                print("lista de libros disponibles")
                for libro in lista:
                    print(libro)

            elif opcion == 2:
                print("qué libro quiere recomendar?")
                autor = input("nombre del autor: ")
                titulo = input("titulo del libro: ")
                genero = input("genero del libro: ")
                libro_nuevo = Libros(autor, titulo, genero)
                lista.append(libro_nuevo)

            elif opcion == 3: 
                print("gracias por usar el programa")
                break
            else: 
                print("opción no válida, por favor elija una opción válida")


            seguir = input("desea seguir usando el programa? (si/no): ").lower()
            if seguir != "si":
                print("hasta luego...")
                break 

usuarios = {}

while True:
  print("-------------------------")
  print("-    Elija una opción   -")
  print("-   1: Registrarse      -")
  print("-   2: Iniciar sesión   -")
  print("-   3: salir...         -")
  print("-------------------------")

  opcion = int(input("elija una opción: "))

  if opcion == 1:
      print("registrese sus datos")
      nombre = input("cuál es su nombre:")
      if nombre in usuarios:
          print("ese nombre ya esta registrado, elija otro.")
      else:
        contraseña = input("ingrese una contraseña: ")
        usuarios[nombre] = contraseña
        print("Usuarios y contraseñas guardados:", usuarios)
        print("registro exitoso \n")

  elif opcion == 2:
      print("iniciar sesión")
      nombre = input("cuál es usuario:")
      contraseña = input("digite su contraseña: ")
      if nombre in usuarios and usuarios[nombre] == contraseña:
        print("inicio de sesión exitoso")
        Biblioteca()
      else: 
        print("Nombre de usuario o contraseña incorrectos \n")

        
  elif opcion == 3:
    print("gracias por usar el programa")
    break
  else:
    print("esa no es una opción válida")