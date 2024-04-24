users = {"pepe":"123"}

def Registro():
    username = input("Ingrese Nombre de usuario:")
    password = input("Ingrese Una contrasenia:")
    users[username] = password
    print("se guardo con exito")
    

def mostrar_users():
    print(users)


def login(username, password):
    contador = 0
    while (not username in users):
     if(contador < 2):
            print("por favor ingrese de nuevo sus datos")
            username = input("Ingrese Nombre de usuario:")
            password = input("Ingrese Una contrasenia:")
            contador += 1
     else:
            print("hola")
            return False
    else:
     if users[username] != password:
            print("por favor ingrese de nuevo sus datos")
            username = input("Ingrese Nombre de usuario:")
            password = input("Ingrese Una contrasenia:")
            contador += 1  
     else:
      return True    


def Menu():
    opcion = 0
    while (opcion!= 4):
        print("apretar 1: agregar un usuario")
        print("apretar 2: ver usuarios existentes")
        print("apretar 3: login")
        print("apretar 4: Que tenga un buen dia")
        opcion = int(input("ingrese una opcion: "))
        if opcion == 1:
            Registro()
        elif opcion == 2:
            mostrar_users()
        elif opcion == 3:
            username = input("su nombre de usuario:")
            password = input("su una contrasenia:")
            ing_exitoso = login(username, password)
            if not ing_exitoso:
                print("usuario o contrasenia incorrectos")
                break
            else:
                print("ing_exitoso")
                break
        elif opcion == 4:
            print("chau") 
            break           

Menu()
