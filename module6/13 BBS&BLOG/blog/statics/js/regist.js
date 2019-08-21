$(function () {
    // 注册逻辑
    $('#btn').click(function (e) {
        e.preventDefault();
        var formdata = new FormData();

        // 一个个手动加
        // formdata.append("name", $('#id_name').val().trim());
        // formdata.append("pwd", $('#id_pwd').val().trim());
        // formdata.append("r_pwd", $('#id_r_pwd').val().trim());
        // formdata.append("email", $('#id_email').val().trim());
        // formdata.append("tel", $('#id_tel').val().trim());
        // formdata.append("csrfmiddlewaretoken", $('[name="csrfmiddlewaretoken"]').val());
        // formdata.append("avatar", $('#avatar')[0].files[0]);

        // 也可以这样简单的加
        var request_data = $("#form").serializeArray();
        $.each(request_data, function (index, data) {
            formdata.append(data.name, data.value)
        });
        formdata.append("avatar", $('#avatar')[0].files[0]);

        $.ajax({
            url: '',
            type: 'post',
            contentType: false,
            processData: false,
            data: formdata,
            success: function (data) {
                if (data.user) {
                    location.href = '/app01/login/'
                } else {
                    // 每次点击显示错误信息之前都删掉上一次的错误信息,清除input红框样式
                    $('span').html('');
                    $('.form-group').removeClass('has-error');
                    // 循环遍历form.errors 将错误信息展示到指定的input标签后面的span标签内
                    $.each(data.msg, function (field, error_list) {
                        if (field === "__all__") {
                            $('#id_r_pwd').next().text(error_list[0]);
                            // 将出错的input标签，边框变红  input标签的父盒子div加上这个类就会变红
                            $('#id_r_pwd').parent().addClass('has-error')
                        } else {
                            $('#id_' + field).next().text(error_list[0]);
                            // 将出错的input标签，边框变红  input标签的父盒子div加上这个类就会变红
                            $('#id_' + field).parent().addClass('has-error')
                        }

                    });
                }
            },
            error: function (data) {
                console.log(data)
            }
        })
    });

    // 点击头像后  头像预览
    $('#avatar').change(function () {
        // 获取用户选中的文件对象
        var file_obj = $(this)[0].files[0];
        if (file_obj) {
            // 获取文件对象路径
            var reader = new FileReader();
            reader.readAsDataURL(file_obj);

            // 修改img的src属性， src=文件对象路径
            reader.onload = function () {
                // 注意需要等reader 加载完才可以修改src，没加载完reader.result还没有值
                $('#avatar_img').attr('src', reader.result)
            };
        }
    })
});
