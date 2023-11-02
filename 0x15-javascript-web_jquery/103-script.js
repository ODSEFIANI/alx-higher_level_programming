$(document).ready(function () {
  $('#btn_translate').click(function () {
    const lang = $('input#language_code').val();
    const url = 'https://hellosalut.stefanbohacek.dev/?lang=' + lang;
    $.get(url, function (data) {
      $('div#hello').text(data.hello);
    });
  });

  $('#language_code').keyup(function (event) {
    if (event.keyCode === 13) {
      const lang = $('input#language_code').val();
      const url = 'https://hellosalut.stefanbohacek.dev/?lang=' + lang;
      $.get(url, function (data) {
        $('div#hello').text(data.hello);
      });
    }
  });
});

