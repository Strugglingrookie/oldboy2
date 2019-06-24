/*
alert("123");  // 弹出警告框
console.log("123456");  // 控制台输出
var a=100; // 变量申明

// 基本数据类型
// 数值类型:number  （如果一个变量中，存放了数字，那么这个变量就是数值型的）
console.log(typeof(a)); //使用typeof函数检测变量a的数据类型  number 类型
var b=a/0;
console.log(b);  //Infinit特殊情况，无限大
*/

var jsonStr = '{"name":"xg","pwd":123456}';
var jsonObj=JSON.parse(jsonStr);
// var jsonObj1=jQuery.packJSON(jsonStr);
var jsonNewStr=JSON.stringify(jsonObj);
console.log(jsonObj);
console.log(typeof jsonObj);
console.log(typeof jsonStr);
console.log(typeof jsonNewStr);
// console.log(typeof jsonObj1);
for (var k in jsonObj){
    console.log(k,jsonObj[k]);
}

