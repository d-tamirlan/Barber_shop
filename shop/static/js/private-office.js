$(document).ready(function(){
	$(".profile_menu").click(function(){
		$(".records").css("display", "none");
		$(".orders").css("display", "none");
		$(".profile").css("display", "block");
	});

	$(".orders_menu").click(function(){
		$(".profile").css("display", "none");
		$(".records").css("display", "none");
		$(".orders").css("display", "block");
	});

	$(".records_menu").click(function(){
		$(".profile").css("display", "none");
		$(".orders").css("display", "none");
		$(".records").css("display", "block");
	});
});