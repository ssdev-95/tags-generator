const form = document.getElementById('form')

form.addEventListener('submit', (event)=>{
	event.preventDefault()
	const data = new FormData(form)
	console.log(JSON.stringify(data))
})
