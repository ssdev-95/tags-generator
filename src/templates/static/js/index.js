const form = document.getElementById('form')

form.addEventListener('submit', async (event)=>{
	event.preventDefault()
	const formData = new FormData(event.target)


	let type = 'BARCODE'
	
	if (!!location.search) {
		console.log(location.search)
		const [_, query] = location.search.split('=')
		type = query.toUpperCase()
	}

	const body = {
		extension: formData.get('extension'),
		product_code: formData.get('product_code')
	}

	const resRAW = await fetch(`/tags/create?type=${type}`, {
		method: 'POST',
		headers: { 'content-type': 'application/json' },
		body: JSON.stringify(body)
	})

	const resJSON = await resRAW.json()
	console.log(resJSON)
})
