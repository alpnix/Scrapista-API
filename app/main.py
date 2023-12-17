from fastapi import FastAPI
from scrapista import *

app = FastAPI()

azs = AmazonScraper()

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