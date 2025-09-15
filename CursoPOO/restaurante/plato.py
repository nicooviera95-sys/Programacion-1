from categoria_plato import CategoriaPlato

class Plato:
    def __init__(self, nombre: str, precio: float, categoria: CategoriaPlato) -> None:
        self.__nombre = nombre
        self.__precio = precio
        self.__categoria = categoria

    @property
    def nombre(self)->str:
        return self.__nombre
    
    @nombre.setter
    def nombre(self,nuevo_nombre:str):
        self.__nombre = nuevo_nombre
    
    @property
    def precio(self)->float:
        return self.__precio
    
    @precio.setter
    def precio(self,nuevo_precio):
        if nuevo_precio <= 0:
            raise ValueError('Precio incorrecto')
        self.__precio = nuevo_precio
    
    @property
    def categoria(self)->CategoriaPlato:
        return self.__categoria
    
    @categoria.setter
    def categoria(self,nueva_categoria: CategoriaPlato)->None:
        if not isinstance(nueva_categoria, CategoriaPlato):
            raise ValueError("No es una categoría para este plato")
        self.__categoria = nueva_categoria

    def __repr__(self):
        return f"{self.nombre}, ${self.precio}, {self.categoria.name}"