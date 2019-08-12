$(function () {
    $('#btn').click(function (e) {
        e.preventDefault();
        // var formdata = new FormData();  表单数据不可以用 FormData  文件才可以
        var formdata = {};
        formdata.name = $('#name').val().trim();
        formdata.pwd = $('#pwd').val().trim();
        if (formdata.name && formdata.pwd) {
            $.ajax({
                url: '',
                type: 'post',
                data: formdata,
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