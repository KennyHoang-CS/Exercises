$('#submit').on('click', function(){
    let title = $('#title').val();
    let ratings = $('#ratings').val();

    $('#titles-container').append($('<p>', {text: title}));
    $('#ratings-container').append($('<p>', {text: ratings}));
    let x = 'X';
    $('#delete-container').append($('<button>', {text: x}));
})

$('#delete-container').on('click', 'button', function(){
    let rmIndex = $(this).index() - 1;
    $('#titles-container p').eq(rmIndex).remove();
    $('#ratings-container p').eq(rmIndex).remove();
    $('#delete-container button').eq(rmIndex).remove();
})