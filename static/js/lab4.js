$(function() {
	$('a#calculate').bind('click', function() {
		$.getJSON('/_add_numbers', {
			a: $('input[name="a"]').val(),
			b: $('input[name="b"]').val()
		}, function(data) {
			$("#result").text(data.result);
		});
		return false;
	});
});

$(function() {
	$('a#get').bind('click', function() {
		$.getJSON('/todo/api/v1.0/tasks', function(data) {
			$("#rest_result").text(data.result);
		});
		return false;
	});
});

$(function() {
	$('a#put').bind('click', function() {
		$.getJSON('/todo/api/v1.0/tasks/put/123', function(data) {
			$("#rest_result").text(data.result);
		});

		$("#rest_result").text("PUT server results");
		return false;
	});
});

$(function() {
	$('a#post').bind('click', function() {
		$.getJSON('/todo/api/v1.0/tasks/post', function(data) {
			$("#rest_result").text(data.result);
		});

		$("#rest_result").text("POST server Results");
		return false;
	});
});

$(function() {
	$('a#delete').bind('click', function() {
		$.getJSON('/todo/api/v1.0/tasks/delete', function(data) {
			$("#rest_result").text(data.result);
		});
		return false;
	});
});

$(function() {
	$('a#search').bind('click', function() {
		var userInputValue = $('#searchField').val();
		$.ajax({
  			method: "GET",
  			url: "/nyt/search/data",
  			data: { data: userInputValue }
		})
		.done(function( msg ) {
			$('#rest_result').text(msg.result);
		});
	});
});