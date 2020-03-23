// window.onload = function () {
//     var tmp_reg = document.getElementById('btn_reg');
//     var tmp_login = document.getElementById('btn_login');
//     tmp_reg.onclick = function () {
//         window.open('/app01/regist',target='_self')
//     };
//     tmp_login.onclick = function () {
//         window.open('/app01/login',target='_self')
//     }
// };

$(function () {
    $('#btn_reg').click(function () {
            window.open('/app01/regist', target = '_self')
        }
    );
    $('#btn_login').click(function () {
            window.open('/app01/login', target = '_self')
        }
    );
});