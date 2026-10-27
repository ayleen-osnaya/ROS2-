pasa esto a .md 
crear nuestro paquete turtlesim 

para crear paquetes en ros2 con base python es

ros2 pkg create --build-type ament_python nombrePaquete

para que sea con c++

ros2 pkg create --build-type ament_cmake nombrePaquete

nosotros haremos un paquete de python , antesde hacerlo tenemos que crear nuestro workspaces si es que no tienes uno 

mkdir -p workspaces/tmr_tutorials_ws/src

dentro de src (source) es donde ya sabemos que estan nuestrospaquetes por lo que cambiamos de direcctorio hacia src para crear nuestro paquete

cd workspaces/tmr_tutorials_ws/src

dentro creamos nuestro paquete 

ros2 pkg create --build-type ament_python turtle_trajectory

podemos ver lo que hay dentro con 

ls turtle_trajectory/

dentro encontraremos un directorio llamado turtle_trajectory donde se encontraran nuestros ejecutables o archivos .py

tambien encontraremos otros directorios y archivos como 

test y resource: que podemos usar para hacer pruebas previas 

setup.cfg: que usa ros2 para saber que tipo de python usamos 

setup.py:  es donde nosotros aclaramos dependencias y cosas que se requieren para usar nuestro paquete

package.xml: es quien explica y tiene la informacion de nuestro paquete

para poder empezar nuestro codigo entraremos a src desde visual studio con 

code .

dentro de turtle_trajectory y otra vez dentro de turtle_trajectory hacemos un nuevo file llamado 

turtle_generator.py




