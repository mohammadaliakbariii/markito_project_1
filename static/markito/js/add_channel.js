$(document).ready(function () {
  $(".frm").submit(function (event) {
    var formData = {
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