from dotenv import load_dotenv, set_key
import os
from google_search_api import GoogleSearchApi
from duck_search_api import DuckSearchApi
from header import Header  
import argparse
import sys
from Search_parser import SearchParser

def env_configuration():
    """Configura el .env con  los valores proporcionados por el usuario"""
    Gapi_key = input("Introduce el API KEY de Google:")
    Gsearch_id = input("Introduce el Id del buscador personalizado de Google:")
    set_key(".env", "API_KEY_GOOGLE", Gapi_key)
    set_key(".env", "SEARCH_IDENTIFIER", Gsearch_id)


def main(query, configure_env, star_pages, pages, lang, output_json, output_html):
    
    #comprobación existencia fichero .env
    env_exists = os.path.exists(".env")
    if not env_exists or configure_env:
        env_configuration()
        print("Archivo .env configurado correctamente.")
        sys.exit(1)    
    load_dotenv()
    Header()
  
    API_KEY_GOOGLE = os.getenv("API_KEY_GOOGLE")
    SEARCH_IDENTIFIER = os.getenv("SEARCH_IDENTIFIER")

    if not query:
        print("Debes indicar una consulta con el comando -q, puedes usar el comando -h para mostrar el manual.")
        sys.exit(1)    

    google_search = GoogleSearchApi(API_KEY_GOOGLE, SEARCH_IDENTIFIER)
    Googleresult = google_search.search(query, pages=pages, start_page=star_pages,lang=lang)
    
    result_parser = SearchParser(Googleresult)
    
    result_parser.show_console()

    if output_html:
        result_parser.html_export(output_html)

    if output_json:
        result_parser.json_export(output_json)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Herramienta que permite realizar hacking con buscadores de manera automática.")
    parser.add_argument("-q", "--query", type=str, help="Especifica el dork que se desea buscar .\n Ejemplo: -q 'filetype: sql \"MySQL dump\" (pass | password | passwd | pwd)'")
    parser.add_argument("-c", "--configure", action="store_true", help="Inicia el proceso de configuración del archivo .env \n Utiliza esta opción som otros argumentos para configurar las claves")
    parser.add_argument("-sp", "--start_pages", type=int, default = 1, help="Define la página de inicio del buscador para obtener los resultados")
    parser.add_argument("-p", "--pages", type=int, default = 1, help="Define el número de páginas de las que se obtienen resultados")
    parser.add_argument("-l", "--lang",default = "lang_es", type=str,  help="Define el idioma de los resultados de busqueda por defecto es 'lang_es'")
    parser.add_argument("--json", type=str,  help="Exporta resultados en formato JSON en el fichero especifico")
    parser.add_argument("--html", type=str,  help="Exporta resultados en formato HTML en el fichero especifico")
    
    arguments = parser.parse_args()

    main(query=arguments.query,
         configure_env=arguments.configure,
         star_pages=arguments.start_pages,
         pages=arguments.pages,
         lang=arguments.lang,
         output_json=arguments.json,
         output_html=arguments.html)

    