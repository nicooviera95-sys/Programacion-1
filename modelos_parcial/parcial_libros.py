class Libro:
    def __init__(self, titulo, autor, genero, cantidad_disponible) -> None:
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.cantidad_disponible = int(cantidad_disponible)


class LineaMalFormadaException(Exception):
    pass

class CantidadDisponibleException(Exception):
    pass


class GestionBiblioteca:
    def __init__(self) -> None:
        self.libros = []

    def guardar_libros(self, archivo):
        try:
            with open(archivo, 'r') as lineas:
                next(lineas)
                for lin in lineas:
                    try:
                        datos = lin.strip().split(',')

                        if len(datos) != 4:
                            raise LineaMalFormadaException()

                        titulo, autor, genero, cantidad = datos

                        libro = Libro(titulo, autor, genero, cantidad)

                        if libro.cantidad_disponible < 0:
                            raise CantidadDisponibleException()

                        self.libros.append(libro)

                    except LineaMalFormadaException:
                        print("Linea mal formadad")
                    except ValueError:
                        print("Valor no numerico")
                    except CantidadDisponibleException:
                        print("Cantidad invalida")
        except FileNotFoundError:
            print("Archivo no encontrado")


    def ordenar_generos(self) -> dict[str, list[Libro]]:
        dic = {}
        for libro in self.libros:
            dic.setdefault(libro.genero, []).append(libro.titulo)
        return dic


    def autor_con_mas_libros(self):