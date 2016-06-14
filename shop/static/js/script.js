var 
	login_link = document.querySelector("#login"),
	map_link = document.querySelector(".travel"),
	modal_login = document.querySelector(".modal-login"),
	modal_map = document.querySelector(".modal-map"),
	modal_login_close = document.querySelector(".modal-login-close"),
	modal_map_close = document.querySelector(".modal-map-close"),
	overlay = document.querySelector(".overlay"),
	record_successful = document.querySelector("#success_message"),
	order_successful = document.querySelector("#order_message");
	
if ((record_successful != null) && (record_successful.value == "True")) {
	alert("Ваша заявка принята. Спасибо, что выбрали нас !");
}
else if ((order_successful != null) && (order_successful.value == "True")){
	alert("Ваш заказ принят. Спасибо, что выбрали нас !");
};

if (login_link != null) {
	login_link.addEventListener("click", function(event){
		event.preventDefault();
		modal_login.classList.add("modal-show");
		overlay.classList.add("modal-show");
	});
};
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

if (map_link != null) {
	map_link.addEventListener("click", function(event){
		event.preventDefault();
		modal_map.classList.add("modal-show");
	});
};

