/*
script that fetches and prints how to say “Hello” depending on the language
*/

$(document).ready(function () {
  $('INPUT#btn_translate').on('click', function () {
    $.ajax({
      url: 'https://hellosalut.stefanbohacek.dev/',
      dataType: 'json',
      type: 'GET',
      data: { cc: `${$('INPUT#language_code').val()}` },
      success: function (response) {
        $('#hello').html(`${response.hello}`).text();
      },
      error: function (xhr, textStatus, errorThrown) {
        console.error(xhr.status);
      }
    });
  });
});
