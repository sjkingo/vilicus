$('div.summary').click(function() {
    $(this).next().slideToggle();
});

$('a.click-collapse').click(function() {
    $(this).parents('div.detail').slideToggle();
});
