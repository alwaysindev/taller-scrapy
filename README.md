# Taller: Creación de una Araña Web con Scrapy

Este proyecto es parte de un taller donde aprenderemos a construir una araña web utilizando el framework Scrapy. Incluye todos los pasos necesarios, desde la configuración del entorno hasta la implementación de la araña y la ejecución de pruebas.

---

## Requisitos previos

Antes de comenzar, asegúrate de tener lo siguiente instalado:

- Python 3.9 o superior
- pip (Gestor de paquetes de Python)
- Acceso a la terminal o línea de comandos

---

## Configuración del entorno

### 1. Crear un entorno virtual

Para mantener las dependencias de este proyecto aisladas, utilizaremos `venv` para crear un entorno virtual.

```bash
python -m venv scrapy_venv
```

Esto creará una carpeta llamada `scrapy_venv` en el directorio actual.

### 2. Activar el entorno virtual

- **Windows:**

  ```bash
  scrapy_venv\Scripts\activate
  ```

- **macOS/Linux:**

  ```bash
  source scrapy_venv/bin/activate
  ```

Una vez activado, deberías ver el prefijo `(scrapy_venv)` en tu terminal.

### 3. Instalar Scrapy

Con el entorno virtual activado, instala Scrapy con pip:

```bash
pip install scrapy
```

Verifica que Scrapy esté instalado correctamente ejecutando:

```bash
scrapy --version
```

---

## Crear el proyecto Scrapy

1. Crea un nuevo proyecto de Scrapy:

   ```bash
   scrapy startproject zacatrus_project
   ```

   Esto generará la estructura de carpetas y archivos inicial para el proyecto.

2. Navega al directorio del proyecto:

   ```bash
   cd zacatrus_project
   ```

---

## Implementar una araña básica

1. Dentro del directorio del proyecto, crea una nueva araña con el comando:

   ```bash
   scrapy genspider zacatrus_spider zacatrus.es
   ```