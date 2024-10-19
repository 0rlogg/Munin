from dotenv import load_dotenv
import os
from google_search_api import GoogleSearchApi
from duck_search_api import DuckSearchApi
from header import Header  
import argparse

def main():

    load_dotenv()
    Header()
    API_KEY_GOOGLE = os.getenv("API_KEY_GOOGLE")
    SEARCH_IDENTIFIER = os.getenv("SEARCH_IDENTIFIER")
    #API_KEY_DUCKDUCKGO = os.getenv("API_KEY_DUCKDUCKGO")
    ASCII_HEADER = os.getenv("ASCII_HEADER")

    query= 'DANIEL'

    google_search = GoogleSearchApi(API_KEY_GOOGLE, SEARCH_IDENTIFIER)
    Googleresult = google_search.search(query)
    
    print(Googleresult)
    print("------------------------------------------------")
    duck_search = DuckSearchApi()
    duckresult = duck_search.search(query)
    print(duckresult)


if __name__ == "__main__":

    main()

