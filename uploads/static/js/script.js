var 
	login_link = document.querySelector("#login"),
	map_link = document.querySelector(".travel"),
	modal_login = document.querySelector(".modal-login"),
	modal_map = document.querySelector(".modal-map"),
	modal_login_close = document.querySelector(".modal-login-close"),
	modal_map_close = document.querySelector(".modal-map-close"),
	overlay = document.querySelector(".overlay");

login_link.addEventListener("click", function(event){
	event.preventDefault();
	modal_login.classList.add("modal-show");
	overlay.classList.add("modal-show");
});

modal_login_close.addEventListener("click", function(event){
	event.preventDefault();
	modal_login.classList.remove("modal-show");
	overlay.classList.remove("modal-show");
});

modal_map_close.addEventListener("click", function(event){
	event.preventDefault();
	modal_map.classList.remove("modal-show");
	overlay.classList.remove("modal-show");
});

map_link.addEventListener("click", function(event){
	event.preventDefault();
	modal_map.classList.add("modal-show");
});

if ("{{record_successful}}") {
	alert("Ваша заявка принята. Спасибо, что выбрали нас!")
};