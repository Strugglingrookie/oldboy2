$(function () {
    // 登陆逻辑
    $('#btn').click(function (e) {
        e.preventDefault();
        var data = {};
        data.name = $('#name').val().trim();
        data.pwd = $('#pwd').val().trim();
        data.valid_code = $('#valid_code').val().trim();
        data.csrfmiddlewaretoken = $('[name="csrfmiddlewaretoken"]').val().trim();
        if (data.name && data.pwd && data.valid_code) {
            $.ajax({
                url: '',
                type: 'post',
                data: data,
                success: function (data) {
                    console.log(data.user);
                    if (data.user) {
                        location.href = '/app01/index/'
                    } else {
                        $('.error').text(data.msg).css({"color": 'red', 'margin-left': "20px"})
                    }
                },
                error: function (data) {
                    console.log(data)
                }
            })
        } else {
            $('.error').text('用户名或密码或验证码不能为空！').css({"color": 'red', 'margin-left': "20px"})
        }
    });

    // 刷新验证码  src增加一个问号即可
    $('#valid_img').click(function () {
        this.src += '?'
    })
});
