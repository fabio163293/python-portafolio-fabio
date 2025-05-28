set_usuarios = {'fabio', 'ramon', 'antonio'}

def acceder():
    while True:
       usuario = input("Por favor ingrese su nombre de acceso: ")
       if usuario.lower() in set_usuarios:
          print("bienvenido")
          break
       else:
         print("El usuario no se encuentra registrado: ")
         registrar()


def registrar():
   while True:
      usuario = (input("por favor indique el nombre de usuario a registrar: "))
      if usuario in set_usuarios:
         print("El nombre esta registrado: ")
         print("intente de nuevo: ")
      else:  
       set_usuarios.add(usuario.lower())

acceder()
