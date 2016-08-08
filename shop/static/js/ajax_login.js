$(document).ready(function($){
	$("#login-form").submit(function(event){
		event.preventDefault();
		var form_data = $(this).serialize();
		$.ajax({
			type: "POST",
			url: "/",
			data: form_data,
			cache: false,
			success: function(response_data){
				 if (response_data == 'ok'){
                   location.reload();
                }
                else{
                   $('.error').html(response_data);
                }
            }
		});
	});
});