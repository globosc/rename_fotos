# Renombrador de Archivos por Fecha

Este script Python te permite renombrar archivos de fotos en una carpeta según su fecha de modificación o creación.

## Descripción

Cuando acumulas una gran cantidad de fotos en una carpeta, a veces puede ser difícil organizarlas de manera efectiva. Este script resuelve ese problema al renombrar archivos de fotos en función de su fecha de modificación o creación, lo que facilita la búsqueda y organización de tus fotos.

## Uso

### Requisitos previos

- Python 3.11

### Ejecución

1. Clona o descarga este repositorio en tu computadora.
2. Abre una terminal o línea de comandos.
3. Navega al directorio donde se encuentra el script.
4. Ejecuta el script con el siguiente comando: `python renombrar_archivos_por_fecha.py`

5. Sigue las instrucciones en la pantalla.

## Configuración Personalizada

Puedes personalizar la configuración del script ajustando las siguientes variables en el código:

- `ruta_base`: La ruta de la carpeta que contiene los archivos de fotos que deseas renombrar.
- `archivo_registro`: La ruta del archivo de registro que registra los archivos procesados y sus nuevos nombres.

## Funcionamiento

- El script escanea la carpeta y sus subdirectorios en busca de archivos de fotos válidos.
- Obtiene la fecha de modificación y creación de cada archivo.
- Construye un nuevo nombre de archivo basado en la fecha en el formato 'IMG_DDMMYYYY_HHMMSS'.
- Evita colisiones de nombres de archivo agregando un contador si es necesario.
- Renombra el archivo con el nuevo nombre.
- Registra los archivos procesados en el archivo de registro.

## Contribución

Si deseas contribuir a este proyecto, sigue estos pasos:

1. Haz un fork del repositorio.
2. Clona tu repositorio fork en tu máquina local.
3. Crea una nueva rama para tu contribución: `git checkout -b mi-contribucion`.
4. Realiza tus cambios y commitea: `git commit -m "Añade mi contribución"`.
5. Haz un push de tus cambios: `git push origin mi-contribucion`.
6. Crea una solicitud de extracción en GitHub.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para obtener más detalles.

## Autor

- [Tu Nombre](https://github.com/tu-usuario)

## Contacto

Si tienes alguna pregunta o sugerencia, no dudes en ponerte en contacto conmigo a través de [tu@email.com](mailto:tu@email.com).

![Licencia](https://img.shields.io/github/license/tu-usuario/tu-repositorio)


