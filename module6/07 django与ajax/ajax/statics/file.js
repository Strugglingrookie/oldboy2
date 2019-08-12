$('#ajax_btn').click(function (e) {
    e.preventDefault();
    // 同form表单文件请求一样，原默认的 application/x-www-form-urlencoded 类型不支持文件上传，需要转换请求参数类型
    // 文件必须要以 FormData 数据类型传递
    var formdata = new FormData();
    formdata.append('name', $('#fileajax').val());
    formdata.append('imgfile', $('#ajax_file')[0].files[0]);
    $.ajax({
        url: '',
        type: 'post',
        data: formdata,
        // 传FormData时 必须设置下面两个参数，不给参数，会报错(js非法输入)
        processData: false,    // 不处理数据，让FormData自己去处理数据
        contentType: false,    // 不设置内容类型，让FormData自己设置内容类型
        success: function (data) {
            console.log(data)
        }
    })
});
