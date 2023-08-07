$(document).ready(function () {
  function fetchTranslation () {
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
  }

  $('input#btn_translate').on('click', function () {
    fetchTranslation();
  });

  $('#language_code').on('keypress', function (event) {
    if (event.key === 'Enter') {
      fetchTranslation();
    }
  });
});
