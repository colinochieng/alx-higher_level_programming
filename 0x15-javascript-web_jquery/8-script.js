/*
 script that fetches and lists the title for all movies by using this URL:
 https://swapi-api.alx-tools.com/api/films/?format=json
*/

$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data, status) {
  $(data.results).each(function (index, element) {
    $('UL#list_movies').append('<li>' + element.title + '</li>');
  });
});
