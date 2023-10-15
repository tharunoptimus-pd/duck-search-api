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