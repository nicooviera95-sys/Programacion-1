### **🏆 Consigna: *"El Torneo de la Llama — Versión Extrema"***

Los héroes compiten en el **Torneo de la Llama**, donde su poder depende de los **ítems mágicos** que poseen.

---

#### **1\. Héroes**

* Cada héroe tiene:

  * Un **nombre**.  
    Una **lista privada de ítems** (`_items`).

* Métodos:

  * `agregar_item(item)` → suma un ítem.

  * `consumir_item(item)` → quita un ítem.

  * `poder_de_fuego()` → suma de los valores de fuego de sus ítems.

  * `mostrar_items()` → lista legible de los ítems actuales.

---

#### **2\. Items**

* Representados con un **enum** `Item`, donde cada valor es un **poder de fuego**.

  * Ejemplo:

    * `ESPADA = 10`  
      `VARITA = 7`  
      `ARCO = 5`  
      `POCION = 3`

---

#### **3\. Torneo**

* Contiene una **lista de héroes participantes**.

* Métodos:

  * `agregar_heroe(heroe)` → añade un héroe al torneo.

  * `enfrentar(heroe1, heroe2)` → aplica la lógica de combate:

    * Gana el de mayor poder de fuego.

    * Perdedor pierde todos los ítems.

    * Ganador debe descartar ítems hasta que su poder de fuego sea **igual o apenas inferior** al que tenía el oponente antes del combate.

    * Empate → ambos sin ítems.

  * `iniciar()` (opcional) → simula rondas de combate entre todos los héroes hasta que quede uno (o empate final).

  Método `enfrentar(heroe1, heroe2)`:

  * El héroe con **mayor poder de fuego** gana.  
    El perdedor queda con su lista de ítems **vacía**.  
    El ganador **pierde ítems** siguiendo esta lógica:

    * Debe descartar ítems hasta que su poder de fuego sea **igual o apenas inferior** al que tenía el oponente antes del combate.

    * (Ejemplo: si el rival tenía 15 de poder, y el ganador tenía 25, debe quitar ítems hasta gastar por lo menos los 15 del oponente).

  * En caso de **empate**, ambos quedan sin ítems.

---

#### **4\. Simulación** (lo hacemos dentro del torneo, con main o Test Unitarios)

1. Crea al menos 3 héroes con ítems diferentes.

2. Hazlos combatir en rondas.

3. Después de cada combate, imprime el estado de los héroes:  
   * Nombre, poder de fuego actual y lista de ítems.