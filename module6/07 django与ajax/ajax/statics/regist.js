$(function () {
    // 鼠标失去焦点校验字符是否已存在
    check_obj = $('input[type="text"]');
    for (var i = 0; i < check_obj.length; i++) {
        $(check_obj[i]).focus(function () {
            $(this).next().text('');
        });
        $(check_obj[i]).blur(function () {
            data_dic = {};
            data_dic.type = this.id;
            data_dic.value = this.value;
            $.ajax({
                url: '/app01/check/',
                type: 'post',
                contentType:"application/json",
                data: JSON.stringify(data_dic),
                success: function (data) {
                    var data_json = JSON.parse(data);
                    console.log(data_json);
                    if (data_json['code'] !== '000000') {
                        type_id = '#' + data_dic.type;
                        $(type_id).next().html(data_json['msg']);
                        console.log(data_json);
                    }
                },
                error: function (err) {
                    console.log(err)
                }
            })
        });
    }

    // 注册逻辑
    $('#btn').click(function (e) {
        e.preventDefault();
        name = $('#name').val().trim();
        nickname = $('#nickname').val().trim();
        phone = $('#phone').val().trim();
        pwd = $('#pwd').val().trim();
        confirm_pwd = $('#confirm_pwd').val().trim();
        if (name && pwd && confirm_pwd && pwd === confirm_pwd) {
            var mydata = {};
            mydata.name = name;
            mydata.nickname = nickname;
            mydata.phone = phone;
            mydata.pwd = pwd;
            mydata.confirm_pwd = confirm_pwd;
            $.ajax({
                url: '',
                type: 'post',
                data: mydata,
                success: function (data) {
                    var data_json = JSON.parse(data);
                    if (data_json['code'] === '000000') {
                        $('.res').addClass('success').html(data_json['msg']);
                        location.href = '/app01/index'
                    } else {
                        $('.res').addClass('error').html(data_json['msg'])
                    }
                },
                error: function (err) {
                    console.log(err)
                }
            })
        } else {
            alert('用户名和密码不能为空,且密码与确认密码一致！')
        }
    });
});