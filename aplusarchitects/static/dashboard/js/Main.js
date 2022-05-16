$(document).ready(function(){
    $('.lang-pick').click((e) => {
        var option = $(e.currentTarget);
        var lang_code = option.data('lang');
        $('#lang-picker input[name="language"]').val(lang_code);
        setTimeout(() => {
          $('#lang-picker').submit();
        }, 200);
    });

    $('.modal-trigger-custom').click((e) => {
        e.preventDefault();
        var target = e.currentTarget;
        $.ajax({
          url: target.dataset.href,
          method: 'GET',
          success: (response) => {
            var modal = $(target.getAttribute('href'));
            modal.html(response).modal('show');
          }
        });
    });
    
    // $('#page-profile .nav-tabs .nav-link').click(function(){
    //     location.hash = $(this).attr('href');
    // });
    
    // var url = document.URL;
    // var hash = url.substring(url.indexOf('#'));
    // $('#page-profile .nav-tabs').find('.nav-item .nav-link').each(function(){
    //     if (hash == $(this).attr('href')) {
    //         $(this).click();
    //     }
    // });
});