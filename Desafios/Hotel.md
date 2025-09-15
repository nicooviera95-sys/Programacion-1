## **📌 Consigna**

Se quiere modelar un sistema básico para gestionar **habitaciones de hotel**.

1. Cada habitación tiene un **número**, un **tipo** (simple, doble, suite) y un **estado** (libre, ocupada, en limpieza).

2. El tipo de habitación debe representarse con un `Enum`.

3. El estado de la habitación también debe representarse con un `Enum`.

4. La clase `Habitacion` debe encapsular sus atributos y permitir acceso controlado mediante **@property y setters**.

   * No se debe permitir asignar un estado inválido.

   * El número de habitación no puede ser negativo.

5. La clase `Hotel` debe administrar un conjunto de habitaciones (**composición**).

   * Permitir agregar habitaciones.

   * Consultar habitaciones libres.

   * Cambiar el estado de una habitación.

