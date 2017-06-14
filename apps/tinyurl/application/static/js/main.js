(function($) {
  var form = $("#tiny-url-form");

  form.find("button").click(function() {
    var originalURL = form.find("#originalURL").val();

    $.post("/shorten_url", { original_url: originalURL })
      .done(function(result, status) {
        if (status === "success") {
          var tinyurl = window.location.protocol + "//" + window.location.host + "/urls/" + result.id;
          $("#result").html(tinyurl);
        }
      });
  });
})(window.jQuery);
