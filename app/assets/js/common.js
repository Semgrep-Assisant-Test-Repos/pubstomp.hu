$(function(){
    $('.poll button').click(function(){
        $.ajax({
            type: 'PUT',
            url: '/poll',
            data: {'value': $(this).attr('value')}
        });
        $('.confirmation-message').addClass($(this).attr('value'))
        ga('send', 'event', 'poll', 'vote', $(this).attr('value'));
    });
    $('.poll .change').click(function(){
        $('.confirmation-message').removeClass('no maybe yes')
        ga('send', 'event', 'poll', 'change');
    });
});
