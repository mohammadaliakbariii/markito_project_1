$(document).ready(function () {
  $("form").submit(function (event) {
    var formData = {
      url: $("#url").val(),
      token: $("#token").val(),
    };

    $.ajax({
      type: "POST",
      url: "/get_data/",
      data: formData,
      dataType: "json",
      encode: true,
    }).done(function (data) {
      console.log(data);
    });

    event.preventDefault();
  });
});