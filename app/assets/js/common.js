$(function(){
    $('.poll button').click(function(){
        $.ajax({
            type: 'PUT',
            url: '/poll',
            data: {'value': $(this).attr('value')}
        });
    });
});
