/*
script that adds, removes and clears LI elements from a list when the user clicks:
*/

$('DIV#add_item').css({
  cursor: 'pointer'
});
$('DIV#remove_item').attr('style', 'cursor: pointer;');
$('DIV#clear_list').attr('style', 'cursor: pointer;');
$('DIV#add_item').on('click', () => {
  $('UL.my_list').append('<li>Item</li>');
});

$('DIV#remove_item').on('click', () => {
  $('UL.my_list > li:last').remove();
});

$('DIV#clear_list').on('click', () => {
  $('UL.my_list').empty();
});
