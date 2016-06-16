$(document).ready(function($){
	$("#reg-form").submit(function(event){
		event.preventDefault();
		var form_data = $(this).serialize();
		$.ajax({
			type: "POST",
			url: "/registration/",
			data: form_data,
			cache: false,
			success: function(response_data){
				$("#user_error").html(response_data.username)
				$("#password_error").html(response_data.password1)
				$("#password2_error").html(response_data.password2)
			}
		});
	});
});