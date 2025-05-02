#Crear clase 'libro'
#Creater class 'book'

class Libro:
    def __init__(self, titulo, autor, epoca, estado ):
        self.titulo = titulo
        self.autor = autor
        self.epoca = epoca
        if not isinstance(estado, bool):
            raise("El atributo solo puede ser booleano")
        self._estado = estado
    

    def get_estado(self):
        return self._estado
    
    #Método que muestra la informacion del libro
    #Method that displays the book information
    def mostrar_libro(self):
        print(f"el libro {self.titulo} fue escrito por {self.autor} el año {self.epoca}")
        if self._estado is True:
           print("El libro no esta disponible")
        else:
            print("el libro esta dispnible") 
    
    #Método para cambiar el estado del libro a True
    #Method to change the book status to True
    def prestar_libro(self):
        if self._estado is True:
            print("El libro no se puede prestar ya que se encuentra prestado ")
        else:
            self._estado = True
            print("El libro a sido prestado con exito")
        self.mostrar_libro()    

    #Método para cambiar el estado del libro a False
    #Method to change the book status to False
    def devolver_libro(self):
        if self._estado is True:
            self._estado = False
            print("El libro fue devuelto con exito")
        else:            
            print("El libro no esta prestado para ser devuelto")
        self.mostrar_libro()

    #vuelve a formato diccionario un objeto libro
    #Convert a book object back to dictionary format 
    def  a_diccionario(self):
         return { "titulo":self.titulo,
            "autor":self.autor,
            "epoca":self.epoca,
            "estado":self._estado 
             
         }

    #conbierte diccionario a objeto libro
    #Convert dictionary to book object
    @classmethod
    def desde_diccionario(cls, data):
       return cls(data["titulo"], data["autor"], data["epoca"],data["estado"])
    
