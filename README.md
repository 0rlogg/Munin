# Munin: Buscador de Información en Línea

**Munin** es una herramienta de búsqueda que permite a los usuarios realizar consultas en Google y DuckDuckGo, obteniendo resultados relevantes de forma sencilla y eficiente. Utilizando las APIs de ambos motores de búsqueda, Munin ofrece una interfaz amigable para recuperar información de la web de manera programática.

## Características

- **Búsqueda en Google**: Permite realizar búsquedas utilizando la API de Google Custom Search, proporcionando resultados estructurados y fáciles de interpretar.

- **Búsqueda en DuckDuckGo**: Utiliza la API de DuckDuckGo para acceder a resultados de búsqueda sin rastrear al usuario, manteniendo la privacidad.

## Requisitos

- Python 3.x
- Las bibliotecas requeridas:
  - `requests`
  - `python-dotenv` para manejar las variables de entorno.

## Configuración

1. **Clona el repositorio:**

   ```bash
   git clone https://github.com/tu_usuario/mi_repositorio.git
   cd mi_repositorio
   ```

2. **Crea un archivo `.env` en la raíz del proyecto con las siguientes variables:**

   ```plaintext
   API_KEY_GOOGLE=tu_api_key_google
   SEARCH_IDENTIFIER=tu_search_identifier
   API_KEY_DUCKDUCKGO=tu_api_key_duckduckgo
   ```
3. **Instala las dependencias:**

   Puedes instalar las dependencias manualmente o utilizar el archivo requirements.txt. Aquí está el contenido del archivo:

      ```plaintext
      requests
      python-dotenv
      ```

   O Puedes usar el archivo requirements.txt
  
      ```bash
      pip install -r requirements.txt
      ```
## Uso

1. Para ejecutar el programa, simplemente corre el archivo munin.py desde la terminal:

      ```bash
       python munin.py
      ```

## Contribuciones

Las contribuciones son bienvenidas. Siéntete libre de abrir un issue o un pull request para sugerir mejoras o nuevas funcionalidades.
