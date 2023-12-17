from fastapi import FastAPI
from scrapista import *

app = FastAPI()

azs = AmazonScraper()
ims = ImdbScraper()
ws = WikiScraper()
gsr = GoodReadsScraper()

# welcome
@app.get("/")
async def root():
    return {"Status": "Welcome"}


# amazon
@app.get("/amazon")
async def amazon(url):
    return azs.scrape_item(url)

@app.get("/amazon/{keyword}")
async def amazon_keyword(keyword):
    return azs.scrape_keyword(keyword)

# imdb
@app.get("/imdb/top")
async def imdb():
    return ims.top_ranked_movies

@app.get("/imdb/popular")
async def imdb_popular():
    return ims.popular_movies

@app.get("/imdb")
async def imdb_name(url):
    return ims.scrape_movie(url)


# wikipedia
@app.get("/wiki/disney-movies")
async def wiki_disney():
    return ws.disney_movies

@app.get("/wiki")
async def wiki(url):
    return ws.scrape_custom(url=url)

@app.get("/wiki/{custom}")
async def wiki_custom(custom):
    return ws.scrape_custom(name=custom)


# goodreads
@app.get("/goodreads/quotes/popular")
async def goodreads_popular():
    return gsr.popular_quotes

@app.get('/goodreads')
async def goodreads_book(url):
    return gsr.scrape_book(url)

@app.get("/goodreads/{genre}")
async def goodreads_genre(genre):
    return gsr.scrape_books_by_genre(genre)

@app.get("/goodreads/quotes/{tag}")
async def goodreads_tag(tag):
    return gsr.scrape_quotes_by_tag(tag)