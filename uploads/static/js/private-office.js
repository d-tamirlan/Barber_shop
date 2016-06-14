// var
// 	info_menu = document.querySelector(".info_menu"),
// 	orders_menu = document.querySelector(".orders_menu"),
// 	records_menu = document.querySelector(".records_menu"),
	

// 	info = document.querySelector(".information"),
// 	orders = document.querySelector(".orders"),
// 	records = document.querySelector(".records");

// if ((info != null) && (info_menu != null)) {
// 	info.addEventListener("click", function(event){
// 		event.preventDefault();
// 		orders.classList.remove("modal-show");
// 		records.classList.remove("modal-show");
// 		info.classList.add("modal-show");
// 	});
// };

// if ((orders != null) && (orders_menu != null)) {
// 	orders.addEventListener("click", function(event){
// 		alert("salam");
// 		event.preventDefault();
// 		info.classList.remove("modal-show");
// 		records.classList.remove("modal-show");
// 		orders.classList.add("modal-show");
// 	});
// };

// if ((records != null) && (records_menu != null)) {
// 	records.addEventListener("click", function(event){
// 		event.preventDefault();
// 		info.classList.remove("modal-show");
// 		orders.classList.remove("modal-show");
// 		records.classList.add("modal-show");
// 	});
// };

$(document).ready(function(){
	$(".orders_menu").click(function(){
		$(".profile").css("display", "none")
		$(".records").css("display", "none")
		$(".orders").css("display", "block")
	});
});