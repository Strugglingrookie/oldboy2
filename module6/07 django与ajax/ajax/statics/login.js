$(function () {
    $('#btn').click(function (e) {
        e.preventDefault();
        // var formdata = new FormData();  表单数据不可以用 FormData  文件才可以
        var data = {};
        data.name = $('#name').val().trim();
        data.pwd = $('#pwd').val().trim();
        if (formdata.name && formdata.pwd) {
            $.ajax({
                url: '',
                type: 'post',
                data: data,  // ajax默认application/x-www-form-urlencoded格式
                success: function (data) {
                    data = JSON.parse(data);
                    if (data.user) {
                        location.href = '/app01/index'
                    } else {
                        $('.res').html(data.msg)
                    }
                }
            })
        } else {
            alert("用户名或密码不能为空！")
        }
    })

});