# ERROR: libgl1-mesa-glx

Este es un error ocasionado a la hora de instalar un software en Ubuntu el cual contiene este paquete que fue deprecado a partir de versiones posteriores a la 23.10, ya que era un paquete de transición para migrar o actualizar a un nuevo sistema, sin causar problemas pero este ya no es necesario.

Información del paquete: https://ubuntu.pkgs.org/22.04/ubuntu-updates-universe-amd64/libgl1-mesa-glx_23.0.4-0ubuntu1~22.04.1_amd64.deb.html

## Pasos

1. Descargar el archivo por terminal: wget http://archive.ubuntu.com/ubuntu/pool/universe/m/mesa/libgl1-mesa-glx_23.0.4-0ubuntu1~22.04.1_amd64.deb
2. Instalar este paquete, estando en descargas: sudo apt install ./"nombre-del-paquete"
3. Ya estaría solucionado y podemos volver a instalar el software que nos impidió este error.

>[!NOTE]
> Instalando los paquetes libgl1 y libglx-mesa0 por separado deberían dar un resultado similar sin tener que utilizar este paquete obsoleto.
