import wikipedia
import sys

agente = {'User-Agent': 'Chrome/39.0.2171.95'}

def search_on_wiki(query='python', language='pt', agente=None):
    """usa um texto para achar o nome de uma pagina na wiki e retorna os possíveis resultados em forma de lista"""
    wikipedia.set_lang(language) # linguem da pesquisa e da pagina
    if agente:
        wikipedia.set_user_agent(agente)
    list_of_possible_pages = wikipedia.search(query, results=5)
    if list_of_possible_pages == []:
        return None
    else:
        return list_of_possible_pages

def get_title(page_name):
    """retorna o titulo da pagina"""
    page = wikipedia.page(page_name)
    title = page.title
    return title


def get_page_content(page_name):
    """pega os dados de uma pagina especifica e retorna o seu conteudo"""
    page = wikipedia.page(page_name)
    content = page.content
    return content

def get_category(page_name):
    """retorna as categorias de uma pagida da wiki"""
    page = wikipedia.page(page_name)
    categorys = page.categories
    # tira a palavra Categoria dos indices da lista pra n ficar repetitivo
    for i in range(len(categorys)):
        categorys[i] = categorys[i].replace('Categoria:', '')
    return categorys


def get_images(page_name):
    page = wikipedia.page(page_name)
    images = page.images
    return images

def get_page_id(page_name):
    """pega o id de uma pagina especifica"""
    page = wikipedia.page(page_name)
    id = page.pageid
    return id


def get_link(page_name):
    """rerorna o link da pagina"""
    page = wikipedia.page(page_name)
    link = page.url
    return link

def get_references(page_name):
    page = wikipedia.page(page_name)
    refences = page.references
    return refences

def main():
    query = str(input('Digite uma palavra para buscar na wiki: '))
    list_of_possible_pages = search_on_wiki(query=query)
    if list_of_possible_pages == None or list_of_possible_pages == []:
        print(f"não encontrei nenhuma pagina relacionada a {query}")
        sys.exit(1)


    print(f"""
    Exibindo resultados para {list_of_possible_pages[0]}
    """)
    print(f"""{get_title(list_of_possible_pages[0])}
        
        
        
        {get_page_content(list_of_possible_pages[0])}
        
        Referencias: {get_references(list_of_possible_pages[0])}
        
        O link da pagina é {get_link(list_of_possible_pages[0])}
        Id {get_page_id(list_of_possible_pages[0])}
        
        Esses foram os possiveis resultados que achei{list_of_possible_pages}""")


if __name__ == '__main__':
    try:
        main()
    except wikipedia.exceptions.DisambiguationError as e:
        print("n achei nada relacionado a sua pesquisa")
        print(f"Seu resultado pode se referir a: {str(e.options)}")
