# Predicción TMR

**Reto:** Implemente un aplicativo web en Django que permita cargue un modelo ML preentrenado y dado un archivo en Excel con una información de un tema dado, los cargue en el modelo y haga una predición, imprimiendo el resultado en una tabla de la página html. El modelo ML puede ser cualquiera que usted entrene o encuentre en internet respecto a cualquier set de datos. Se evaluará la implementación del aplicativo, más allá de los resultados de un modelo ML.

## Instalación

1. El primer paso para usar este programa es descargarlo desde el repositorio con el siguiente comando:

    ```sh
    git clone https://github.com/Juansecod/bancolombia-test.git
    ```

    Esto creara una copia del repositorio en su computadora.

2. Ahora, accederemos a la carpeta raiz del proyecto: `bancolombia-test`

    Desde la consola lo puedes hacer con el siguiente comando:

    ```sh
    cd bancolombia-test
    ```

3. Una vez accedimos a nuestra carpeta, abriremos nuestro editor de codigo favorito. En este caso se usara como referencia vscode. Para ello puede darle click derecho sobre la ventana e clickear la opcion `Abrir con vscode`

    Si esta usando la terminal puede ejecutar el siguiente comando:

    ```sh
    code .
    ```

    Esto abrira directamente su editor de codigo configurado como predeterminado.

4. Ahora, abriremos una consola en el editor para instalar las dependencia que tiene el proyecto. Con la terminal abierta ejecutamos el siguiente comando:

    ```sh
    pip install -r requirements.txt
    ```

    > [!NOTE]
    > Se recomienda el uso de un entorno virtual para evitar conflictos de versiones o entre librerias que puede tener instalada en su maquina. Para ello ejecutamos los siguiente comandos:
    >
    >```sh
    >python -m venv venv
    >```
    >
    >Esto creara su entorno virtual, ahora lo activaremos:
    >
    > - Si esta desde una terminal cmd:
    >
    >   ```cmd
    >   cd venv/Scripts/
    >   activate.bat
    >   ```
    >
    > - Si esta usando una terminal linux
    >
    >   ```sh
    >   source venv/bin/activate
    >   ```
    >
    > Ya una vez con el entorno virtual activo, puede instalar las dependencias sin ningun conflicto

5. Ahora que tenemos nuestras dependencias instaladas, realizaremos las migraciones para evitar errores en el programa. Para ello correremos el siguiente comando:

    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

## Ejecutar entorno de desarrollo

Para ejecutar la aplicación ejecutamos el siguiente comando:

```sh
python manage.py runserver
```

Con esto ejecutara de manera local la aplicacion en el puerto `8000`. Para acceder a ella abres tu navegador favorito y accedes a [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Uso

Para un correcto uso de la aplicacion se recomienda subir archivos de excel o csv, en donde es requerido que contenga las siguientes dos columnas para una correcta prediccion del modelo:

Nombre Columna|Descripción|
-----|-----|
VALOR|Indica el valor que tenia el dolar en pesos colombianos(COP)|
VIGENCIADESDE|Indica el dia que se realizo la toma del valor|

> [!WARNING]
>
> Es de vital importancia que las columnas esten nombradas en mayuscula sostenida y sin espacios, esto debido a que el programa no reconoce otros nombres de columna. Por ello, cuenta en el repositorio con un archivo de ejemplo dentro de la carpeta `TMR Dolar - COP` con el nombre `TMR.csv`.
