### **📘 Consigna**

Se desea modelar un sistema básico de **pedidos en un restaurante**.

1. Crear un `enum` llamado `CategoriaPlato` con las siguientes categorías: `ENTRADA`, `PRINCIPAL`, `POSTRE`, `BEBIDA`.

2. Definir una clase `Plato` que tenga los siguientes atributos privados:

   * `__nombre` (str)

   * `__precio` (float)

   * `__categoria` (CategoriaPlato)  
      Incluye métodos getters y setters controlados (ejemplo: validar que el precio sea positivo).

3. Definir una clase `Pedido` que use **composición** para mantener una lista de platos (`Plato`).

   * Método `agregar_plato(plato: Plato)` para añadir un plato al pedido.

   * Método `calcular_total()` que devuelva la suma de los precios.

   * Método `ticket()` que muestre todos los platos del pedido con su categoría y precio, y el total del ticket. 

4. Probar el sistema creando algunos platos y armando un pedido con varios de ellos.

