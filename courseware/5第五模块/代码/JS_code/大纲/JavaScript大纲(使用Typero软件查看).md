###  javascript简介

web前端有三层：

- HTML:从语义的角度，描述页面的结构
- CSS:从审美的角度，描述样式（美化页面）
- JavaScript：从交互的角度，描述行为（提升用户体验）



#### 历史背景介绍

布兰登 艾奇  1995年在网景公司 发明的JavaScript

一开始的JavaScrip叫LiveScript

同一个时期  比如 VBScript,JScript等，但是后来被JavaScript打败了，**现在的浏览器只运行一种脚本语言叫JavaScript**

#### JavaScript的发展

**2003**年之前，JavaScript被认为“牛皮鲜”，用来制作页面上的广告，弹窗、漂浮的广告。什么东西让人烦，什么东西就是JavaScript开发的。所以浏览器就推出了屏蔽广告功能。

**2004**年，JavaScript命运开始改变，那一年，**谷歌公司开始带头使用Ajax技术**，Ajax技术就是JavaScript的一个应用。并且，那时候人们逐渐开始提升用户体验了。Ajax有一些应用场景。比如，当我们在百度搜索框搜文字时，输入框下方的智能提示，可以通过Ajax实现。比如，当我们注册网易邮箱时，能够及时发现用户名是否被占用，而不用调到另外一个页面。

**2007**年乔布斯发布了第一款iPhone，这一年开始，用户就多了上网的途径，就是用移动设备上网。
**JavaScript在移动页面中，也是不可或缺的**。并且这一年，互联网开始标准化，按照W3C规则三层分离，JavaScript越来越被重视。

**2010**年，人们更加了解**HTML5技术**，**HTML5推出了一个东西叫做Canvas**（画布），工程师可以在Canvas上进行游戏制作，利用的就是JavaScript。

**2011**年，**Node.js诞生**，使JavaScript能够开发服务器程序了。

React-native inoic

如今，**WebApp**已经非常流行，就是用**网页技术开发手机应用**。手机系统有iOS、安卓。比如公司要开发一个“携程网”App，就需要招聘三队人马，比如iOS工程师10人，安卓工程师10人，前端工程师10人。共30人，开发成本大；而且如果要改版，要改3个版本。现在，假设公司都用web技术，用html+css+javascript技术就可以开发App。也易于迭代（网页一改变，所有的终端都变了）。

虽然目前WebApp在功能和性能上的体验远不如Native App，但是“WebApp慢慢取代Native App”很有可能是未来的趋势。

#### JavaScript的组成

- ECMAScript 5.0:定义了js的语法标准： 包含变量 、表达式、运算符、函数、if语句 for循环 while循环、内置的函数
- DOM :操作网页上元素的API。比如让盒子显示隐藏、变色、动画  form表单验证
- BOM:操作浏览器部分功能的API。比如刷新页面、前进后退、让浏览器自动滚动

### ECMAScript 5.0

####  js的引入方式

-  内接式

```html
<script type="text/javascript">

</script>
```

- 外接式

```html
<!--相当于引入了某个模块-->
<script type="text/javascript" src = './index.js'></script>
```

#### 注释

```单行注释的快捷键ctrl+/.多行注释的快捷键是ctrl+shift+/```

#### 调试语句

- alert(''); 弹出警告框
- console.log('');  控制台输出



#### 变量的声明

在js中使用var关键字 进行变量的声明,注意 分号作为一句代码的结束符

```javascript
var a = 100;
```

- 定义变量：var就是一个**关键字**，用来定义变量。所谓关键字，就是有特殊功能的小词语。关键字后面一定要有空格隔开。
- 变量的赋值：等号表示**赋值**，将等号右边的值，赋给左边的变量。
- 变量名：我们可以给变量任意的取名字。

变量要先定义，才能使用。比如，我们不设置变量，直接输出：

```html
 <script type="text/javascript">
        console.log(a);
  </script>
```

控制台将会报错：

