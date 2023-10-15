let posts = []

function createImageResultHTML(result) {
	return `
		<div class="imageResult">
			<a href="${result.url}" target="_blank">
				<img src="${result.thumbnail}" alt="${result.title}" />
			</a>
		</div>
	`
}

function createImageResultsHTML(results) {

	posts = []

	results.forEach((result, index) => {
		let item = {
			id: index,
			title: result.title,
			image: result.thumbnail,
		}
		posts.push(item)
	})

	if (previousScreenSize < 600) {
		generateMasonryGrid(1, posts)
	} else if (previousScreenSize >= 600 && previousScreenSize < 1000) {
		generateMasonryGrid(2, posts)
	} else {
		generateMasonryGrid(4, posts)
	}
	

	return results.map(createImageResultHTML).join("")
}

function createSiteResultHTML(result) {
	return `
		<a class="siteResult" href="${result.href}">
			<h2 class="siteTitle">${result.title}</h2>
			<span class="siteDescription">${result.body}</span>
		</a>
			
	`
}

function createSiteResultsHTML(results) {
	return results.map(createSiteResultHTML).join("")
}

function getSearchType() {
	return document.querySelector('[name="searchType"]:checked').value
}

function getDesiredResultCount() {
	let value = parseInt(document.querySelector("#resultCount").value)
	if (isNaN(value) && value > 30 && value < 1) {
		value = 10
	}
	return value
}

document.querySelector(".searchButton").addEventListener("click", async () => {
	let searchTerm = document.querySelector("#searchInput").value
	let searchType = getSearchType()
	let resultCount = getDesiredResultCount()
	let url = `/${searchType}?q=${searchTerm}&count=${resultCount}`

	let response = await fetch(url)
	let results = await response.json()

	let resultsDiv = document.querySelector(".resultsContainer")
	if (searchType === "images") {
		createImageResultsHTML(results)
	} else {
		resultsDiv.innerHTML = createSiteResultsHTML(results)
	}
})
