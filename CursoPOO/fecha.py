import calendar

class Fecha:
    # --- Constructor por defecto ---
    def __init__(self, dia=1, mes=1, ano=2000):
        self.set_dia(dia)
        self.set_mes(mes)
        self.set_ano(ano)
        self._mesStr = calendar.month_name[self._mes]  # nombre del mes en inglés

    # --- Getters ---
    def get_dia(self):
        return self._dia

    def get_mes(self):
        return self._mes

    def get_ano(self):
        return self._ano

    def get_mesStr(self):
        return self._mesStr

    # --- Setters ---
    def set_dia(self, dia):
        if 1 <= dia <= 31:
            self._dia = dia
        else:
            raise ValueError("El día debe estar entre 1 y 31")

    def set_mes(self, mes):
        if 1 <= mes <= 12:
            self._mes = mes
            self._mesStr = calendar.month_name[mes]
        else:
            raise ValueError("El mes debe estar entre 1 y 12")

    def set_ano(self, ano):
        if ano > 0:
            self._ano = ano
        else:
            raise ValueError("El año debe ser positivo")

    # --- toString ---
    def __str__(self):
        return f"{self._dia:02d} / {self._mes:02d} / {self._ano} ({self._mesStr})"

    # --- aJuliana ---
    def aJuliana(self):
        """
        Convierte la fecha gregoriana a fecha juliana representada como
        (número de día del año, año)
        Ej: 1 feb 2001 -> (32, 2001)
        """
        ordinal = sum(calendar.monthrange(self._ano, m)[1] for m in range(1, self._mes)) + self._dia
        return (ordinal, self._ano)


# -------- Ejemplo de uso --------
if __name__ == "__main__":
    f1 = Fecha()  # constructor por defecto
    print("Fecha por defecto:", f1)

    f2 = Fecha(1, 2, 2001)  # 1 de febrero de 2001
    print("Fecha:", f2)
    print("aJuliana:", f2.aJuliana())  # (32, 2001)

    f3 = Fecha(1, 1, 2001)  # 1 de enero de 2001
    print("Fecha:", f3)
    print("aJuliana:", f3.aJuliana())  # (1, 2001)
