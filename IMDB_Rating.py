#### script for imdb movie rating website
from bs4 import BeautifulSoup
import requests, openpyxl


# creating excel file
excel = openpyxl.Workbook()
sheet = excel.active
# naming excel file
sheet.title = 'Top rated movies'

# creating headings for (attributes)
sheet.append(['Movie Rank', 'Name', 'Year','IMDB Rating'])

try:

    source = requests.get('https://www.imdb.com/chart/top/')
    source.raise_for_status()
    soup = BeautifulSoup(source.text, 'html.parser')
    # print(soup)
    movies = soup.find('tbody', class_ = 'lister-list').find_all('tr')
    # print(len(movies))

    for movie in movies:
        name = movie.find('td', class_ = 'titleColumn').a.text
        rank = movie.find('td', class_ = 'titleColumn').get_text(strip=True).split('.')[0]
        year = movie.find('td', class_ = 'titleColumn').span.text.strip('()')
        rating = movie.find('td', class_ = 'ratingColumn imdbRating').strong.text

        # print(f'Name:{name} \trank:{rank} \tyear:{year} \trating:{rating}')
        
        sheet.append([rank,name,year,rating])

except Exception as e:
    print(e)

excel.save('IMDB rating.xlsx')