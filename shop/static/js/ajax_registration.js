$(document).ready(function($){
	$("#reg-form").submit(function(event){
		var form_data = $(this).serialize();
		$.ajax({
			type: "POST",
			url: "/registration/"
		})
	});
});