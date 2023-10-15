# Search API using DuckDuckGo Results
- Supports searching sites and images with an optional count parameter defaulting to 5

## Creating a virtual environment
- Install virtualenv using `python -m /path/to/venv`
- Eg: `python -m venv venv`

## Installation
- Clone the repository
- Install the requirements using `pip install -r requirements.txt`
- Run the app using `uvicorn app:app --reload`

## Usage

"""
This endpoint provides two search options: sites and images. 
Both options require a query parameter 'q' to be passed in the URL. 
The 'count' parameter is optional and defaults to 5 if not provided.

Usage:
- To search for sites, use the following URL: /sites?q=your_query&count=number_of_results
- To search for images, use the following URL: /images?q=your_query&count=number_of_results

Example:
- To search for sites with the query 'python' and return 10 results, use the following URL:
/sites?q=python&count=10
- To search for images with the query 'cat', use the following URL:
/images?q=cat
"""

## Example
- Searching for doggo images (http://localhost:8000/images?q=doggo&count=2)
	```json
		[
			{
				"title": "Smiling doggo | Pet dogs, Cute dogs, Doggo",
				"image": "https://i.pinimg.com/originals/7f/e1/a3/7fe1a3c59fad552cd5346451cbf51e4b.jpg",
				"thumbnail": "https://tse1.mm.bing.net/th?id=OIP.12xned9JE5YKWAU4kLqHqQHaHU&pid=Api",
				"url": "https://www.pinterest.com/pin/585538389032262522/",
				"height": 1067,
				"width": 1080,
				"source": "Bing"
			},
			{
				"title": "Nice Doggo : doggos",
				"image": "https://external-preview.redd.it/pJC1P0TVDLNyW8KrDS7dxWhYeVqlYzYdrQKeuSynYqE.jpg?auto=webp&s=a9abd5779a18020edb1e9101d4bca08241e62d62",
				"thumbnail": "https://tse4.mm.bing.net/th?id=OIP.QWw43q4sU4w_eYaVoeeX1AHaIN&pid=Api",
				"url": "https://www.reddit.com/r/doggos/comments/9ocfit/nice_doggo/",
				"height": 1024,
				"width": 923,
				"source": "Bing"
			}
		]
	```
- Searching for doggo sites (http://localhost:8000/sites?q=doggo&count=2)
	```json
		[
			{
				"title": "Doggo Definition & Meaning - Merriam-Webster",
				"href": "https://www.merriam-webster.com/dictionary/doggo",
				"body": "The meaning of DOGGO is dog. How to use doggo in a sentence."
			},
			{
				"title": "Where Did 'Doggo' Come From? Wouldn't You Like to Know, Fren | WIRED",
				"href": "https://www.wired.com/story/rise-of-doggo/",
				"body": "Doggo has the misfortune of competing in a crowded \"marketplace of words,\" Bergen notes. Synonyms, it would seem, are, ahem, a bitch. More Internet Lingo. The internet defines \"covfefe\""
			}
		]
	```
- Or you can go to / and use the UI