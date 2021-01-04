$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-alvo .modal-content").html("");
        $("#modal-alvo").modal("show");
      },
      success: function (data) {
        $("#modal-alvo .modal-content").html(data.html_form);
      }
    });
  };

  var saveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#alvo-table tbody").html(data.html_alvo_list);
          $("#modal-alvo").modal("hide");
        }
        else {
          $("#modal-alvo .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create alvo
  $(".js-create-alvo").click(loadForm);
  $("#modal-alvo").on("submit", ".js-alvo-create-form", saveForm);

  // Update alvo
  $("#alvo-table").on("click", ".js-update-alvo", loadForm);
  $("#modal-alvo").on("submit", ".js-alvo-update-form", saveForm);

  // Delete alvo
  $("#alvo-table").on("click", ".js-delete-alvo", loadForm);
  $("#modal-alvo").on("submit", ".js-alvo-delete-form", saveForm);

});

