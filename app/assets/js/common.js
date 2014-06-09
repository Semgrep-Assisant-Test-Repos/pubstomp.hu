$(function(){
    $('.poll button').click(function(){
        $.ajax({
            type: 'PUT',
            url: '/poll',
            data: {'value': $(this).attr('value')}
        });
        $('.confirmation-message').addClass($(this).attr('value'))
    });
    $('.poll .change').click(function(){
        $('.confirmation-message').removeClass('no maybe yes')
    });
});
