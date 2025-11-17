class Cancion:
    def __init__(self, titulo, artista, duracion_minuto, reproducciones, genero) -> None:
        self.titulo = titulo
        self.artista = artista
        self.duracion_minuto = float(duracion_minuto)
        self.reproducciones = int(reproducciones)
        self.genero = genero

    def __str__(self):
        return f"{self.titulo} - {self.artista} ({self.duracion_minuto} min, {self.reproducciones} reproducciones)"

    def es_popular(self) -> bool:
        return self.reproducciones > 5000000


class LineaMalFormadaException(Exception):
    pass


class Playlist:
    def __init__(self):
        self.canciones = []

    def cargar_playlist(self, archivo):
        try:
            with open(archivo, 'r') as lineas:
                next(lineas)
                for lin in lineas:
                    try:
                        datos = lin.strip().split(',')

                        if len(datos) != 5:
                            raise LineaMalFormadaException()

                        titulo, artista, duracion_minuto, reproducciones, genero = datos

                        cancion = Cancion(titulo, artista, duracion_minuto, reproducciones, genero)

                        self.canciones.append(cancion)

                    except LineaMalFormadaException:
                        print("Error!!")
                    except ValueError:
                        print("No es un numero")
        except FileNotFoundError:
            print("Archivo no encontrado")

    def canciones_por_genero(self) -> dict[str, list[Cancion]]:
        generos = {}
        for cancion in self.canciones:
            generos.setdefault(cancion.genero, []).append(cancion)
        return generos