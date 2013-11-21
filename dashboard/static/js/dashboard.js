$('div.summary').click(function() {
    $(this).next().slideToggle();
    $(this).toggleClass('selected');
});

$('a.click-collapse').click(function() {
    $(this).parents('div.detail').slideToggle();
});