![img](https://images2018.cnblogs.com/blog/1364810/201805/1364810-20180526102920462-1087853951.png)

正确写法：

```javascript
var a; //先定义
a = 100; // 后赋值

//也可以直接定义变量+赋值
var a = 100;
```

#### 变量的命名规范

变量名有命名规范：只能由**英语字母、数字、下划线、美元符号$**构成，且不能以数字开头，并且不能是JavaScript保留字。

下列的单词叫做保留字，就是说不允许当做变量名，不用记：

```javascript
bstract、boolean、byte、char、class、const、debugger、double、enum、export、extends、final、float、goto
implements、import、int、interface、long、native、package、private、protected、public、short、static、super、synchronized、throws、transient、volatile
```

#### 基本数据类型

##### 数值类型:number

 如果一个变量中，存放了数字，那么这个变量就是数值型的

```javascript
    var a = 100;            //定义了一个变量a，并且赋值100
    console.log(typeof a);  //输出a变量的类型 使用typeof函数 检测变量a的数据类型
    //特殊情况
    var b = 5/0;
	console.log(b); //Infinity 无限大
    console.log(typeof b); //number 类型
```

ps:**在JavaScript中，只要是数，就是数值型(number)的**。无论整浮、浮点数（即小数）、无论大小、无论正负，都是number类型的。

##### 字符串类型:string

```javascript
var a = "abcde";
var b = "路飞";
var c = "123123";
var d = "哈哈哈哈哈";
var e = "";     //空字符串
```

###### 连字符和+号的区别

键盘上的`+`可能是连字符，也可能是数字的加号。如下：

```javascript
console.log("我" + "爱" + "你");   //连字符，把三个独立的汉字，连接在一起了
console.log("我+爱+你");           //原样输出
console.log(1+2+3);             //输出6
```

**总结**：如果加号两边**都是**数值，此时是加。否则，就是连字符（用来连接字符串）。

##### 布尔类型：boolean

```javascript
var isShow = false;
console.log(typeof b1);
```

##### 空对象：null

```javascript
var c1 = null;//空对象. object
console.log(typeof c1);
```

##### 未定义：undefined

```javascript
var d1;
//表示变量未定义
console.log(typeof d1);
```

#### 复杂（引用）数据类型

#####   Function

#####  Object

#####  Arrary

#####  String

#####  Date 

后面课程讲解

#### 运算符

##### 赋值运算符

以var x = 12,y=5来演示示例

![img](https://images2018.cnblogs.com/blog/1364810/201805/1364810-20180527110502282-357921689.png)



##### 算数运算符

var a = 5,b=2;

![img](https://images2018.cnblogs.com/blog/1364810/201805/1364810-20180527110542094-803310766.png)

##### 比较运算符

var x = 5;

![img](https://images2018.cnblogs.com/blog/1364810/201805/1364810-20180527110620741-188424489.png)

#### 数据类型转换

##### 将number类型转换成string类型

###### 隐式转换

```javascript
var n1 = 123;
var n2 = '123';
var n3 = n1+n2;
// 隐式转换
console.log(typeof n3);
```

###### 强制转换

```javascript
// 强制类型转换String(),toString()
var str1 = String(n1);
console.log(typeof str1);

var num = 234;
console.log(num.toString())
```

##### 将string类型转换成number类型

```javascript
var  stringNum = '789.123wadjhkd';
var num2 =  Number(stringNum);
console.log(num2); //NaN  Not a Number 但是一个number类型

// parseInt()可以解析一个字符串 并且返回一个整数
console.log(parseInt(stringNum))； //789
console.log(parseFloat(stringNum)); //789.123
```

##### 任何的数据类型都可以转换为boolean类型

```javascript
var b1 = '123'; //true
var b2 = 0; //false
var b3 = -123 //true
var b4 = Infinity; //true
var b5 = NaN; //false
var b6; //false
var b7 = null; //false
//使用Boolean(变量) 来查看当前变量的真假
```

#### 流程控制

##### if

```javascript
var age = 20;
if(age>18){
    //{}相当于作用域
	console.log('可以去会所');
}
alert('alex'); //下面的代码照样执行
```

##### if-else

```javascript
var age = 20;
if(age>18){
    //{}相当于作用域
	console.log('可以去会所');
}else{
    console.log('好好学js,年纪够了再去会所');
}
alert('alex'); //下面的代码照样执行
```

##### if-else if -else

```javascript
var age = 18;
if(age==18){
    //{}相当于作用域
	console.log('可以去会所');
}else if(age==30){
    console.log('该娶媳妇了！！');
}else{
    console.log('随便你了')
}
alert('alex'); //下面的代码照样执行
```

##### 逻辑与&&、 逻辑或||

```javascript
//1.模拟  如果总分 >400 并且数学成绩 >89分 被清华大学录入
//逻辑与&& 两个条件都成立的时候 才成立
if(sum>400 && math>90){
    console.log('清华大学录入成功')
}else{
    alert('高考失利')
}
```

```javascript
//2.模拟 如果总分>400 或者你英语大于85 被复旦大学录入
//逻辑或  只有有一个条件成立的时候 才成立
if(sum>500 || english>85){
    alert('被复旦大学录入')
}else{
    alert('高考又失利了')
}
```

##### switch 语句

```javascript
var gameScore = 'better';

switch(gameScore){

//case表示一个条件 满足这个条件就会走进来 遇到break跳出。break终止循环。如果某个条件中不写 break，那么直到该程序遇到下一个break停止
    case 'good':
    console.log('玩的很好')
    //break表示退出
    break;
    case  'better':
    console.log('玩的老牛逼了')
    break;
    case 'best':
    console.log('恭喜你 吃鸡成功')
    break;

    default:
    console.log('很遗憾')

}
//注意：switch相当于if语句 但是玩switch的小心case穿透
```

##### while循环

给大家总结了循环三步走，任何语言的循环离不开这三步：

1. 初始化循环变量
2. 判断循环条件
3. 更新循环变量

```javascript
// 例子：打印 1~9之间的数
var i = 1; //初始化循环变量

while(i<=9){ //判断循环条件
    console.log(i);
    i = i+1; //更新循环条件
}
```

练习：将1~100所有是2的倍数在控制台打印。使用while循环

```javascript
var i = 1;
while(i <= 100){
    if(i%2==0){
        console.log(i);
    }
    i +=1;
}
```

##### do-while循环 

用途不大：就是先做一次 ，上来再循环

```javascript
//不管有没有满足while中的条件do里面的代码都会走一次
var i = 3;//初始化循环变量
do{

    console.log(i)
    i++;//更新循环条件

}while (i<10) //判断循环条件
```

##### for循环

for循环遍历列表是最常用的对数据的操作，在js中希望大家熟练使用for循环的书写方式

```javascript
//输出1~10之间的数
for(var i = 1;i<=10;i++){
     console.log(i)
 }
```

课堂练习：输入1~100之间所有数之和

```javascript
var sum = 0;
for(var j = 1;j<=100;j++){
    sum = sum+j
}
console.log(sum);
```

##### for循环嵌套的练习

document.write('*'); 往浏览器文档中写*

```javascript
for(var i=1;i<=3;i++){
            
 　　for(var j=0;j<6;j++){
        document.write('*')
    }
            
   document.write('<br>')
 }
```

小作业：

1.在浏览器中输出直角三角形

```html
*  
** 
***
****
*****
******
```

代码：

```javascript
for(var i=1;i<=6;i++){ //控制的行数
   for(var j=1;j<=i;j++){ //控制的*
      　　document.write("*")；
   }
                
     document.write('<br>')；
}
```

2.在浏览器中输出 等腰三角形

```html
 		 *  
		***  
        ***** 
       ******* 
      ********* 
     *********** 
```

代码：

```javascript
    for(var i=1;i<=6;i++){ //控制行数，一共显示6行 记得换行document.write('<br>');

        //控制我们的空格数
        for(var s=i;s<6;s++){
            document.write('&nbsp;');
        }
        //控制每行的输出*数
        for(var j=1;j<=2*i-1;j++){
            document.write('*');
        }
        document.write('<br>');

   }
            
```



#### 常用内置对象（复杂数据类型）

所谓内置对象就是ECMAScript提供出来的一些对象，我们知道对象都是有相应的属性和方法,jie'xi'lai

##### 数组Array

###### 字面量方式创建（推荐大家使用这种方式，简单粗暴）

```javascript
var colors = ['red','green','yellow'];
```

###### 使用构造函数（后面会讲）的方式创建 使用new关键词对构造函数进行创建对象,构造函数与后面的面向对象有关系

```javascript
var colors = new Array();
//通过下标进行赋值
colors[0] = 'red';
colors[1] = 'green';
colors[2] = 'yellow';
console.log(colors);
```

###### 数组的常用方法

![img](https://images2018.cnblogs.com/blog/1364810/201805/1364810-20180527115412171-47405715.png)

- 数组的合并 concat()

```javascript
var north = ['北京','山东','天津'];
var south = ['东莞','深圳','上海'];
        
var newCity = north.concat(south);
console.log(newCity)
```

- join() 将数组中元素使用指定的字符串连接起来，它会形成一个新的字符串

```javascript
var score = [98,78,76,100,0];
var str = score.join('|');
console.log(str);//"98|78|76|100|0"
```

- slice(start,end); 返回数组的一段记录，顾头不顾尾

```javascript
var arr = ['张三','李四','王文','赵六'];
var newArr  = arr.slice(1,3);
console.log(newArr);//["李四", "王文"]
```



- pop 移除数组的最后一个元素

```javascript
var arr = ['张三','李四','王文','赵六'];
arr.pop();
console.log(arr);//["张三", "李四"，"王文"]
```

- push() 向数组最后添加一个元素

```javascript
var arr = ['张三','李四','王文','赵六'];
arr.push('小马哥');
console.log(arr);//["张三", "李四"，"王文"，"赵六"，"小马哥"]
```

- reverse() 翻转数组

```javascript
var names = ['alex','xiaoma','tanhuang','angle'];
//4.反转数组
names.reverse();
console.log(names);
```

- sort对数组排序

```javascript
var names = ['alex','xiaoma','tanhuang','abngel'];
names.sort();
console.log(names)；// ["alex", "angle", "tanhuang", "xiaoma"]
```

- 判断是否为数组：isArray()

```
 布尔类型值 = Array.isArray(被检测的值) ;
```

##### 字符串string

![img](https://images2018.cnblogs.com/blog/1364810/201805/1364810-20180527115519670-1394154604.png)

-  chartAt() 返回指定索引的位置的字符

```javascript
var str = 'alex';
var charset = str.charAt(1);
console.log(charset);//l
```

-  concat 返回字符串值，表示两个或多个字符串的拼接

```javascript
var str1 = 'al';
var str2  = 'ex';
console.log(str1.concat(str2,str2));//alexex
```

-  replace(a,b) 将字符串a替换成字符串b

```javascript
var a = '1234567755';
var newStr = a.replace("4567","****");
console.log(newStr);//123****755
```

-  indexof() 查找字符的下标，如果找到返回字符串的下标，找不到则返回-1 。跟seach()方法用法一样

```javascript
var str = 'alex';
console.log(str.indexOf('e'));//2
console.log(str.indexOf('p'));//-1
```

-  slice(start，end) 左闭右开 分割字符串

```javascript
var str = '小马哥';
console.log(str.slice(1,2));//马
```

-  split('a',1) 以字符串a分割字符串，并返回新的数组。如果第二个参数没写，表示返回整个数组，如果定义了个数，则返回数组的最大长度

```javascript
var  str =  '我的天呢,a是嘛,你在说什么呢?a哈哈哈';
console.log(str.split('a'));//["我的天呢,", "是嘛,你在说什么呢?", "哈哈哈"]
```

- substr(statr,end) 左闭右开

```javascript
var  str =  '我的天呢,a是嘛,你在说什么呢?a哈哈哈';
console.log(str.substr(0,4));//我的天呢
```

- toLowerCase()转小写

```javascript
var str = 'XIAOMAGE';
console.log(str.toLowerCase())；//xiaomage
```

- toUpperCase()转大写

```javascript
var str = 'xiaomage';
console.log(str.toUpperCase());//XIAOMAGE
```

特别：

```javascript
//1.将number类型转换成字符串类型
var num = 132.32522;
var numStr = num.toString()
console.log(typeof numStr)
//四舍五入
var newNum = num.toFixed(2)
console.log(newNum)
```

##### Math内置对象

![img](https://images2018.cnblogs.com/blog/1364810/201805/1364810-20180527115730266-1931075271.png)

- Math.ceil() 向上取整，'天花板函数'

```javascript
var x = 1.234;
//天花板函数  表示大于等于 x，并且与它最接近的整数是2
var a = Math.ceil(x);
console.log(a);//2
```

- Math.floor 向下取整，'地板函数'

```javascript
var x = 1.234;
// 小于等于 x，并且与它最接近的整数 1
var b = Math.floor(x);
console.log(b);//1
```

- 求两个数的最大值和最小值

```javascript
//求 两个数的最大值 最小值
console.log(Math.max(2,5));//5
console.log(Math.min(2,5));//2
```

- 随机数 Math.random()

```javascript
var ran = Math.random();
console.log(ran);[0,1)
```

如果让你取100-200之间的随机数，怎么做？

背过公式：min - max之间的随机数： min+Math.random()*(max-min);

#### 函数

函数：就是把将一些语句进行封装，然后通过调用的形式，执行这些语句。

函数的作用：

- 解决大量的重复性的语句
- 简化编程，让编程模块化

```python
# python 中声明函数
def add(x,y):
    return x+y

# 调用函数
print(add(1,2))
    
```

```javascript
//js中声明函数
function add(x,y){
    return x+y;
}
//js中调用函数
console.log(add(1,2));
```

解释如下：

- function：是一个关键字。中文是“函数”、“功能”。
- 函数名字：命名规定和变量的命名规定一样。只能是字母、数字、下划线、美元符号，不能以数字开头。
- 参数：后面有一对小括号，里面是放参数用的。
- 大括号里面，是这个函数的语句。

  

#### 伪数组 arguments

arguments代表的是实参。有个讲究的地方是：arguments**只在函数中使用**。

```javascript
    fn(2,4);
    fn(2,4,6);
    fn(2,4,6,8);

    function fn(a,b,c) {
        console.log(arguments);
        console.log(fn.length);         //获取形参的个数
        console.log(arguments.length);  //获取实参的个数

        console.log("----------------");
    }
```

结果：

![img](https://images2018.cnblogs.com/blog/1364810/201805/1364810-20180528211812538-79786405.png)

（2）之所以说arguments是伪数组，是因为：**arguments可以修改元素，但不能改变数组的长短**。举例：

```javascript
    fn(2,4);
    fn(2,4,6);
    fn(2,4,6,8);

    function fn(a,b) {
        arguments[0] = 99;  //将实参的第一个数改为99
        arguments.push(8);  //此方法不通过，因为无法增加元素
    }
```

清空数组的几种方式：

```javascript
   var array = [1,2,3,4,5,6];
    array.splice(0);      //方式1：删除数组中所有项目
    array.length = 0;     //方式2：length属性可以赋值，在其它语言中length是只读
    array = [];           //方式3：推荐
```





#### 对象Object

1.使用Object或对象字面量创建对象

2.工厂模式创建对象

3.构造函数模式创建对象

4.原型模式创建对象

##### 使用Object或字面量方式创建对象

JS中最基本创建对象的方式：

```javascript
var student = new Object();
student.name = "easy";
student.age = "20";
```

这样，一个student对象就创建完毕，拥有2个属性`name`以及`age`，分别赋值为`"easy"`和`20`。

 如果你嫌这种方法有一种封装性不良的感觉。来一个对象字面量方式创建对象。

```javascript
var sutdent = {
  name : "easy",
  age : 20
};
```

这样看起来似乎就完美了。但是马上我们就会发现一个十分尖锐的问题：当我们要创建同类的student1，student2，…，studentn时，我们不得不将以上的代码重复n次....

```javascript
var sutdent1 = {
  name : "easy1",
  age : 20
};

var sutdent2 = {
  name : "easy2",
  age : 20
};

...

var sutdentn = {
  name : "easyn",
  age : 20
};
```

有个提问？能不能像工厂车间那样，有一个车床就不断生产出对象呢？我们看”工厂模式”。

##### 工厂模式创建对象

JS中没有类的概念，那么我们不妨就使用一种函数将以上对象创建过程封装起来以便于重复调用，同时可以给出特定接口来初始化对象

```javascript
function createStudent(name, age) {
  var obj = new Object();
  obj.name = name;
  obj.age = age;
  return obj;
}

var student1 = createStudent("easy1", 20);
var student2 = createStudent("easy2", 20);
...
var studentn = createStudent("easyn", 20);
```

这样一来我们就可以通过createStudent函数源源不断地”生产”对象了。看起来已经高枕无忧了，但贪婪的人类总有不满足于现状的天性：我们不仅希望”产品”的生产可以像工厂车间一般源源不断，我们还想知道生产的产品究竟是哪一种类型的。

比如说，我们同时又定义了”生产”水果对象的createFruit()函数：

```javascript
function createFruit(name, color) {
  var obj = new Object();
  obj.name = name;
  obj.color = color;
  return obj;
}

var v1 = createStudent("easy1", 20);
var v2 = createFruit("apple", "green");
```

对于以上代码创建的对象v1、v2，我们用instanceof操作符去检测，他们统统都是Object类型。我们的当然不满足于此，我们希望v1是Student类型的，而v2是Fruit类型的。为了实现这个目标，我们可以用自定义构造函数的方法来创建对象

##### 构造函数模式创建对象

在上面创建Object这样的原生对象的时候，我们就使用过其构造函数：

```
var obj = new Object();

```

在创建原生数组Array类型对象时也使用过其构造函数：

 

```
var arr = new Array(10);  //构造一个初始长度为10的数组对象

```

在进行自定义构造函数创建对象之前，我们首先了解一下`构造函数`和`普通函数`有什么区别。

1、实际上并不存在创建构造函数的特殊语法，其与普通函数唯一的区别在于调用方法。对于任意函数，使用new操作符调用，那么它就是构造函数；不使用new操作符调用，那么它就是普通函数。

2、按照惯例，我们约定构造函数名以大写字母开头，普通函数以小写字母开头，这样有利于显性区分二者。例如上面的new Array()，new Object()。

3、使用new操作符调用构造函数时，会经历(1)创建一个新对象；(2)将构造函数作用域赋给新对象（使this指向该新对象）；(3)执行构造函数代码；(4)返回新对象；4个阶段。

ok，了解了`构造函数`和`普通函数`的区别之后，我们使用构造函数将`工厂模式`的函数重写，并添加一个方法属性： 

```javascript
function Student(name, age) {
  this.name = name;
  this.age = age;
  this.alertName = function(){
    alert(this.name)
  };
}

function Fruit(name, color) {
  this.name = name;
  this.color = color;
  this.alertName = function(){
    alert(this.name)
  };
}
```

这样我们再分别创建Student和Fruit的对象：

```javascript
var v1 = new Student("easy", 20);
var v2 = new Fruit("apple", "green");
```

这时我们再来用instanceof操作符来检测以上对象类型就可以区分出Student以及Fruit了：

```javascript
alert(v1 instanceof Student);  //true
alert(v2 instanceof Student);  //false
alert(v1 instanceof Fruit);  //false
alert(v2 instanceof Fruit);  //true

alert(v1 instanceof Object);  //true 任何对象均继承自Object
alert(v2 instanceof Object);  //true 任何对象均继承自Object
```

这样我们就解决了`工厂模式`无法区分对象类型的尴尬。那么使用构造方法来创建对象是否已经完美了呢？使用构造器函数通常在js中我们来创建对象。

我们会发现Student和Fruit对象中共有同样的方法，当我们进行调用的时候这无疑是内存的消耗。

我们完全可以在执行该函数的时候再这样做，办法是将对象方法移到构造函数外部：

```javascript
function Student(name, age) {
  this.name = name;
  this.age = age;
  this.alertName = alertName;
}

function alertName() {
  alert(this.name);
}

var stu1 = new Student("easy1", 20);
var stu2 = new Student("easy2", 20);
```

在调用stu1.alertName()时，this对象才被绑定到stu1上。

我们通过将alertName()函数定义为全局函数，这样对象中的alertName属性则被设置为指向该全局函数的指针。由此stu1和stu2共享了该全局函数，解决了内存浪费的问题

但是，通过全局函数的方式解决对象内部共享的问题，终究不像一个好的解决方法。如果这样定义的全局函数多了，我们想要将自定义对象封装的初衷便几乎无法实现了。更好的方案是通过原型对象模式来解决。

##### 原型的模式创建对象

原型链甚至原型继承，是整个JS中最难的一部分也是最不好理解的一部分，在这里由于我们课程定位的原因，如果对js有兴趣的同学，可以去查阅一下相关JS原型的一些知识点。

```javascript
function Student() {
    this.name = 'easy';
    this.age = 20;
}


Student.prototype.alertName = function(){
    alert(this.name);
};

var stu1 = new Student();
var stu2 = new Student();

stu1.alertName();  //easy
stu2.alertName();  //easy

alert(stu1.alertName == stu2.alertName);  //true 二者共享同一函数
```

#### Date日期对象

创建日期对象只有构造函数一种方式，使用new关键字

```javascript
//创建了一个date对象
var myDate = new Date();
```

![img](https://images2018.cnblogs.com/blog/1364810/201805/1364810-20180527115655555-1984356276.png)



```javascript
//返回本地时间
console.log(myDate().toLocalString());
```

#### JSON

##### 概念简介

JSON(JavaScript Object Notation) 是一种轻量级的数据交换格式，采用完全独立于语言的文本格式，是理想的数据交换格式。同时，JSON是 JavaScript 原生格式，这意味着在 JavaScript 中处理 JSON数据不须要任何特殊的 API 或工具包。

在JSON中，有两种结构：对象和数组。

- 对象

```json
var packJSON= {"name":"alex", "password":"123"};
```

一个对象以“{”开始，“}”结束，“key/value”之间运用 “,”分隔。

- 数组

```json
var packJSON = [{"name":"alex", "password":"123"}, {"name":"wusir", "password":"456"}];
```

数组是值的有序集合。一个数组以“[”开始，“]”结束。值之间运用 “,”分隔。

##### JSON对象和JSON字符串转换

在数据传输过程中，JSON是以字符串的形式传递的，而JS操作的是JSON对象，所以，JSON对象和JSON字符串之间的相互转换是关键。例如：

- JSON字符串:

```javascript
var jsonStr ='{"name":"alex", "password":"123"}' ;
```

- JSON对象：

```javascript
var jsonObj = {"name":"alex", "password":"123"};
```

1. JSON字符串转换JSON对象

```javascript
var jsonObject= jQuery.parseJSON(jsonstr);
```

2. JSON对象转化JSON字符串

```javascript
var jsonstr =JSON.stringify(jsonObject );
```

##### 遍历JSON对象和JSON数组

1. 遍历JSON对象代码如下：

```javascript
var packAlex  = {"name":"alex", "password":"123"} ;
 
for(var k in packAlex ){//遍历packAlex 对象的每个key/value对,k为key
   alert(k + " " + packAlex[k]);
}

```

2. 遍历JSON数组代码如下

```javascript
var packAlex = [{"name":"alex", "password":"123"}, {"name":"wusir", "password":"456"}];
 
for(var i in packAlex){//遍历packJson 数组时，i为索引
   alert(packAlex[i].name + " " + packAlex[i].password);
}
```









### DOM

##### 概念

所谓DOM,全称 Docuemnt Object Model 文档对象模型，毫无疑问，此时要操作对象，什么对象？文档对象

在文档中一切皆对象，比如html,body,div,p等等都看做对象，那么我们如何来点击某个盒子让它变色呢？

DOM 为文档提供了结构化表示，并定义了如何通过脚本来访问文档结构。目的其实就是为了能让js操作html元素而制定的一个规范。

##### 解析过程

HTML加载完毕，渲染引擎会在内存中把HTML文档，生成一个DOM树，getElementById是获取内中DOM上的元素节点。然后操作的时候修改的是该元素的**属性**。

##### DOM树（一切皆是节点）

![img](https://images2018.cnblogs.com/blog/1364810/201805/1364810-20180528220440235-730879308.png)

上图可知，**在HTML当中，一切都是节点**：（非常重要）

- **元素节点**：HMTL标签。
- **文本节点**：标签中的文字（比如标签之间的空格、换行）
- **属性节点**：：标签的属性

整个html文档就是一个文档节点。所有的节点都是Object。

##### DOM可以做什么

- 找对象（元素节点）
- 设置元素的属性值
- 设置元素的样式
- 动态创建和删除元素
- 事件的触发响应：事件源、事件、事件的驱动程序

##### 清楚DOM的结构

- 获取文档对象：document
- 获取html：document.documentElement
- 获取body:  document.body

##### 获取其它DOM（事件源）的三种方式

```javascript
var oDiv1 = document.getElementById("box1");      //方式一：通过id获取单个标签
 
var oDiv2 = document.getElementsByTagName("div")[0];     //方式二：通过 标签名 获得 标签数组，所以有s
 
var oDiv3 = document.getElementsByClassName("box")[0];  //方式三：通过 类名 获得 标签数组，所以有s

```

##### 事件

```javascript
JS是事件驱动为核心的一门语言
```

##### 事件的三要素

**事件的三要素：事件源、事件、事件驱动程序**。

比如，我用手去按开关，灯亮了。这件事情里，事件源是：手。事件是：按开关。事件驱动程序是：灯的开和关。

再比如，网页上弹出一个广告，我点击右上角的`X`，广告就关闭了。这件事情里，事件源是：`X`。事件是：onclick。事件驱动程序是：广告关闭了。

于是我们可以总结出：谁引发的后续事件，谁就是事件源。

**总结如下：**

- 事件源：引发后续事件的html标签。
- 事件：js已经定义好了（见下图）。
- 事件驱动程序：对样式和html的操作。也就是DOM。

 **代码书写步骤如下：**（重要）

- （1）获取事件源：```document.getElementById(“box”);``` //类似与ios语言的``` UIButton *adBtn = [UIButton buttonWithType:UIButtonTypeCustom];```
- （2）绑定事件： 事件源box.事件onclick = function(){ 事件驱动程序 };
- （3）书写事件驱动程序：关于DOM的操作

常用事件如下：

![img](https://images2018.cnblogs.com/blog/1364810/201805/1364810-20180528212850888-1985583768.png) 



##### 绑定事件的方式

###### 直接绑定匿名函数

```javascript
 var oDiv = document.getElementById("box");
    //绑定事件的第一种方式
    oDiv.onclick = function () {
        alert("我是弹出的内容");
    };
```

###### 先单独定义函数，再绑定

```javascript
 var oDiv = document.getElementById("box");
    //绑定事件的第二种方式
    oDiv.onclick = fn;   //注意，这里是fn，不是fn()。fn()指的是返回值。
    //单独定义函数
    function fn() {
        alert("我是弹出的内容");
    };
```

注意上方代码的注释。**绑定的时候，是写fn，不是写fn()**。fn代表的是整个函数，而fn()代表的是返回值。

###### 行内绑定

```html
<!--行内绑定-->
<div id="box" onclick="fn()"></div>

<script type="text/javascript">

    function fn() {
        alert("我是弹出的内容");
    }

</script>
```

注意第一行代码，绑定时，是写的`"fn()"`，不是写的`"fn"`。因为绑定的这段代码不是写在js代码里的，而是被识别成了**字符串**。

##### JavaScript入口函数 window.onload()

此函数调用，是当页面加载完毕(文档和图片)的时候，触发onload()函数，文档先加载，图片资源后加载

```html
<script type="text/javascript">
    window.onload = function () {
        console.log("alex");  //等页面加载完毕时，打印字符串
    }
</script>
```

有一点我们要知道：**js的加载是和html同步加载的**。因此，如果使用元素在定义元素之前，容易报错。这个时候，onload事件就能派上用场了，我们可以把使用元素的代码放在onload里，就能保证这段代码是最后执行。

###### window.onload()方法存在的问题

- 图片加载完成才调用onload方法，大家想个问题，如果现在用户访问JD商城页面，如果JD商城中的脚本文件在window.onload()方法调用，如果此时用户网速卡了，然后图片资源加载失败了，此时用户是做不了任何操作的，所以winodw.onload()方法有很大问题。
- window.onload()方法 如果脚本中书写两个这样的方法，那么会有事件覆盖现象。

##### 样式属性操作

所谓样式属性，就是对之前所讲解的style标签中的属性进行操作，并且通过js控制盒模型的属性（width,height等），控制盒子的显示隐藏（display:none|block）,控制盒子的颜色切换（background：red|green）等等

首先，大家明确一点，你是要操作文档对象了，要遵循事件三步走

- 获取事件源
- 事件
- 事件驱动程序

```html
<div id='box'></div>
<script>
    window.onload = function(){
        //1.获取事件源(事件对象，在文档中一切的标签都是对象)
        var oDiv = docuement.getElementById('box');
        
        //2.事件
        oDiv.onclick = function(){
            //3.事件驱动程序  ps:记得 所有的style中使用的像margin-left 在js操作时都是用marginLeft属性进行赋值
            oDiv.style.backgroundColor = 'yellow'；
        }
    };

</script>
```

##### 值的操作

所谓值的操作，就是对前闭合标签和后闭合标签中间的文本内容的设置和获取。

- 双闭合标签： innerText或者innerHTML
- 单闭合标签：除了img标签，就剩input了，使用value进行赋值

```html
<div id='box'></div>
<input type='text' value = 'alex' id='user'>
<script>
    window.onload = function(){
        //1.获取事件源(事件对象，在文档中一切的标签都是对象)
        var oDiv = docuement.getElementById('box');
         var oInput = docuement.getElementById('user');
        //2.事件
        oDiv.onclick = function(){
            //3.事件驱动程序  
            oDiv.innerText = 'alex'；//仅仅设置文本内容
            oDiv.innerHTML = '<h1>alex</h1>';//将标签和文本内容一起解析
        };
        
        //2.事件
        oInput.onclick = function(){
            //3.事件驱动程序   只有有value属性的 才能使用value赋值和设置值
            oInput.value = 'wusir'；
        }
    };

</script>
```

##### 标签属性操作

所谓标签属性,就是对标签中（字面上看到的）属性的操作。比如像每个标签中id，class，title、img

标签的src属性和alt属性、a标签的href属性、input标签中的name、type属性等等

```html
<script>
        //window.onload页面加载完毕以后再执行此代码
        window.onload = function () {
            //需求：鼠标放到img上，更换为另一张图片，也就是修改路径（src的值）。
            //步骤：
            //1.获取事件源
            //2.绑定事件
            //3.书写事件驱动程序

            //1.获取事件源
            var oImg = document.getElementById("box");
            //2.绑定事件(悬停事件：鼠标进入到事件源中立即出发事件)
            oImg.onmouseover = function () {
                //3.书写事件驱动程序(修改src)
                img.src = "image/jd2.png";
//                this.src = "image/jd2.png";
            }

            //2.绑定事件(悬停事件：鼠标进入到事件源中立即出发事件)
            oImg.onmouseout = function () {
                //3.书写事件驱动程序(修改src)
                img.src = "image/jd1.png";
            }
        }
    </script>
```





#### 节点的操作

都是**函数**（方法）

##### 创建节点

格式如下：

```
新的标签(元素节点) = document.createElement("标签名");
```

比如，如果我们想创建一个li标签，或者是创建一个不存在的adbc标签，可以这样做：

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
<script type="text/javascript">
    var a1 = document.createElement("li");   //创建一个li标签
    var a2 = document.createElement("adbc");   //创建一个不存在的标签

    console.log(a1);
    console.log(a2);

    console.log(typeof a1);
    console.log(typeof a2);
</script>
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

结果：

![img](https://images2018.cnblogs.com/blog/1364810/201805/1364810-20180528224017818-1091477607.png)

##### 插入节点

插入节点有两种方式，它们的含义是不同的。

方式1：

```
 父节点.appendChild(新的子节点);
```

解释：父节点的最后插入一个新的子节点。

方式2：

```
父节点.insertBefore(新的子节点,作为参考的子节点);
```

解释：

- 在参考节点前插入一个新的节点。
- 如果参考节点为null，那么他将在父节点最后插入一个子节点。

##### 删除节点

格式如下：

```
  父节点.removeChild(子节点);
```

解释：**用父节点删除子节点**。必须要指定是删除哪个子节点。

如果我想删除自己这个节点，可以这么做：

```
node1.parentNode.removeChild(node1);
```

#### DOM相关案例

##### 1.模态框案例

需求：

 打开网页时有一个普通的按钮，点击当前按钮显示一个背景图，中心并弹出一个弹出框，点击X的时候会关闭当前的模态框

代码如下：

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title></title>
        <style type="text/css">
            *{
                padding: 0;
                margin: 0;
            }
            html,body{
                height: 100%;
            }
            #box{
                width: 100%;
                height: 100%;
                background: rgba(0,0,0,.3);
            }
            #content{
                position: relative;
                top: 150px;
                width: 400px;
                height: 200px;
                line-height: 200px;
                text-align: center;
                color: red;
                background-color: #fff;
                margin: auto;
            }
            #span1{
                position: absolute;
                background-color: red;
                top: 0;
                right: 0;
                width: 30px;
                height: 30px;
                line-height: 30px;
                text-align: center;
                color: #fff;

            }
        </style>
    </head>
    <body>
        <button id="btn">弹出</button>
    </body>
    <script type="text/javascript">
        //获取dom元素 1.获取事件源
        var oBtn = document.getElementById('btn');
        //创建弹出模态框的相关DOM对象
        var oDiv = document.createElement('div');
        var oP = document.createElement('p');
        var oSpan = document.createElement('span');
        
        
        // 设置属性
        oDiv.id = 'box';
        oP.id = 'content'
        oP.innerHTML = '模态框成功弹出'
        oSpan.innerHTML = 'X';
        oSpan.id = 'span1'
        
        // 追加元素
        oDiv.appendChild(oP);
        oP.appendChild(oSpan);

        // 点击弹出按钮 弹出模态框
        oBtn.onclick = function(){
            //动态的添加到body中一个div
            this.parentNode.insertBefore(oDiv,oBtn)
            
        }
        // 点击X 关闭模态框
        oSpan.onclick = function(){
            // 移除oDiv元素
            oDiv.parentNode.removeChild(oDiv)
        }   
        
    </script>
</html>
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

##### 2.简易留言板

需求：

![img](https://images2018.cnblogs.com/blog/1364810/201805/1364810-20180529123520598-1464069347.png)

当在textarea中输入内容，点击留言按钮，会添加到浏览器中

图如下：
![img](https://images2018.cnblogs.com/blog/1364810/201805/1364810-20180529123719165-1667193028.png)

代码如下：

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>留言板</title>
        <style type="text/css">
            *{
                padding: 0;
                margin: 0;
            }
            .close{
                display: inline-block;
                width: 20px;
                height: 20px;
                line-height: 20px;
                text-align: center;
                cursor: pointer;
                background-color: rgba(0,0,0,.1);
                margin-left: 20px;
            }
        </style>
    </head>
    <body>
        <h1>简易留言板</h1>
        <div id="box">
            <!--<ul>
                
            </ul>-->
            
        </div>
        <textarea id="msg"></textarea>
        <input type="button" id="btn" value="留言"/>
        <button onclick="sum()">统计</button>
    </body>
    <script type="text/javascript">

        // 0 将ul标签添加到div#box标签中
        var oUl = document.createElement('ul');
        var oBox = document.getElementById('box');
        oBox.appendChild(oUl);
        
        var oBtn = document.getElementById('btn');
        var oMsg = document.getElementById('msg')
        // 控制留言的总数量
        var count = 0;
        oBtn.onclick = function(){
            
            
            // 点击留言按钮事件操作
            // 1.创建li标签
            var oLi = document.createElement('li');        
            //2.设置内容
            oLi.innerHTML = oMsg.value + "<span class='close'>X</span>"
            
            // 3.如果想在插入的第一个li获取的前面继续添加li标签
            //3.1获取li标签
            var olis = document.getElementsByTagName('li');
             //3.2 如果是第一次添加的li标签，则直接添加到ul的后面
            if(olis.length == 0){
                oUl.appendChild(oLi);
                count++;
                
            }else{
                // 3.3 如果不是第一次添加的li标签，则插入到第一个li标签的前面
                oUl.insertBefore(oLi,olis[0]);
                count++;
            }
            // 4.添加完成之后 清空textarea的值
            oMsg.value = '';
            
            
            // 5.点击X的时候删除当前的一条数据
            //5.1先获取所有的X
            var oSpans = document.getElementsByTagName('span');
            
            // 5.2for循环 对所有的X添加点击事件
            for(var i = 0; i< oSpans.length; i++){
                oSpans[i].onclick  = function(){
                    // 5.3 移除当前的li标签
                    oUl.removeChild(this.parentNode)
                    count--;
                }
            }
        
            
        }
    
        function sum(){
            alert('一共发布了'+count+'条留言');
            
        }
    </script>
</html>
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

 

##### 3.使用js模拟选择器中hover

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```html
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
    <style>
        button {
            margin: 10px;
            width: 100px;
            height: 40px;
            cursor: pointer;
        }
        .current {
            background-color: red;
        }
    </style>
</head>
<body>
<button>按钮1</button>
<button>按钮2</button>
<button>按钮3</button>
<button>按钮4</button>
<button>按钮5</button>

<script>
    //需求：鼠标放到哪个button上，改button变成黄色背景（添加类）


    var btnArr = document.getElementsByTagName("button");
    //绑定事件
    for(var i=0;i<btnArr.length;i++){   //要为每一个按钮绑定事件，所以用到了for循环
        btnArr[i].onmouseover = function () {
            //【重要】排他思想：先把所有按钮的className设置为空，然后把我（this）这个按钮的className设置为current
            //排他思想和for循环连用
            for(var j=0;j<btnArr.length;j++){
                btnArr[j].className = "";
            }
            this.className = "current";  //【重要】核心代码
        }
    }

    //鼠标离开current时，还原背景色
    for(var i=0;i<btnArr.length;i++){   //要为每一个按钮绑定事件，所以用到了for循环
        btnArr[i].onmouseout = function () { //鼠标离开任何一个按钮时，就把按钮的背景色还原
            this.className = "";
        }
    }

</script>

</body>


</html>
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

代码解释：

鼠标悬停时，current栏变色，这里用到了排他思想：先把所有按钮的className设置为空，然后把我(this)这个按钮的className设置为current，就可以达到变色的效果。核心代码是：

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```html
            //排他思想：先把所有按钮的className设置为空，然后把我（this）这个按钮的className设置为current
            //排他思想和for循环连用
            for(var j=0;j<btnArr.length;j++){
                btnArr[j].className = "";
            }
            this.className = "current";
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

##### 4.tab栏选项卡

代码如下：

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title></title>
        <style type="text/css">
            *{
                padding: 0;
                margin: 0;
            }
            ul{
                list-style: none;
            }
            #tab{
                width: 480px;
                margin: 20px auto;
                border: 1px solid red;
            }
            ul{
                width: 100%;
                overflow: hidden;
            }
            ul li{
                float: left;
                width: 160px;
                height: 60px;
                line-height: 60px;
                text-align: center;
                background-color: #cccccc;
            }
            
            ul li a{
                text-decoration: none;
                color:black;
            }
            li.active{
                background-color: red;
            }
            p{
                display: none;
                height: 200px;
                text-align: center;
                line-height: 200px;
                background-color: red;
            }
            p.active{
                display: block;
                
            }
            
        </style>
    </head>
    <body>
        <div id="tab">
            <ul>
                <li class="active">
                    <a href="#">首页</a>
                </li>
                <li>
                    <a href="#">新闻</a>
                </li>
                <li>
                    <a href="#">图片</a>
                </li>        
            </ul>
            <p class="active">首页内容</p>
            <p>新闻内容</p>
            <p>图片内容</p>
            
            
        </div>
    </body>
    <script type="text/javascript">
        window.onload = function(){
            // //需求：鼠标放到上面的li上，li本身变色(添加类)，对应的p也显示出来(添加类);
                    //思路：1.点亮上面的盒子。   2.利用索引值显示下面的盒子。

            var tabli = document.getElementsByTagName('li');
            var tabContent = document.getElementsByTagName('p')
        
            for(var i = 0; i < tabli.length; i++){
                // 绑定索引值（新增一个自定义属性：index属性）
                tabli[i].index  = i;
                tabli[i].onclick = function(){
                    
                    // 1.点亮上面的盒子。   2.利用索引值显示下面的盒子。(排他思想)
                    for(var j = 0; j < tabli.length; j++){
                        tabli[j].className = '';
                        tabContent[j].className = '';
                    }    
                    this.className = 'active'
                    
                    tabContent[this.index].className = 'active';//【重要代码】
                }
        }
        }
        
    </script>
</html>
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

#####  5、购物车案例

代码如下：

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title></title>
    <style type="text/css">
        *{
            padding: 0;
            margin: 0;
        }
        .box{
            width: 500px;
            height: 400px;
            margin: 100px auto;
            background-color: rgba(255,255,255,0.4);
            position: relative;
            
        }
        .car{
            width: 150px;
            height: 30px;
            background-color: #fff;
            padding-left: 30px;
            position: absolute;
            left: 130px;
            top: 3px;
            z-index: 3;
            border: 1px solid green;

        }
        .shop{
            width: 310px;
            height: 70px;
            background-color: #fff;
            position: absolute;
            top:33px;
            left: 0;
            display: none;

        }
        div.c{
            
            border-bottom-width: 0;
            
        }
        div.t{
            border:  1px solid green;
        }
    </style>
</head>
<body>
    <div class="box">
        <div class="car" id="myCar">我的购物车</div>
        <div class="shop t" id="shop"></div>
    </div>
    <script type="text/javascript">
        var myCar =  document.getElementById('myCar');
        var shop  = document.getElementById('shop');
        myCar.onmouseover = function(){
            shop.style.display = 'block';
            myCar.className +=' c';
        }
        myCar.onmouseout = function(){
            shop.style.display = 'none';
            myCar.removeAttribute('class');
            myCar.className = 'car';
        }
    </script>
</body>
</html>
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);) 

#### client、offset、scroll系列

他们的作用主要与计算盒模型、盒子的偏移量和滚动有关

```javascript
clientTop 内容区域到边框顶部的距离 ，说白了，就是边框的高度
clientLeft 内容区域到边框左部的距离，说白了就是边框的乱度
clientWidth 内容区域+左右padding   可视宽度
clientHeight 内容区域+ 上下padding   可视高度
```

##### client演示

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title></title>
        <style type="text/css">
            .box{
                width: 200px;
                height: 200px;
                position: absolute;
                border: 10px solid red;
                /*margin: 10px 0px 0px 0px;*/
                padding: 80px;
            }
        </style>
    </head>
    <body>
        <div class="box">
            专业丰富的课程体系，博学多闻的实力讲师以及风趣生动的课堂，在路飞，不是灌输知识，而是点燃你的学习火焰。专业丰富的课程体系，博学多闻的实力讲师以及风趣生动的课堂，在路飞，不是灌输知识，而是点燃你的学习火焰。专业丰富的课程体系，博学多闻的实力讲师以及风趣生动的课堂，在路飞，不是灌输知识，而是点燃你的学习火焰。专业丰富的课程体系，博学多闻的实力讲师以及风趣生动的课堂，在路飞，不是灌输知识，而是点燃你的学习火焰。
        </div>
    </body>
    <script type="text/javascript">
        /*
         *      clientTop 内容区域到边框顶部的距离 ，说白了，就是边框的高度
         *      clientLeft 内容区域到边框左部的距离，说白了就是边框的乱度
         *      clientWidth 内容区域+左右padding   可视宽度
         *      clientHeight 内容区域+ 上下padding   可视高度
         * */
        
        var oBox = document.getElementsByClassName('box')[0];
        console.log(oBox.clientTop);
        console.log(oBox.clientLeft);
        console.log(oBox.clientWidth);
        console.log(oBox.clientHeight)；   
        
    </script>
    
</html>
```

###### 屏幕的可视区域

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title></title>
    </head>
    <body>
    </body>
    <script type="text/javascript">
        
        // 屏幕的可视区域
        window.onload = function(){
            
            // document.documentElement 获取的是html标签
            console.log(document.documentElement.clientWidth);
            console.log(document.documentElement.clientHeight);
            // 窗口大小发生变化时，会调用此方法
            window.onresize = function(){    
                console.log(document.documentElement.clientWidth);
                console.log(document.documentElement.clientHeight);
            }         
        }
    </script>
</html>
```

##### offset演示

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title></title>
        <style type="text/css">
            *{
                padding: 0;
                margin: 0;
            }
        </style>
        
    </head>
    <body style="height: 2000px">
        <div>
            <div class="wrap" style=" width: 300px;height: 300px;background-color: green">
                <div id="box" style="width: 200px;height: 200px;border: 5px solid red;position: absolute;top:50px;left: 30px;">            
                </div>
            </div>
        </div>
    </body>
    <script type="text/javascript">
        window.onload = function(){
            var box = document.getElementById('box')
            /*
             offsetWidth占位宽  内容+padding+border
             offsetHeight占位高 
             offsetTop: 如果盒子没有设置定位 到body的顶部的距离,如果盒子设置定位，那么是以父辈为基准的top值
             offsetLeft： 如果盒子没有设置定位 到body的左部的距离，如果盒子设置定位，那么是以父辈为基准的left值
             
             * */
            console.log(box.offsetTop)
            console.log(box.offsetLeft)
            console.log(box.offsetWidth)
            console.log(box.offsetHeight)
            
        }
        
    </script>
</html>
```



##### scroll演示

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title></title>
        <style type="text/css">
            *{padding: 0;margin: 0;}
        </style>
    </head>
    <body style="width: 2000px;height: 2000px;">
        <div style="height: 200px;background-color: red;"></div>
        <div style="height: 200px;background-color: green;"></div>
        <div style="height: 200px;background-color: yellow;"></div>
        <div style="height: 200px;background-color: blue;"></div>
        <div style="height: 200px;background-color: gray;"></div>
        <div id = 'scroll' style="width: 200px;height: 200px;border: 1px solid red;overflow: auto;padding: 10px;margin: 5px 0px 0px 0px;">
            <p>学习新技能，达成人生目标，开始用自己的力量影响世界学习新技能，达成人生目标，开始用自己的力量影响世界学习新技能，达成人生目标，开始用自己的力量影响世界学习新技能，达成人生目标，开始用自己的力量影响世界学习新技能，达成人生目标，开始用自己的力量影响世界学习新技能，达成人生目标，开始用自己的力量影响世界学习新技能，达成人生目标，开始用自己的力量影响世界学习新技能，达成人生目标，开始用自己的力量影响世界学习新技能，达成人生目标，开始用自己的力量影响世界学习新技能，达成人生目标，开始用自己的力量影响世界学习新技能，达成人生目标，开始用自己的力量影响世界学习新技能，达成人生目标，开始用自己的力量影响世界
            </p>
            
        </div>
        
        
    </body>
    <script type="text/javascript">
        
        window.onload = function(){
            
            //实施监听滚动事件
            window.onscroll = function(){
//                console.log(1111)
//                console.log('上'+document.documentElement.scrollTop)
//                console.log('左'+document.documentElement.scrollLeft)
//                console.log('宽'+document.documentElement.scrollWidth)
//                console.log('高'+document.documentElement.scrollHeight)
                
                
            }
            
            var s = document.getElementById('scroll');
            
            s.onscroll = function(){
//            scrollHeight : 内容的高度+padding  不包含边框
                console.log('上'+s.scrollTop)
                console.log('左'+s.scrollLeft)
                console.log('宽'+s.scrollWidth)
                console.log('高'+s.scrollHeight)
            }
        }
        
    </script>
</html>
```

#### 补充内容：

##### 定时器

在js中有两种定时器：

- 一次性定时器：setTimeout()

- 周期性循环定时器: setInterval()

###### setTimeout()

只在指定的时间后执行一次

```javascript
/定时器 异步运行  
function hello(){  
alert("hello");  
}  
//使用方法名字执行方法  
var t1 = window.setTimeout(hello,1000);  
var t2 = window.setTimeout("hello()",3000);//使用字符串执行方法  
window.clearTimeout(t1);//去掉定时器
```



###### setInterval()

在指定时间为周期循环执行

```javascript
/实时刷新  时间单位为毫秒  
setInterval('refreshQuery()',8000);   
/* 刷新查询 */  
function refreshQuery(){  
  console.log('每8秒调一次') 
}
```

两种方法根据不同的场景和业务需求择而取之，

对于这两个方法，需要注意的是如果要求在每隔一个固定的时间间隔后就精确地执行某动作，那么最好使用setInterval，而如果不想由于连续调用产生互相干扰的问题，尤其是每次函数的调用需要繁重的计算以及很长的处理时间，那么最好使用setTimeout

### BOM

#### BOM的介绍

浏览器对象模型。

- 操作**浏览器部分功能**的API。比如让浏览器自动滚动。

####  BOM的结构图

![img](https://images2018.cnblogs.com/blog/1364810/201805/1364810-20180529172315923-104404745.png)

- **window对象是BOM的顶层(核心)对象**，所有对象都是通过它延伸出来的，也可以称为window的子对象。
- DOM是BOM的一部分。

**window对象：**

- **window对象是JavaScript中的顶级对象**。
- 全局变量、自定义函数也是window对象的属性和方法。
- window对象下的属性和方法调用时，可以省略window。

####  弹出系统对话框

比如说，`alert(1)`是`window.alert(1)`的简写，因为它是window的子方法。

系统对话框有三种：

```
    alert();    //不同浏览器中的外观是不一样的
    confirm();  //兼容不好
    prompt();   //不推荐使用
```

#### 打开窗口、关闭窗口

1、打开窗口：

```
window.open(url,target);
```

**参数解释：**

- url：要打开的地址。
- target：新窗口的位置。可以是：`_blank` 、`_self`、 `_parent` 父框架。

2、关闭窗口

```javascript
window.close();
```

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title></title>
    </head>
    <body>
        
        <!--行间的js中的open() window不能省略-->
        <button onclick="window.open('https://www.luffycity.com/')">路飞学城</button>
        
        <button>打开百度</button>
        <button onclick="window.close()">关闭</button>
        <button>关闭</button>
        
    </body>
    <script type="text/javascript">
        
        var oBtn = document.getElementsByTagName('button')[1];
        var closeBtn = document.getElementsByTagName('button')[3];
        
        oBtn.onclick = function(){
                      //open('https://www.baidu.com')
            
            //打开空白页面
            open('about:blank',"_self")
        }
        closeBtn.onclick = function(){
            if(confirm("是否关闭？")){
                close();
            }
        }
        
    </script>
</html>
```

#### location对象

`window.location`可以简写成location。location相当于浏览器地址栏，可以将url解析成独立的片段。

###### location对象的属性

- **href**：跳转
- hash 返回url中#后面的内容，包含#
- host 主机名，包括端口
- hostname 主机名
- pathname url中的路径部分
- protocol 协议 一般是http、https
- search 查询字符串

######  案例 模拟a标签跳转

```html
<body>
<span>luffy</span>
<script>

    var oSpan = document.getElementsByTagName("span")[0];

    oSpan.onclick = function () {
        location.href = "http://www.luffycity.com";   //点击span时，跳转到指定链接
 //     window.open("http://www.luffycity.com"","_blank");  //方式二 跳转
    }

</script>
</body>
```

###### location对象的方法

```javascript
window.location.reload(); //全局刷新页面，相当于浏览器导航栏上 刷新按钮
```

###### navigator对象

window.navigator 的一些属性可以获取客户端的一些信息。

- userAgent：系统，浏览器)
- platform：浏览器支持的系统，win/mac/linux

 ```javascript
console.log(navigator.userAgent);
console.log(navigator.platform);
 ```

###### history对象

1、后退：

- history.back()
- history.go(-1)：0是刷新

2、前进：

- history.forward()
- history.go(1)

 用的不多。因为浏览器中已经自带了这些功能的按钮：

#### HTML5 存储技术 localStorage sessionStorage

```javascript
对浏览器来说，使用 Web Storage 存储键值对比存储 Cookie 方式更直观，而且容量更大，它包含两种：localStorage 和 sessionStorage

sessionStorage（临时存储） ：为每一个数据源维持一个存储区域，在浏览器打开期间存在，包括页面重新加载

localStorage（长期存储） ：与 sessionStorage 一样，但是浏览器关闭后，数据依然会一直存在
```

##### API

```javascript
sessionStorage 和 localStorage 的用法基本一致，引用类型的值要转换成JSON
```

##### 1.保存数据到本地

```javascript
let info = {
    name: 'Lee',
    age: 20,
    id: '001'
};
sessionStorage.setItem('key', JSON.stringify(info));
localStorage.setItem('key', JSON.stringify(info));
```

##### 2.从本地存储获取数据

```javascript
var data1 = JSON.parse(sessionStorage.getItem('key'));
var data2 = JSON.parse(localStorage.getItem('key'));
```

##### 3.本地存储中删除某个保存的数据

```javascript
sessionStorage.removeItem('key');
localStorage.removeItem('key');
```

##### 4.删除所有保存的数据

```javascript
sessionStorage.clear();
localStorage.clear();
```

##### 5.监听本地存储的变化

```javascript
Storage 发生变化（增加、更新、删除）时的 触发，同一个页面发生的改变不会触发，只会监听同一域名下其他页面改变 Storage
```

```javascript
 window.addEventListener('storage', function (e) {
        console.log('key', e.key);
        console.log('oldValue', e.oldValue);
        console.log('newValue', e.newValue);
        console.log('url', e.url);
    })
```

##### 浏览器查看方法

- 1. 进入开发者工具
- 1. 选择 Application
- 1. 在左侧 Storage 下 查看 Local Storage 和 Session Storage