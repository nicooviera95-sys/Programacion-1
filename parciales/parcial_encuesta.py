class RespuestaEncuesta:
    def __init__(self,nombre,edad,ciudad,satisfaccion) -> None:
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad
        self.satisfaccion = satisfaccion

class LineaMalFormadaException(Exception):
    pass

class NumeroFueraDeRangoException(Exception):
    pass

class Encuesta:
    def __init__(self):
        self.respuestas = []

    def cargar_respuestas(self, archivo):
        try:
            with open(archivo, 'r') as lineas:
                next(lineas)
                for lin in lineas:
                    try:
                        datos = lin.strip().split(',')

                        if len(datos) != 4:
                            raise LineaMalFormadaException()

                        nombre = datos[0]
                        edad = int(datos[1])
                        ciudad = datos[2]
                        satisfaccion = int(datos[3])

                        if not 1 <= satisfaccion <= 10:
                            raise NumeroFueraDeRangoException()

                        respuesta = RespuestaEncuesta(nombre, edad, ciudad, satisfaccion)

                        self.respuestas.append(respuesta)

                    except LineaMalFormadaException:
                        print('Error de linea mal formada')

                    except ValueError:
                        print('Error de formato numerico en la linea')

                    except NumeroFueraDeRangoException:
                        print('Error nivel de satisfaccion fuera de rango')

        except FileNotFoundError:
            print('No existe el archivo')


    def respuestas_por_ciudad(self) -> dict[str, list[RespuestaEncuesta]]:
        ciudades = {}
        for ciu in self.respuestas:
            ciudades.setdefault(ciu.ciudad, []).append(ciu)
        return ciudades

    def promedio_satisfaccion_por_ciudad(self) -> dict[str, float]:
        promedios = {}
        ciudades = self.respuestas_por_ciudad()

        for ciudad, respuestas in ciudades.items():
            total = sum(r.satisfaccion for r in respuestas)
            promedios[ciudad] = total / len(respuestas)

        return promedios

    def guardar_promedios(self, archivo_salida):
        promedios = self.promedio_satisfaccion_por_ciudad()

        try:
            with open(archivo_salida, 'w') as f:
                for ciudad, promedio in promedios.items():
                    f.write(f"{ciudad}: {promedio:.2f}\n")

        except Exception as e:
            print("Error al guardar el archivo:", e)