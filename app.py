from duckduckgo_search import DDGS
from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
	return {"message": "This is a Search API", 
		"usage": {
			"sites": {
				"url": "/sites?q=your_query",
				"params": {
					"q": "your_query",
					"count": "number_of_results (default: 5)"
				}
			}, 
			"images": {
				"url": "/images?q=your_query",
				"params": {
					"q": "your_query",
					"count": "number_of_results (default: 5)"
				}
			}
		}
	}

@app.get("/sites")
def search(q: Union[str, None] = None, count: int = 5):
	if q:
		with DDGS() as ddgs:
			results = [r for r in ddgs.text(q, max_results=count)]
			return results
	else:
		return {"message": "Sites API Online"}
