from duckduckgo_search import DDGS
from typing import Union
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
	return FileResponse("static/index.html")


@app.get("/sites")
def search(q: Union[str, None] = None, count: int = 5):
	if q:
		with DDGS() as ddgs:
			results = [r for r in ddgs.text(q, max_results=count)]
			return results
	else:
		return {"message": "Sites API Online"}

@app.get("/images")
def images(q: Union[str, None] = None, count: int = 5):
	if q:
		with DDGS() as ddgs:
			results = [r for r in ddgs.images(q, max_results=count)]
			return results
	else:
		return {"message": "Images API Online"}