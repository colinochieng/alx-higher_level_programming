/* script that updates the text color of the <header>
element to red (#FF0000) when the user clicks on the tag DIV#red_header Using vanilla Js */

document.querySelector('DIV#red_header').style.cursor = 'pointer';
document.querySelector('DIV#red_header').addEventListener('click', () => {
  document.querySelector('header').style.color = '#FF0000';
});
