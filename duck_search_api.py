import requests

class DuckSearchApi:
    
    def search(self, query):
        """Function to perform the search on DuckDuckGo"""
        final_result = []
        
        # Construct the request URL with parameters
        duck_url = f"http://api.duckduckgo.com/?q={query}&format=json&no_redirect=1&no_html=1&skip_disambig=1"
        response = requests.get(duck_url)
        
        if response.status_code == 200:
            data = response.json()
            results = data.get("RelatedTopics", [])  # Adjusted to fetch from 'RelatedTopics'
            if results:  # Ensure results are not empty
                sresults = self.results_search(results)
                final_result.extend(sresults)
            else:
                print(f"No results found for query: {query}")  # Notify user about no results
        else:
            print(f"Error: {response.status_code}")

        return final_result
    
    def results_search(self, results):
        """Filter and return the search results"""
        results_search = []
        for r in results:
            if 'Text' in r and 'FirstURL' in r:  # Check for required keys
                sresults = {
                    "Title": r['Text'],
                    "Link": r['FirstURL']
                }
                results_search.append(sresults)
        return results_search
