document.addEventListener('DOMContentLoaded', () => {
	load_page('Home');
	document.querySelectorAll('.nav-link').forEach(link => {
		link.onclick = () => {
			load_page(link.dataset.page);
			return false;
		};
	});
});

function load_page(name) {
	const request = new XMLHttpRequest();
	request.open('GET', `/${name}`);
	request.onload = () => {
		const response = request.responseText;
		document.querySelector('#top').innerHTML = response;
	};
	request.send();
}

/*
$(document).ready(function() {
	$("#Home").prepend('<i class="fa fa-home fa-2x"></i>');
	$("#About").prepend('<i class="fa fa-user fa-2x"></i>');
	$("#Projects").prepend('<i class="fa fa-code fa-2x"></i>');
	$("#Hobby").prepend('<i class="fa fa-gamepad fa-2x" style></i>');
}) */