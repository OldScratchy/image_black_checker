# Image Black Checker

## Prerequisitos

Seguir los pasos de este [link](https://docs.opencv.org/4.x/d7/d9f/tutorial_linux_install.html).

O si la queres hacer facil:

```bash
apt-get install libopencv-dev
```

Tambien contar con GCC, Python y el paquete `rich`.

## Pasos a seguir

1. Definir la ruta de las imagenes a analizar y especificar en la variable directory_path.
2. Compilar:

    ```bash
    g++ image_black_checker.cpp -o image_black_checker `pkg-config --cflags --libs opencv4`
    ```

3. Correr check_images.py.
