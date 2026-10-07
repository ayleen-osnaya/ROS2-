# **APUNTE 1: ROS 2**
[Ver video en YouTube](https://www.youtube.com/watch?v=dN0HZVCUmA0&t=12s)

**Atajos:**

* Copiar: `ctrl + shift + C`  
* Pegar: `ctrl + shift + V`  
* Autocompletar: `tab`  
* Regresar a un comando: `↑` `↓`

**Recomendación:** Tener Terminator

**ROS2 es un middleware:** puente de comunicación entre aplicaciones. (Hardware ↔ ROS2 ↔ Software)

Esquema: ROS2 \> Workspaces \> PKG \> Nodos

1. ROS2  
2. **Workspaces:** carpeta de trabajo (todos tus PKG)  
3. **Paquetes:** agrupa nodos, librerías, config, etc.  
4. **Nodos:** proceso individual que ejecuta 1 tarea (leer sensor, mover motor); se comunica con tópicos, servicios o acciones.

**Síncrono / Asíncrono**

* **S:** Espera una respuesta. El nodo pide y se detiene hasta recibir.  
* **A:** No espera una respuesta. El nodo sigue publicando/recibiendo sin esperar respuesta.

**Tópicos:** Asíncrono. Flujo de datos de 1 solo sentido. De muchos a muchos.  
 Un nodo publica datos (lectura de sensor) y otro nodo se suscribe para recibirlos.

**Publicadores y Suscriptores**

* Un nodo publicador escribe datos en un tópico.  
* Uno o varios nodos suscriptores lo escuchan.  
* El tópico es el canal.

**Servicios:** Síncrono. Un nodo pide algo y un nodo servidor responde 1 vez.

**Acciones:** Feedback continuo. (Ej: motores)  
 3 partes: **Goal** (dónde queremos llegar), **Feedback** (dónde estamos), **Result** (a dónde llegamos).

---

**Workspaces:** `build` · `install` · `log` · `src`

* **src:** Source. Códigos que programo / instrucciones / tiene los pkg. Al compilar src se generan build, install y log.  
* **build:** compila los pkg de source.  
* **install:** son los archivos ya compilados (todo lo que ocupa para ejecutar).  
* **log:** guarda los registros (se compiló, errores, warnings).

---

**TERMINAL**

`Usuario @ ubicación : ~ $`

* Usuario: el usuario  
* @ ubicación: se encuentra en / dirección IP  
* `:` dirección dentro de la compu  
* `~` alias de Linux de carpeta "Home"  
* `$` a partir de aquí son comandos

**¿Cómo cambiamos de dirección?**  
 `cd` \= change directory. Ej: `cd`

* Si solo llamamos a `cd` sin poner un parámetro, nos lleva a Home.  
* Si ponemos `cd -` nos lleva a la última dirección.

**HELP**  
 Cuando no nos acordamos de los parámetros que requiere un comando, llamamos a `--help`. Ej:  
 `cd --help ; cd: cd [-L|[-P [-e]] [-@]] [dir]`

* Corchete \= parámetro opcional `[ ]`  
* Nada \= parámetro obligatorio

**¿Cómo puedo conocer mis direcciones?**  
 `ls` \= list. Enlista los contenidos del directorio donde te encuentras.

* Normalmente las carpetas están en **negritas** y los archivos en texto normal.  
* También podemos ver el contenido de una carpeta sin cambiar de dir con `ls nombreCarpeta/`

```sh
ls
```

**¿Cómo crear un archivo?**  
 `touch` 

Ej: `touch nombre.extensión`

```sh
touch nombre.extensión
```

 Se genera en el directorio donde te encuentras.

**¿Cómo crear una carpeta?**  
 `mkdir` \= make directory. 

Ej: `mkdir nombreCarpeta`

```sh
mkdir nombreCarpeta
```

 Se genera en el directorio donde te encuentras.

**¿Cómo encontrar un ejecutable?**  
 `ros2 pkg executables nombreDelPkg`

```sh
ros2 pkg executables nombreDelPkg
```

**¿Cómo buscar un PKG específico?**  
 `ros2 pkg list | grep nombre`  
 (`|` \= concatenador)

```sh
ros2 pkg list | grep nombre
```

**¿Cómo correr un ejecutable?**  
 `ros2 run nombrePkg nombreEjecutable`

```sh
ros2 run nombrePkg nombreEjecutable
```

 **¿Cómo ver todos los PKG que tengo?**  
 `ros2 pkg list`

```sh
ros2 pkg list
```

 **¿Cómo ver mis nodos?**  
 `ros2 node list`

```sh
ros2 node list
```

**¿Cómo iniciar a mi tortuga?**  
 `ros2 run turtlesim turtlesim_node`

```sh
ros2 run turtlesim turtlesim_node
```

 **Interfaces**
 [Ver video en YouTube](https://www.youtube.com/watch?v=puPAFd_jRF4&t=1s)

**Interfaces:** el formato o molde que ocupan los msg, srv y Action.

* **msg:** Message / Tópicos. Los datos que debe llevar el mensaje.  
   Ej: `geometry_msgs/Twist` ocupa velocidad lineal y angular.  
* **srv:** Service. Define lo que se pide y lo que se responde.  
   Ej: suma estos números (request); el resultado es 8 (response).  
* **action:** Define: Goal, Feedback y Result.

**¿Por qué importan?**  
 Para que un publicador y un suscriptor (o un cliente y un servidor) se puedan entender, ambos deben usar la misma interfaz. Es como si publicador y suscriptor hablaran el mismo "idioma" de datos: si uno manda un Twist y el otro espera un String, no se van a entender.  
 Comandos útiles:

* `ros2 interface list` → ver todas las interfaces disponibles  
* `ros2 interface show <nombre>` → ver la estructura de una interfaz específica  
   Ejemplo: `ros2 interface show geometry_msgs/msg/Twist` te muestra exactamente qué campos tiene ese mensaje.

---

**TÓPICOS**

**¿Cómo ver los tópicos?**  
 `ros2 topic list`

```sh
ros2 topic list
```

 **¿Cómo escuchar un tópico?**  
 `ros2 topic echo nombreTopico`

```sh
 ros2 topic echo nombreTopico
```

 **¿Cómo escuchar un tópico 1 vez?**  
 `ros2 topic echo nombreTopico --once`

```sh
ros2 topic echo nombreTopico --once
```

 **¿Cómo ver la info de un nodo?**  
 `ros2 node info nombreNodo`

```sh
ros2 node info nombreNodo
```

 **¿Cómo veo la info de un tópico específico?**  
 `ros2 topic info nombreTopico`  
 Ej: `ros2 topic info /turtle1/pose`

* Type: `turtlesim/msg/Pose` ← tipo de interfaz (Pose)  
* Publisher: 1 ← alguien publica  
* Subscription: 0 ← nadie escucha

```sh
ros2 topic info nombreTopico
```

 **¿Con qué tópico muevo mi tortuga?**  
 `turtle1/cmd_vel`

```sh
turtle1/cmd_vel
```

 **¿Cómo enviar un mensaje a un tópico?**  
 `ros2 topic pub nombreTopico tipoMensaje`  
 (Esto se hace para ver cómo mandar el mensaje que se requiere.)

```sh
ros2 topic pub nombreTopico tipoMensaje
```

 **¿Cómo mover mi tortuga desde tópicos?**  
 Primero necesito ver la interfaz del tópico:  
 `ros2 interface show geometry_msgs/msg/Twist`

```sh
ros2 interface show geometry_msgs/msg/Twist
```

 Lo que veremos será:

```
Vector3 linear
    Float64 x
    Float64 y
    Float64 z
Vector3 angular
    Float64 x
    Float64 y
    Float64 z
```

(La jerarquía se determina por tabulación. Formato: Tipo, nombre. `linear` \= posición, `angular` \= ángulo.)

Por lo tanto, para mover mi tortuga:  
 `ros2 topic pub nombreTopico tipoMensaje '{mensaje}'`

* nombreTopico \= `/turtle1/cmd_vel`  
* tipoMensaje \= `geometry_msgs/msg/Twist`  
* `'{linear: {x: 0.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 0.0}}'`

---

**Pose**  
 Significa posición y orientación.

* Describe dónde está: coordenadas (x, y, z)  
* Dónde se orienta: cuaterniones

**Twist**  
 Qué tan rápido se mueve algo.

* linear: vel. de desplazamiento  
* angular: vel. de rotación

---

**SERVICIOS**

**¿Cómo llamar un servicio?**  
 `ros2 service call nombreServicio tipoServicio`

```sh
ros2 service call nombreServicio tipoServicio
```

**¿Cómo puedo saber mi tipo de servicio?**  
 `ros2 service info nombreServicio`

```sh
 ros2 service info nombreServicio
```

**¿Cómo saber qué tipo de mensaje enviar a mi servicio?**  
 `ros2 interface show nombreTipoServicio`

```sh
ros2 interface show nombreTipoServicio
```

---

**¿Cómo podemos teleoperar un nodo específico de tortuga?**  
 `ros2 run turtlesim turtle_teleop_key --ros-args --remap /turtle1/cmd_vel:=/Bollo/cmd_vel` **(?)**

* Cambia el nodo. ¿Qué cambiamos? `turtle1` por la nuestra (mi tortuga, ej: "Bollo" **(?)**).

```sh
ros2 run turtlesim turtle_teleop_key --ros-args --remap /turtle1/cmd_vel:=/Bollo/cmd_vel
```

---

**ACCIONES**

**¿Cómo veo mis acciones disponibles?**  
 `ros2 action list`

* Para ver el tipo de mensaje es igual que service con `info nombreAction`.  
* Para saber cómo mandar el mensaje vemos la interfaz: `interface show`.

```sh
ros2 action list
```

**¿Cómo activo mi acción?**  
 `ros2 action send_goal actionName actionType '{msg}'`

```sh
ros2 action send_goal actionName actionType '{msg}'
```

