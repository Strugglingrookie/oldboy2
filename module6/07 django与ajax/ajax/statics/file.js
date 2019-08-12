$('#ajax_btn').click(function (e) {
    e.preventDefault();
    var formdata = new FormData();
    formdata.append('name', $('#fileajax').val());
    formdata.append('imgfile', $('#ajax_file')[0].files[0]);
    $.ajax({
        url: '',
        type: 'post',
        data: formdata,
        processData: false,    // 不处理数据
        contentType: false,    // 不设置内容类型
        success: function (data) {
            console.log(data)
        }
    })
});
