from gnews import GNews

google_news = GNews()
google_news.language = 'pt-br'
google_news.max_results = 10
google_news.country = 'Brazil'
busca = input('O que você deseja saber hoje? ')
google_news.period = input('Tempo da noticia: ')
result = google_news.get_news(busca)
for x in result:
    print("-------------------------------------||------------------------------------"*2)
    print("Titulo: ", x['title'])
    print("Data ", x['published date'])
    print("Descrição---", x['description']),
    print("Link--- ", x['url'])
    print()
