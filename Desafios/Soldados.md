### **ENCAPSULAMIENTO \+ PRUEBAS UNITARIAS**

### **Consigna: Clase Soldado**

Queremos simular enfrentamientos entre soldados. Para ello, vas a modelar una clase llamada **`Soldado`** con las siguientes características:

#### **Atributos**

* **`nombre`**: un identificador para cada soldado.

* **`energia`**: comienza en 100\.

* **`salud`**: comienza en 200\.

#### **Comportamiento**

1. **Atacar**

   * Un soldado puede atacar a otro si tiene **al menos 10 puntos de energía**.

   * Cada ataque:

     * Consume **10 de energía** al atacante.

     * Infringe **10 de daño** (reduce 10 de salud) al soldado atacado.

   * Si no tiene suficiente energía, el ataque no ocurre.

2. **Recibir ración de agua**

   * Restaura **20 puntos de energía** (sin superar 100).

3. **Estado del soldado**

   * Un método para mostrar la salud y energía actuales.

   * Un soldado queda **derrotado** si su salud llega a 0 o menos.

[soldado.py](https://drive.google.com/file/d/1SKqax3Mxw18k-q3ec6248oRmo8uHy6L1/view?usp=drive_link)  
[soldado\_test.py](https://drive.google.com/file/d/1Um3eCrw67RE8IPjYPrsHaHDq8NPX-lcl/view?usp=sharing)