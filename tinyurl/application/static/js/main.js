(function($) {
  var form = $("#tiny-url-form");

  form.find("button").click(function() {
    var originalURL = form.find("#originalURL").val();

    $.post("/shorten_url", { original_url: originalURL })
      .done(function() {
        console.log(arguments);
      });
  });
})(window.jQuery);
