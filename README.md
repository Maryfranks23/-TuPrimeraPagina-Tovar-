# Tu Primera Pagina de Recargas

Esta es una sencilla web de Django para gestionar recargas de celulares.

## Cómo probar la aplicación:

1.  Asegúrate de tener Python y Django instalados en tu entorno.
2.  Clona este repositorio: `git clone https://github.com/Maryfranks23/TuPrimeraPagina-Tovar.git`
3.  Navega al directorio del proyecto: `cd TuPrimeraPagina-Tovar`
4.  Crea y activa un entorno virtual (recomendado):
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Linux/macOS
    .\venv\Scripts\activate  # En Windows
    ```
5.  Instala las dependencias: `pip install -r requirements.txt` (si tienes un archivo `requirements.txt`, sino omite este paso).
6.  Ejecuta las migraciones: `python manage.py migrate`
7.  Crea un superusuario para acceder al panel de administración (opcional, pero útil para verificar los datos): `python manage.py createsuperuser`
8.  Inicia el servidor de desarrollo: `python manage.py runserver`
9.  Abre tu navegador web y ve a las siguientes URLs para probar las funcionalidades:
    * Página principal: `http://127.0.0.1:8000/`
    * Crear Empresa: `http://127.0.0.1:8000/crear/empresa/`
    * Crear Cliente: `http://127.0.0.1:8000/crear/cliente/`
    * Crear Recarga: `http://127.0.0.1:8000/crear/recarga/`
    * Buscar Recarga por Teléfono: `http://127.0.0.1:8000/buscar/recarga/`
    * Panel de Administración (para verificar los datos): `http://127.0.0.1:8000/admin/`

## Funcionalidades Principales:

* **Creación de Empresas:** Permite agregar nuevas compañías de recarga.
* **Creación de Clientes:** Permite registrar nuevos clientes.
* **Creación de Recargas:** Permite registrar nuevas recargas asociando un cliente, una empresa y un monto.
* **Búsqueda de Recargas:** Permite buscar recargas por el número de teléfono del cliente.
