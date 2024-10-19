import requests

class GoogleSearchApi:
    def __init__(self, api_key, search_id):
        """
        Nueva instancia de google engine search, esta clase nos permite realizar peticiones a la api de google
        
        ARGS:
            API_KEY_GOOGLE (String) Clave api de google.
            SEARCH_IDENTIFIER (String) identificador de motor de busqueda.
        """
        self.api_key = api_key
        self.search_id = search_id
    
    def search (self, query, start_page=1, pages=1, lang="lang_es"):
        """Funcion para realizar la busqueda en google"""
        final_result = []
        results_per_page = 10 
        for page in range(pages):
            start_index = (start_page -1) * results_per_page + 1 + (page * results_per_page)
            google_url =f"https://www.googleapis.com/customsearch/v1?key={self.api_key}&cx={self.search_id}&q={query}&start{start_index}&lr={lang}"
            response = requests.get(google_url)
            if response.status_code == 200:
                data = response.json()
                results = data.get("items")  # Check for the 'items' key
                if results:  # Ensure results are not None or empty
                    sresults = self.results_search(results)
                    final_result.extend(sresults)
                else:
                    print(f"No results found for query: {query}")  # Notify user about no results
                    break  # Exit the loop if no results are found
            else:
                print(f"Error fetching results: HTTP {response.status_code}")
                break
        return final_result
    
    def results_search (self, results):
        """Filtra y devuelve los resultados de la consulta"""
        results_search = []
        for r in results:
            sresults = {}
            sresults["Title"] = r.get("title")
            sresults["Snippet"] = r.get("snippet")
            sresults["Link"] = r.get("link")
            results_search.append(sresults)
        return results_search
    
    