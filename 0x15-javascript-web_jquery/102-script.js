$(document).ready(function () {
  $('#btn_translate').click(function () {
    const lang = $('INPUT#language_code').val();
    let url = 'https://hellosalut.stefanbohacek.dev/?lang=' + lang;
    $.get(url, function (data, textStatus, jqXHR) {
      $('DIV#hello').text(data.hello);
    });
  });
});
