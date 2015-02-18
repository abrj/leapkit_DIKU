setTimeout(function () {
    $("#alert-container").remove();
}, 3000);

// Dirty function meant to take the help information and place them as tooltips
$(document).ready(function() {
    $("body").tooltip({ selector: '[data-toggle=tooltip]' });

    if($("form").length > 0) {
            var help_input = $("p.help-block");
            help_input.each(function(i, obj) {

                //Find the help text & remove it from the page
                var help = $( this );
                var help_text = help.text();
                var help_id = help.attr("id").substr(5);
                help.empty();


                //Find the label and set the help text as a tooltip
                var label = $('label[for="' + help_id + '"]');
                var help_tooltip = document.createElement("a");
                help_tooltip.id = help_id + "_question"
                help_tooltip.className = "btn btn-default btn-link";
                help_tooltip.setAttribute("data-toggle", "tooltip");
                help_tooltip.setAttribute("data-placement", "right");
                help_tooltip.setAttribute("title", help_text);
                help_tooltip.innerHTML = "?";
                label.append(help_tooltip);
            });
      }
});

//Add Hover effect to menus
$('ul.nav li.dropdown.user-options').hover(function() {
  $(this).addClass("open");
}, function() {
  $(this).removeClass("open");
});