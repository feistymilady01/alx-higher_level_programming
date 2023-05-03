$(function(){
    $('INPUT#btn_translate').on('click', function(){
        const trans = $('INPUT#language_code').val();
    })
    $.get('https://www.fourtonfish.com/hellosalut/?lang=' + trans, function(data){
        $('DIV#hello').text(data.hello);
    })
})
