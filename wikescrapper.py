import wikipedia
from colorama import Fore
from colorama import Style

def search_on_wiki(query='python', lenguage='pt-br'):
    """usa um texto para achar o nome de uma pagina na wiki e retorna os possiveis resultados em forma de lista"""
    wikipedia.set_lang(lenguage)
    list_of_possible_pages = wikipedia.search(query, results=5)
    return list_of_possible_pages

def get_page_content(page_name):
    """pega os dados de uma pagina especifica e retorna o seu conteudo"""
    page = wikipedia.page(page_name)
    content = page.content
    return content

def get_link(page_name):
    page = wikipedia.page(page_name)
    link = page.url
    return link

query = input('Digite uma palavra para buscar na wiki: ')
list_of_possible_pages = search_on_wiki(query=query)

Sumario_text = Fore.BLUE + Style.BRIGHT + "Sumario:" + Style.RESET_ALL
link_text = Fore.RED + Style.DIM + "Link:" + Style.RESET_ALL
print(f"""exibindo resultados para {list_of_possible_pages[0]}
      
      
      
      
      
      
      Sumario: 
        
        
        {wikipedia.summary(list_of_possible_pages[0])}

      
      
      O {link_text} da pagina é: {get_link(list_of_possible_pages[0])}""")

