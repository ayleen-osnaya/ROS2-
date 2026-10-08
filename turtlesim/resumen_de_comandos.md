# Resumen para usar turtlesim

Primero abre la tortuga en una terminal y deja los comandos en otra:

```sh
ros2 run turtlesim turtlesim_node
```

## **Nodos y teleoperación**

```sh
# Controlar con el teclado (flechas)
ros2 run turtlesim turtle_teleop_key
```

 `Teleoperar otra tortuga` 

```sh
ros2 run turtlesim turtle_teleop_key --ros-args --remap /turtle1/cmd_vel:=/turtle2/cmd_vel
```

`Ver nodos y tópicos`

```sh
ros2 node list
```

```sh
ros2 node list
```

## **Tópicos y mensajes**

| Tópico | Tipo | Dirección |
| ----- | ----- | ----- |
| `/turtle1/cmd_vel` | `geometry_msgs/msg/Twist` | Tú le envías (mover) |
| `/turtle1/pose` | `turtlesim/msg/Pose` | La tortuga publica |
| `/turtle1/color_sensor` | `turtlesim/msg/Color` | La tortuga publica |

`Escuchar posición y color`

```sh
ros2 topic echo /turtle1/pose
```

```sh
ros2 topic echo /turtle1/pose --once
```

```sh
ros2 topic echo /turtle1/color_sensor
```

`Avanzar una vez`

```sh
ros2 topic pub --once /turtle1/cmd_vel geometry_msgs/msg/Twist 
```

`Girar una vez`

```sh
ros2 topic pub --once /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 0.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 1.5}}" 
```

`Hacer círculos (se repite cada 1 segundo, Ctrl+C para parar)`

```sh
ros2 topic pub -r 1 /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 1.8}}"
```

`Retroceder`

```sh
ros2 topic pub --once /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: -2.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 0.0}}" 
```

## 

## **Servicios**

| Servicio | Tipo |
| ----- | ----- |
| `/clear` | `std_srvs/srv/Empty` |
| `/reset` | `std_srvs/srv/Empty` |
| `/spawn` | `turtlesim/srv/Spawn` |
| `/kill` | `turtlesim/srv/Kill` |
| `/turtle1/set_pen` | `turtlesim/srv/SetPen` |
| `/turtle1/teleport_absolute` | `turtlesim/srv/TeleportAbsolute` |
| `/turtle1/teleport_relative` | `turtlesim/srv/TeleportRelative` |

`Ver servicios`

```sh
ros2 service list
```

```sh
ros2 service list -t
```

`Borrar el rastro dibujado`

```sh
ros2 service call /clear std_srvs/srv/Empty
```

`Reiniciar todo (borra rastro y regresa la tortuga al centro)`

```sh
ros2 service call /reset std_srvs/srv/Empty
```

`Crear una nueva tortuga`

```sh
ros2 service call /spawn turtlesim/srv/Spawn "{x: 2.0, y: 2.0, theta: 0.0, name: 'turtle2'}"
```

`Eliminar una tortuga`

```sh
ros2 service call /kill turtlesim/srv/Kill "{name: 'turtle2'}"
```

`Cambiar el color y grosor del rastro (off: 1 = sin dibujar, 0 = dibujando)`

```sh
ros2 service call /turtle1/set_pen turtlesim/srv/SetPen "{r: 255, g: 0, b: 0, width: 5, 'off': 0}"
```

`Apagar el lápiz (no dibuja al moverse)`

```sh
ros2 service call /turtle1/set_pen turtlesim/srv/SetPen "{r: 255, g: 255, b: 255, width: 3, 'off': 1}"
```

`Teletransportar a una posición (el mapa va de 0 a 11)`

```sh
ros2 service call /turtle1/teleport_absolute turtlesim/srv/TeleportAbsolute "{x: 5.5, y: 5.5, theta: 0.0}"
```

`Moverse relativo a donde está`

```sh
ros2 service call /turtle1/teleport_relative turtlesim/srv/TeleportRelative "{linear: 2.0, angular: 1.57}"
```

`Ver la estructura de cualquier servicio`

```sh
ros2 interface show turtlesim/srv/Spawn
```

## **Acciones**

| Acción | Tipo |
| ----- | ----- |
| `/turtle1/rotate_absolute` | `turtlesim/action/RotateAbsolute` |

`Ver acciones`

```sh
ros2 action list
```

```sh
ros2 action list -t
```

`Info de la acción`

```sh
ros2 action info /turtle1/rotate_absolute
```

`Rotar a un ángulo en radianes (1.57 = 90°)`

```sh
ros2 action send_goal /turtle1/rotate_absolute turtlesim/action/RotateAbsolute "{theta: 1.57}"
```

`Lo mismo pero viendo el feedback en tiempo real`

```sh
ros2 action send_goal /turtle1/rotate_absolute turtlesim/action/RotateAbsolute "{theta: 3.14}" --feedback
```

`Ver la estructura (Goal / Feedback / Result)`

```sh
ros2 interface show turtlesim/action/RotateAbsolute
```

## **Parámetros (color de fondo)**

```sh
ros2 param list
```

```sh
ros2 param set /turtlesim background_r 255
```

 

```sh
ros2 param set /turtlesim background_g 0
```

 

```sh
ros2 param set /turtlesim background_b 0
```

## **Ver las interfaces de mensajes**

```sh
ros2 interface show geometry_msgs/msg/Twist
```

```sh
ros2 interface show turtlesim/msg/Pose
```

```sh
ros2 interface show turtlesim/msg/Color
```

## **Tips**

* Los ángulos van en **radianes**: 1.57 ≈ 90°, 3.14 ≈ 180°, 6.28 ≈ 360°.  
* En `set_pen`, la palabra `'off'` va entre comillas simples dentro de las comillas dobles porque `off` es palabra reservada en YAML.  
* Si copias un comando y falla por comillas, revisa que tu terminal no haya cambiado las comillas rectas `"` por curvas `“ ”`.  
* Para cualquier comando que no recuerdes, usa el patrón : `list` → `info` → `interface show` → ejecutar.

