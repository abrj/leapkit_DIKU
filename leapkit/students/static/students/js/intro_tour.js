$(document).ready(function() {
    var label = $('label[for="id_title"]');
    label.attr("data-step", "1")
    label.attr("data-intro", "Fields with a * attached to the title are required. These fields must be filled out before uploading the project or saving drafts.");


    var questionmark = $('#id_title_question');
    questionmark.attr("data-step", "2")
    questionmark.attr("data-intro", "Each field has a questionmark attached to its title. Hover over it to get help on what to write.");

    var draft_button = $('#draft_button');
    draft_button.attr("data-step", "3")
    draft_button.attr("data-intro", "Click here to save a draft of your project. Remember that you need to fill in the required fields before the draft can be saved. ");

    var publish_button = $('#publish_button');
    publish_button.attr("data-step", "4")
    publish_button.attr("data-intro", 'Click here to publish your project. It will now be visible to other student users and contact messages will be forwarded to the email you have entered in "Contact email".');
});