function rollup(id) {
    let inner = $("#eval_step_"+id).find("#inner-contents");
    if ($("#eval_step_"+id).find("#inner-contents").is(":visible")) {
        $(inner).slideUp();
    } else {
        $(inner).slideDown();
    }
}
$(document).ready(function () {
    $('.step-name').each(function () {
        $(this).html($(this).text().trim().replace(/\, /g, "<br>"));
    })
});


