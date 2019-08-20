$(function () {
   // 注册逻辑
   $('#btn').click(function (e) {
       e.preventDefault();
       var formdata = new FormData();
       formdata.append("name", $('#id_name').val().trim());
       formdata.append("pwd", $('#id_pwd').val().trim());
       formdata.append("r_pwd", $('#id_r_pwd').val().trim());
       formdata.append("email", $('#id_email').val().trim());
       formdata.append("tel", $('#id_tel').val().trim());
       formdata.append("avatar", $('#avatar')[0].files[0]);
       formdata.append("csrfmiddlewaretoken", $('[name="csrfmiddlewaretoken"]').val());

       if(formdata.name && formdata.pwd && formdata.r_pwd && formdata.email && formdata.tel){
           $.ajax({
               url:'',
               type:'post',
               contentType:false,
               processData:false,
               data:formdata,
               success:function (data) {
                   console.log(data.user);
                   if(data.msg){
                       $('.error').text(data.msg).css({"color":'red', 'margin-left':"20px"})
                   }else{
                       location.href='/app01/login/'
                   }
               },
               error:function (data) {
                   console.log(data)
               }
           })
       }else{
           $('.error').text('所有项均为必填！').css({"color":'red', 'margin-left':"20px"})
       }
   });

    // 图片预览
    $('#avatar').change(function () {
        // 获取用户选中的文件对象
        var file_obj = $(this)[0].files[0];

        // 获取文件对象路径
        var reader = new FileReader();
        reader.readAsDataURL(file_obj);

        // 修改img的src属性， src=文件对象路径
        reader.onload = function () {
            // 注意需要等reader 加载完才可以修改src，没加载完reader.result还没有值
            $('#avatar_img').attr('src', reader.result)
        };
    })
});
