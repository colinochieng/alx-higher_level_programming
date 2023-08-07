/*
script that fetches from https://fourtonfish.com/hellosalut/?lang=fr
and displays the value of hello from that fetch in the HTML tag DIV#hello.
*/

$.ajax({
  url: 'https://fourtonfish.com/hellosalut/?lang=fr',
  type: 'Get',
  dataType: 'json',
  success: (response) => {
    $('DIV#hello').text(response.hello);
  },
  error: function (xhr, textStatus, errorThrown) {
    $('DIV#hello').text(textStatus);
  }
});
