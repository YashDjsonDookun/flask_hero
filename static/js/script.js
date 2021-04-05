$(function(){
	$('#btn-getData').click(function(e){
        e.preventDefault();
        let name_inputBox = $('#name').val();
        let name_dropdown = $('#names option:selected').text();

		$.ajax({
			url: '/search',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
                $('#name').val("");
                $('#names').prop('selectedIndex',0);
				// console.log(response);
                $("#app").load(location.href + " #app");
			},
			error: function(error){
				console.log(error);
			}
		});
	});
});
