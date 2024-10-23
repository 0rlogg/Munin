import json
from rich.console import Console
from rich.table import Table

class SearchParser:

    def __init__(self,results):
        self.results = results
    
    def html_export (self, output_file):
        with open("html_export.html", 'r', encoding='utf-8') as f:
            plantilla = f.read()

        html_elements = ''
        for indice, resultado in enumerate(self.results, start=1):
            element = f'<div class="resultado">' \
                      f'<div class="indice"> Resultado {indice}</div>'\
                      f'<h5> {resultado ["Title"]}</h5>' \
                      f'<p> {resultado ["Snippet"]}</p>' \
                      f'<a href = "{resultado ["Link"]}" target = "_blank">{resultado ["Link"]}</a>' \
                      f'</div>' 
            html_elements += element
            html_report = plantilla.replace('{{ resultados }}', html_elements)
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_report)
            print(f'resultados exportados a HTML. Fichero: {output_file}')
    
    def json_export (self, output_file):
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(self.results, f, ensure_ascii=False, indent=4)
            print(f"resultados exportados a JSON. Fichero: {output_file}")

    def show_console (self):
        console = Console()
        table = Table(show_header =True, header_style = "bright_green") 
        table.add_column("#", style="dim")
        table.add_column("Title")
        table.add_column("Description")
        table.add_column("Link")
        
        for indice, resultado in enumerate(self.results, start=1):
                table.add_row(str(indice), resultado["Title"], resultado["Snippet"], resultado["Link"])
                table.add_row("","","","")
                console.print(table)

