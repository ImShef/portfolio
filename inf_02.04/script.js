const img = document.querySelector('.carousel')
const imgNum = 3
const delay = 1500
img.width = 900
img.height = 600
let i = 1
setTimeout(function tick() {
	i = i + 1
	if (i > imgNum) i = 1
	img.src = `images/${i}.jpg`
	setTimeout(tick, delay)
}, delay)
