

### jQuery的介绍和核心

jQuery是一个快速，小巧，功能丰富的JavaScript库。它通过易于使用的API在大量浏览器中运行，使得HTML文档遍历和操作，事件处理，动画和Ajax更加简单。通过多功能性和可扩展性的结合，jQuery改变了数百万人编写JavaScript的方式。另外它只是封装了js的dom的操作和ajax，其它的未封装。所以js是包含jquery的。由此可见，jquery的出现，使我们更加容易操作DOM。

```javascript
核心思想：write less,do more 写的少 做的多
```

 **关于jQuery的相关资料：**

- 官网：<http://jquery.com/>
- 官网API文档：<http://api.jquery.com/>
- 汉化API文档：<http://www.css88.com/jqapi-1.9/>

 

#### 为什么要使用jQuery

在用js写代码时，会遇到一些问题：

- window.onload 事件有事件覆盖的问题，因此只能写一个事件。
- 代码容错性差。
- 浏览器兼容性问题。
- 书写很繁琐，代码量多。
- 代码很乱，各个页面到处都是。
- 动画效果很难实现。

![img](https://images2018.cnblogs.com/blog/1364810/201805/1364810-20180530143204263-706550346.png)

**jQuery的出现，可以解决以上问题。**

#### 学习jQuery，主要学什么

初期，主要学习如何使用jQuery操作DOM，其实就是学习jQuery封装好的那些功API。

这些API的共同特点是：几乎全都是**方法**。所以，在使用jQuery的API时，都是方法调用，也就是说要加小括号()，小括号里面是相应的参数，参数不同，功能不同。

#### jQuery的第一个demo

先让大家感受一下jquery的强大，为什么是write less ,do more?

```javascript
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title></title>
    <style type="text/css">
        div{
            width: 100px;
            height: 100px;
            background-color: green;
            margin-top: 20px;
            display: none;
        }
    </style>
</head>
<body>
    <button>操作</button>
    <div></div>
    <div></div>
    <div></div>
    <script type="text/javascript" src="jquery-3.3.1.js"></script>
    <script type="text/javascript">
        $(document).ready(function(){
            // 获取dom元素
            var oBtn = $('button'); //根据标签名获取元素
            var oDiv = $('div'); //根据标签名获取元素
            oBtn.click(function(){
                oDiv.show(1000);//显示盒子
                oDiv.html('赵云'); // 设置内容
            });//事件是通过方法绑定的
        })
    </script>
    
</body>
</html>
```

#### jQuery的两大特点

- 链式编程：比如`.show()`和`.html()`可以连写成`.show().html()`。
- 隐式迭代：隐式 对应的是 显式。隐式迭代的意思是：在方法的内部进行循环遍历，而不用我们自己再进行循环，简化我们的操作，方便我们调用。

#### 入口函数和window.onload()对比

原生 js 的入口函数指的是：`window.onload = function() {};` 如下：

```javascript
  //原生 js 的入口函数。页面上所有内容加载完毕，才执行。
        //不仅要等文本加载完毕，而且要等图片也要加载完毕，才执行函数。
       window.onload = function () {
           alert(1);
       }
```

而 jQuery的入口函数，有以下几种写法：

```javascript
写法一：
 //1.文档加载完毕，图片不加载的时候，就可以执行这个函数。
       $(document).ready(function () {
           alert(1);
       })
写法二：（写法一的简洁版）

 //2.文档加载完毕，图片不加载的时候，就可以执行这个函数。
       $(function () {
           alert(1);
       });
写法三：

  //3.文档加载完毕，图片也加载完毕的时候，在执行这个函数。
       $(window).ready(function () {
           alert(1);
       })
```

#### **jQuery入口函数与js入口函数的区别**：

区别一：书写个数不同：

- Js 的入口函数只能出现一次，出现多次会存在事件覆盖的问题。
- jQuery 的入口函数，可以出现任意多次，并不存在事件覆盖问题。

区别二：执行时机不同：

- Js的入口函数是在**所有的文件资源加载**完成后，才执行。这些**文件资源**包括：页面文档、外部的js文件、外部的css文件、图片等。
- jQuery的入口函数，是在文档加载完成后，就执行。文档加载完成指的是：DOM树加载完成后，就可以操作DOM了，不用等到所有的**外部资源**都加载完成。

**文档加载的顺序：从上往下，边解析边执行。**

#### jQuery的`#### 符号

jQuery 使用 `$` 符号原因：书写简洁、相对于其他字符与众不同、容易被记住。

jQuery占用了我们两个变量：`$` 和 jQuery。当我们在代码中打印它们俩的时候：

```javascript
  <script src="jquery-3.3.1.js"></script>
    <script>

        console.log($);
        console.log(jQuery);
        console.log($===jQuery);


    </script>
```

打印结果：

![img](https://images2018.cnblogs.com/blog/1364810/201805/1364810-20180530155126046-775007440.png)

从打印结果可以看出，$ 代表的就是 jQuery。

那怎么理解jQuery里面的 `$` 符号呢？

**$ 实际上表示的是一个函数名** 如下：

```javascript
    $(); // 调用上面我们自定义的函数$

    $(document）.ready(function(){}); // 调用入口函数

    $(function(){}); // 调用入口函数

    $("#btnShow") // 获取id属性为btnShow的元素

    $("div") // 获取所有的div标签元素

```

如上方所示，jQuery 里面的 `$` 函数，根据传入参数的不同，进行不同的调用，实现不同的功能。返回的是jQuery对象。

jQuery这个js库，除了`$` 之外，还提供了另外一个函数：jQuery。jQuery函数跟 `$` 函数的关系：`jQuery === $`。

#### js中的DOM对象 和 jQuery对象 比较（重点，难点）

##### 二者的区别

通过 jQuery 获取的元素是一个**伪数组**，数组中包含着原生JS中的DOM对象。举例：

针对下面这样一个div结构：

通过原生 js 获取这些元素节点的方式是：

```
    var myBox = document.getElementById("app");           //通过 id 获取单个元素
    var boxArr = document.getElementsByClassName("box");  //通过 class 获取的是伪数组
    var divArr = document.getElementsByTagName("div");    //通过标签获取的是伪数组
```

通过 jQuery 获取这些元素节点的方式是：（获取的都是数组）

```
  //获取的是伪数组，里面包含着原生 JS 中的DOM对象。
```

```javascript
console.log($('#app'));

console.log($('.box'));

console.log($('div'));
```

打印结果如下：

![img](https://images2018.cnblogs.com/blog/1364810/201805/1364810-20180530155928958-95493609.png)

##### 二者的相互准换

**1、 DOM 对象 转为 jQuery对象**：

```
$(js对象);
```

**2、jQuery对象 转为 DOM 对象**：

```
jquery对象[index];      //方式1（推荐）

jquery对象.get(index);  //方式2
```

jQuery对象转换成了 DOM 对象之后，可以直接调用 DOM 提供的一些功能。如：

```
$('div')[1].style.backgroundColor = 'yellow';
$('div')[3].style.backgroundColor = 'green';
```

 **总结**：如果想要用哪种方式设置属性或方法，必须转换成该类型。

举例：

隔行换色

```html
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
    <script src="jquery-3.3.1.js"></script>
    <script>
        //入口函数
        jQuery(function () {
            var jqLi = $("li");
            for (var i = 0; i < jqLi.length; i++) {
                if (i % 2 === 0) {
                    //jquery对象，转换成了js对象
                    jqLi[i].style.backgroundColor = "pink";
                } else {
                    jqLi[i].style.backgroundColor = "yellow";
                }
            }
        });
    </script>
</head>
<body>
<ul>
    <li>小马哥</li>
    <li>小马哥</li>
    <li>小马哥</li>
    <li>小马哥</li>
    <li>小马哥</li>
    <li>小马哥</li>
</ul>
</body>
</html>
```

效果如下：

![img](https://images2018.cnblogs.com/blog/1364810/201805/1364810-20180530163837593-2073119955.png)



### jQuery的选择器

我们以前在CSS中学习的选择器有：

![img](https://images2018.cnblogs.com/blog/1364810/201805/1364810-20180530164310470-821681311.png)

今天来学习一下jQuery 选择器。

jQuery选择器是jQuery强大的体现，它提供了一组方法，让我们更加方便的获取到页面中的元素。

#### jquery的基本选择器

![img](https://images2018.cnblogs.com/blog/1364810/201805/1364810-20180530164441341-1837779533.png)

![img](https://images2018.cnblogs.com/blog/1364810/201805/1364810-20180530164500967-140993085.png)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
    <div></div>
    <div id="box"></div>
    <div class="box"></div>
    <div class="box"></div>
    <div></div>
    <script type="text/javascript" src="jquery-3.3.1.js"></script>
    <script type="text/javascript">
        //入口函数
        $(function(){
            //三种方式获取jquery对象
            var jqBox1 = $("#box");
                   var jqBox2 = $(".box");
            var jqBox3 = $('div');

            //操作标签选择器
            jqBox3.css('width', '100');
            jqBox3.css('height', 100);
            jqBox3.css('background-color', 'red');
            jqBox3.css('margin-top', 10);


            //操作类选择器(隐式迭代，不用一个一个设置)
                    jqBox2.css("background", "green");
                    jqBox2.text('哈哈哈')

                    //操作id选择器
                    jqBox1.css("background", "yellow");
                   
        })
    </script>
    
</body>
</html>
```

#### 层级选择器

![img](https://images2018.cnblogs.com/blog/1364810/201805/1364810-20180530165910666-772076109.png)



![img](https://images2018.cnblogs.com/blog/1364810/201805/1364810-20180530165935681-993240948.png)

```html
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
    <script src="jquery-3.3.1.js"></script>
    <script>
        $(function () {
            //获取ul中的li设置为粉色
            //后代：儿孙重孙曾孙玄孙....
            var jqLi = $("ul li");
            jqLi.css("margin",5);
            jqLi.css("background", "pink");

            //子代：亲儿子
            var jqOtherLi = $("ul>li");
            jqOtherLi.css("background", "red");
        });
    </script>
</head>
<body>
<ul>
    <li>111</li>
    <li>222</li>
    <li>333</li>
    <ol>
        <li>aaa</li>
        <li>bbb</li>
        <li>ccc</li>
    </ol>
</ul>
</body>
</html>
```

#### 基本过滤选择器

![img](https://images2018.cnblogs.com/blog/1364810/201805/1364810-20180530170210737-2052147195.png)

![img](https://images2018.cnblogs.com/blog/1364810/201805/1364810-20180530170245617-2029917748.png)



```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>基本过滤选择器</title>
    </head>
    <body>
        <ul>
            <li>哈哈哈哈，基本过滤选择器</li>
            <li>嘿嘿嘿</li>
            <li>天王盖地虎</li>
            <li>小鸡炖蘑菇</li>
            
        </ul>
    </body>
    <script src="jquery-3.3.1.js"></script>
    <script type="text/javascript">
        
        $(function(){
            //获取第一个 :first ,获取最后一个 :last
            
            //奇数
            $('li:odd').css('color','red');
            //偶数
            $('li:even').css('color','green');
            
            //选中索引值为1的元素 *
            $('li:eq(1)').css('font-size','30px');
            
            //大于索引值1
            $('li:gt(1)').css('font-size','50px');
            
            //小于索引值1
            $('li:lt(1)').css('font-size','12px');  
            
        })

    </script>
</html>
```

#### 属性选择器

![img](https://images2018.cnblogs.com/blog/1364810/201805/1364810-20180531183756059-1051347862.png)



```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title></title>
    </head>
    <body>
         <div id="box">
            <h2 class="title">属性元素器</h2>
            <!--<p class="p1">我是一个段落</p>-->
            <ul>
                <li id="li1">分手应该体面</li>
                <li class="what" id="li2">分手应该体面</li>
                <li class="what">分手应该体面</li>
                <li class="heihei">分手应该体面</li>

            </ul>

            <form action="" method="post">

                <input name="username" type='text' value="1" checked="checked" />
                <input name="username1111" type='text' value="1" />
                <input name="username2222" type='text' value="1" />
                <input name="username3333" type='text' value="1" />
                <button class="btn-default">按钮1</button>
                <button class="btn-info">按钮1</button>
                <button class="btn-success">按钮1</button>
                <button class="btn-danger">按钮1</button>


            </form>
        </div>
    </body>
    <script src="jquery-3.3.1.js"></script>
    <script type="text/javascript">
        
        $(function(){
            //标签名[属性名] 查找所有含有id属性的该标签名的元素
            $('li[id]').css('color','red');
            
            //匹配给定的属性是what值得元素
            $('li[class=what]').css('font-size','30px');
            //[attr!=value] 匹配所有不含有指定的属性，或者属性不等于特定值的元素
            $('li[class!=what]').css('font-size','50px');
            
            //匹配给定的属性是以某些值开始的元素
            $('input[name^=username]').css('background','gray');
            //匹配给定的属性是以某些值结尾的元素
            $('input[name$=222]').css('background','greenyellow');
            
            //匹配给定的属性是以包含某些值的元素
            $('button[class*=btn]').css('background','red')
        
            
        })
    
    </script>
</html>
```

#### 筛选选择器

![img](https://images2018.cnblogs.com/blog/1364810/201805/1364810-20180530170831837-1810442619.png)

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title></title>
    </head>
    <body>
         <div id="box">
            <p class="p1">
                <span>我是第一个span标签</span>
                <span>我是第二个span标签</span>
                <span>我是第三个span标签</span>
            </p>
            <button>按钮</button>
        </div>
        <ul>
            <li class="list">2</li>
            <li>3</li>
            <li>4</li>
            <li>5</li>
        </ul>
    </body>
    <script src="jquery-3.3.1.js"></script>
    <script type="text/javascript">
        
        //获取第n个元素 数值从0开始
        $('span').eq(1).css('color','#FF0000');
        
        //获取第一个元素 :first :last    点语法  ：get方法 和set方法
        $('span').last().css('color','greenyellow');
        $('span').first().css('color','greenyellow');
        
        //查找span标签的父元素（亲的）
        $('span').parent('.p1').css({"width":'200px','height':'200px',"background":'red'});
        
        //选择所有的兄弟元素（不包括自己）
                  $('.list').siblings('li').css('color','red');

                  
                //查找所有的后代元素
                   $('div').find('button').css('background','yellow');

                
                //不写参数代表获取所有子元素。
                   $('ul').children().css("background", "green");
                   $('ul').children("li").css("margin-top", 10);
                   

        
        
    </script>
</html>
```

选择器介绍完毕，内容比较多，大家根据之前学习到的css选择器可以更好的使用jquery选择器的用法。

### jQuery动画

jQuery提供的一组网页中常见的动画效果，这些动画是标准的、有规律的效果；同时还提供给我们了自定义动画的功能。

#### 显示动画

方式一：

```
  $("div").show();
```

解释：无参数，表示让指定的元素直接显示出来。其实这个方法的底层就是通过`display: block;`实现的。

方式二：

```
$('div').show(3000);
```

解释：通过控制元素的宽高、透明度、display属性，逐渐显示，2秒后显示完毕。

方式三：

```
 $("div").show("slow");
```

参数可以是：

- slow 慢：600ms
- normal 正常：400ms
- fast 快：200ms

解释：和方式二类似，也是通过控制元素的宽高、透明度、display属性，逐渐显示。

方式四：

```
 //show(毫秒值，回调函数;
    $("div").show(5000,function () {
        alert("动画执行完毕！");
    });
```

解释：动画执行完后，立即执行回调函数。

**总结：**

上面的四种方式几乎一致：参数可以有两个，第一个是动画的执行时长，第二个是动画结束后执行的回调函数。

#### 隐藏动画

方式参照上面的show()方法的方式。如下：

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
    $(selector).hide();

    $(selector).hide(1000); 

    $(selector).hide("slow");

    $(selector).hide(1000, function(){});
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

###### **实现点击按钮显示盒子，再点击按钮隐藏盒子**

**代码如下：**

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title></title>
        <style type="text/css">
            #box{
                width: 200px;
                height: 200px;
                background-color: green;
                border: 1px solid red;
                display: none;
            }
        </style>
    </head>
    <body>
        <div id="box">        
        </div>
        <button id="btn">隐藏</button>    
    </body>
    <script src="jquery-3.3.1.js"></script>
    
    <script type="text/javascript">
        
        //jquery 提供了一些方法 show() hide() 控制元素显示隐藏
        var isShow = true;
        $('#btn').click(function(){
            if(isShow){
                $('#box').show('slow',function(){
                    $(this).text('盒子出来了');            
                    $('#btn').text('显示');
                    isShow = false;
                })
            }else{
                $('#box').hide(2000,function(){
                    $(this).text('');    
                    $('#btn').text('隐藏');
                    isShow = true;
                    
                })
            }
        })
    
        
    </script>
</html>
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

 

#### **开关式显示隐藏动画**

```
$('#box').toggle(3000,function(){});
```

显示和隐藏的来回切换采用的是toggle()方法：就是先执行show()，再执行hide()。

代码如下：

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```javascript
    $('#btn').click(function(){
            $('#box').toggle(3000,function(){
                $(this).text('盒子出来了');    
                if ($('#btn').text()=='隐藏') {
                    $('#btn').text('显示');    
                }else{
                    $('#btn').text('隐藏');    
                }
            });
     })
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

#### 滑入和滑出

**1、滑入动画效果**：（类似于生活中的卷帘门）

```
$(selector).slideDown(speed, 回调函数);
```

解释：下拉动画，显示元素。

注意：省略参数或者传入不合法的字符串，那么则使用默认值：400毫秒（同样适用于fadeIn/slideDown/slideUp）

**2、滑出动画效果：** 

```
 $(selector).slideUp(speed, 回调函数);
```

解释：上拉动画，隐藏元素。

**3、滑入滑出切换动画效果：**

```
 $(selector).slideToggle(speed, 回调函数);
```

代码如下：

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```html
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
    <style>
        div {
            width: 300px;
            height: 300px;
            display: none;
            background-color: green;
        }
    </style>

    <script src="jquery-3.3.1.js"></script>
    <script>
        $(function () {
            //点击按钮后产生动画
            $("button:eq(0)").click(function () {

                //滑入动画： slideDown(毫秒值，回调函数[显示完毕执行什么]);
                $("div").slideDown(2000, function () {
                    alert("动画执行完毕！");
                });
            })

            //滑出动画
            $("button:eq(1)").click(function () {

                //滑出动画：slideUp(毫秒值，回调函数[显示完毕后执行什么]);
                $("div").slideUp(2000, function () {
                    alert("动画执行完毕！");
                });
            })

            $("button:eq(2)").click(function () {
                //滑入滑出切换（同样有四种用法）
                $("div").slideToggle(1000);
            })

        })
    </script>
</head>
<body>
<button>滑入</button>
<button>滑出</button>
<button>切换</button>
<div></div>

</body>
</html>
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

#### 淡入淡出动画

1、淡入动画效果：

```
 $(selector).fadeIn(speed, callback);

```

作用：让元素以淡淡的进入视线的方式展示出来。

 

2、淡出动画效果：

```
$(selector).fadeOut(1000);

```

作用：让元素以渐渐消失的方式隐藏起来

 

3、淡入淡出切换动画效果：

```
 $(selector).fadeToggle('fast', callback);

```

作用：通过改变透明度，切换匹配元素的显示或隐藏状态。

参数的含义同show()方法。

代码如下：

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```html
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
    <style>
        div {
            width: 300px;
            height: 300px;
            display: none;
            /*透明度*/
            opacity: 0.5;
            background-color: red;
        }
    </style>

    <script src="jquery-3.3.1.js"></script>
    <script>
        $(function () {
            //点击按钮后产生动画
            $("button:eq(0)").click(function () {

//                //淡入动画用法1:   fadeIn();   不加参数
                $("div").fadeIn();

//                //淡入动画用法2:   fadeIn(2000);   毫秒值
//                $("div").fadeIn(2000);
//                //通过控制  透明度和display

                //淡入动画用法3:   fadeIn(字符串);   slow慢：600ms   normal正常:400ms   fast快：200ms
//                $("div").fadeIn("slow");
//                $("div").fadeIn("fast");
//                $("div").fadeIn("normal");

                //淡入动画用法4:   fadeIn(毫秒值，回调函数[显示完毕执行什么]);
//                $("div").fadeIn(5000,function () {
//                    alert("动画执行完毕！");
//                });
            })

            //滑出动画
            $("button:eq(1)").click(function () {
//                //滑出动画用法1:   fadeOut();   不加参数
               $("div").fadeOut();

//                //滑出动画用法2:   fadeOut(2000);   毫秒值
//                $("div").fadeOut(2000);  //通过这个方法实现的：display: none;
//                //通过控制  透明度和display

                //滑出动画用法3:   fadeOut(字符串);   slow慢：600ms   normal正常:400ms   fast快：200ms
//                $("div").fadeOut("slow");
//                $("div").fadeOut("fast");
//                $("div").fadeOut("normal");

                //滑出动画用法1:   fadeOut(毫秒值，回调函数[显示完毕执行什么]);
//                $("div").fadeOut(2000,function () {
//                    alert("动画执行完毕！");
//                });
            })

            $("button:eq(2)").click(function () {
                //滑入滑出切换
                //同样有四种用法
                $("div").fadeToggle(1000);
            })

            $("button:eq(3)").click(function () {
                //改透明度
                //同样有四种用法
                $("div").fadeTo(1000, 0.5, function () {
                    alert(1);
                });
            })
        })
    </script>
</head>
<body>
<button>淡入</button>
<button>淡出</button>
<button>切换</button>
<button>改透明度为0.5</button>
<div></div>

</body>
</html>
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

#### 自定义动画

语法：

```
 $(selector).animate({params}, speed, callback);

```

作用：执行一组CSS属性的自定义动画。

- 第一个参数表示：要执行动画的CSS属性（必选）
- 第二个参数表示：执行动画时长（可选）
- 第三个参数表示：动画执行完后，立即执行的回调函数（可选）

代码如下：

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```html
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
    <style>
        div {
            position: absolute;
            left: 20px;
            top: 30px;
            width: 100px;
            height: 100px;
            background-color: green;
        }
    </style>
    <script src="jquery-3.3.1.js"></script>
    <script>
        jQuery(function () {
            $("button").click(function () {
                var json = {"width": 500, "height": 500, "left": 300, "top": 300, "border-radius": 100};
                var json2 = {
                    "width": 100,
                    "height": 100,
                    "left": 100,
                    "top": 100,
                    "border-radius": 100,
                    "background-color": "red"
                };

                //自定义动画
                $("div").animate(json, 1000, function () {
                    $("div").animate(json2, 1000, function () {
                        alert("动画执行完毕！");
                    });
                });

            })
        })
    </script>
</head>
<body>
<button>自定义动画</button>
<div></div>
</body>
</html>
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

#### 停止动画

```
$(selector).stop(true, false);

```

**里面的两个参数，有不同的含义。**

第一个参数：

- true：后续动画不执行。
- false：后续动画会执行。

第二个参数：

- true：立即执行完成当前动画。
- false：立即停止当前动画。

PS：参数如果都不写，默认两个都是false。实际工作中，直接写stop()用的多。

 

**案例：鼠标悬停时，弹出下拉菜单（下拉时带动画）**

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```html
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
    <style type="text/css">
        * {
            margin: 0;
            padding: 0;
        }

        ul {
            list-style: none;
        }

        .wrap {
            width: 330px;
            height: 30px;
            margin: 100px auto 0;
            padding-left: 10px;
            background-color: pink;
        }

        .wrap li {
            background-color: green;
        }

        .wrap > ul > li {
            float: left;
            margin-right: 10px;
            position: relative;
        }

        .wrap a {
            display: block;
            height: 30px;
            width: 100px;
            text-decoration: none;
            color: #000;
            line-height: 30px;
            text-align: center;
        }

        .wrap li ul {
            position: absolute;
            top: 30px;
            display: none;
        }
    </style>
    <script src="jquery-3.3.1.js"></script>
    <script>
        //入口函数
        $(document).ready(function () {
            //需求：鼠标放入一级li中，让他里面的ul显示。移开隐藏。
            var jqli = $(".wrap>ul>li");

            //绑定事件
            jqli.mouseenter(function () {
                $(this).children("ul").stop().slideDown(1000);
            });

            //绑定事件(移开隐藏)
            jqli.mouseleave(function () {
                $(this).children("ul").stop().slideUp(1000);
            });
        });
    </script>

</head>
<body>
<div class="wrap">
    <ul>
        <li>
            <a href="javascript:void(0);">一级菜单1</a>
            <ul>
                <li><a href="javascript:void(0);">二级菜单2</a></li>
                <li><a href="javascript:void(0);">二级菜单3</a></li>
                <li><a href="javascript:void(0);">二级菜单4</a></li>
            </ul>
        </li>
        <li>
            <a href="javascript:void(0);">二级菜单1</a>
            <ul>
                <li><a href="javascript:void(0);">二级菜单2</a></li>
                <li><a href="javascript:void(0);">二级菜单3</a></li>
                <li><a href="javascript:void(0);">二级菜单4</a></li>
            </ul>
        </li>
        <li>
            <a href="javascript:void(0);">三级菜单1</a>
            <ul>
                <li><a href="javascript:void(0);">三级菜单2</a></li>
                <li><a href="javascript:void(0);">三级菜单3</a></li>
                <li><a href="javascript:void(0);">三级菜单4</a></li>
            </ul>
        </li>
    </ul>
</div>
</body>
</html>
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

ps:

```
javascript:void(0); //跟javascript:;效果一样 阻止默认事件 比如a标签和form表单
```

### jQuery的属性操作

上方代码中，关键的地方在于，用了stop函数，再执行动画前，先停掉之前的动画。

jquery的属性操作模块分为四个部分：html属性操作，dom属性操作，类样式操作和值操作

- `html属性操作：是对html文档中的属性进行读取，设置和移除操作。比如attr()、removeAttr()`
- `DOM属性操作：对DOM元素的属性进行读取，设置和移除操作。比如prop()、removeProp()`
- `类样式操作：是指对DOM属性className进行添加，移除操作。比如addClass()、removeClass()、toggleClass()`
- `值操作：是对DOM属性value进行读取和设置操作。比如html()、text()、val()`



#### 对html属性操作

##### attr()

设置属性值或者 返回被选元素的属性值

```javascript
//获取值：attr()设置一个属性值的时候 只是获取值
var id = $('div').attr('id')
console.log(id)
var cla = $('div').attr('class')
console.log(cla)
//设置值
//1.设置一个值 设置div的class为box
$('div').attr('class','box')
//2.设置多个值，参数为对象，键值对存储
$('div').attr({name:'hahaha',class:'happy'})
```

##### removeAttr()

移除属性

```javascript
//删除单个属性
$('#box').removeAttr('name');
$('#box').removeAttr('class');
//删除多个属性
$('#box').removeAttr('name class');
```

##### prop()

prop() 方法设置或返回被选元素的属性和值。

当该方法用于**返回**属性值时，则返回第一个匹配元素的值。

当该方法用于**设置**属性值时，则为匹配元素集合设置一个或多个属性/值对。

语法：

返回属性的值：

```javascript
$(selector).prop(property)
```

设置属性和值：

```javascript
$(selector).prop(property,value)
```

设置多个属性和值：

```javascript
$(selector).prop({property:value, property:value,...})
```

##### 关于attr()和prop()的区别

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
    男<input type="radio" id='test' name="sex"  checked/>
    女<input type="radio" id='test2' name="sex" />
    <button>提交</button>

    <script type="text/javascript" src="jquery-3.3.1.js"></script>
    <script type="text/javascript">
        $(function(){
            //获取第一个input
            var el = $('input').first();
            //undefined  因为attr是获取的这个对象属性节点的值，很显然此时没有这个属性节点，自然输出undefined
            console.log(el.attr('style'));
            // 输出CSSStyleDeclaration对象，对于一个DOM对象，是具有原生的style对象属性的，所以输出了style对象
            console.log(el.prop('style'));
            console.log(document.getElementById('test').style);

            $('button').click(function(){
                alert(el.prop("checked") ? "男":"女");
            })
            


        })
    </script>
    
</body>
</html>
```

##### 什么时候使用attr()，什么时候使用prop()？

1.是有true,false两个属性使用prop();

2.其他则使用attr();

 

#### 对标签class的操作

##### addClass（添加多个类名）

为每个匹配的元素添加指定的类名。

```javascript
$('div').addClass("box");//追加一个类名到原有的类名
```

还可以为匹配的元素添加多个类名

```javascript
$('div').addClass("box box2");//追加多个类名
```

##### removeClass

从所有匹配的元素中删除全部或者指定的类。

 移除指定的类（一个或多个）

```javascript
$('div').removeClass('box')；
```

移除全部的类

```javascript
$('div').removeClass();
```

可以通过添加删除类名，来实现元素的显示隐藏

代码如下：

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```javascript
var tag  = false;
    $('span').click(function(){
        if(tag){
            $('span').removeClass('active')
            tag=false;
        }else{
            $('span').addClass('active')
            tag=true;
        }    
})
```

##### 案例：

代码如下：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title></title>
    <style type="text/css">
        .active{
            color: red;
        }
    </style>
</head>
<body>
     <ul>
         <li class="item">张三</li>
         <li class="item">李四</li>
         <li class="item">王五</li>
     </ul>
     <script type="text/javascript" src="jquery-3.3.1.js"></script>
     <script type="text/javascript">
         $(function(){

             $('ul li').click(function(){
                 // this指的是当前点击的DOM对象 ,使用$(this)转化jquery对象
                 $(this).addClass('active').siblings('li').removeClass('active');
             })
         })
     </script>
    
</body>
</html>
```

##### toggleClass

如果存在（不存在）就删除（添加）一个类。

语法：toggleClass('box')

```javascript
$('span').click(function(){
    //动态的切换class类名为active
    $(this).toggleClass('active')
})
```



#### 对值的操作

##### html()

获取值：

语法;

html() 是获取选中标签元素中所有的内容

```javascript
$('#box').html();
```

设置值：设置该元素的所有内容 会替换掉 标签中原来的内容

```javascript
$('#box').html('<a href="https://www.baidu.com">百度一下</a>');
```

##### text()

获取值：

text() 获取匹配元素包含的文本内容

语法：

```javascript
$('#box').text();
```

设置值：

设置该所有的文本内容

```javascript
$('#box').text('<a href="https://www.baidu.com">百度一下</a>');
```

注意：值为标签的时候 不会被渲染为标签元素 只会被当做值渲染到浏览器中

##### val()

获取值：

val()用于表单控件中获取值，比如input textarea select等等

设置值：

```javascript
$('input').val('设置了表单控件中的值')；
```

#### 操作input的value值

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title></title>
</head>

<body>
    <form>
        男
        <input type="radio" name="sex" checked=""> 女
        <input type="radio" name="sex">
        <select>
            <option >张三</option>
            <option text='test'>李四</option>
            <option>王五</option>
        </select>
    </form>
    <script type="text/javascript" src="jquery-3.3.1.js"></script>
    <script type="text/javascript">
 

    $(function() {

    	// $('input[type=radio]').get(1).checked = true;
	//设置value=2的项目为当前选中项 
	$("input[type=radio]").eq(1).attr("checked",true);
        $('input[type=radio]').change(function(event) {
            /* Act on the event */
            alert(1);
            // console.log($(this).select());
            console.log($(this).select().prop('checked'));
            var item = $("input[type=radio]:checked").val();
            console.log(item);
            // 获取select被选中项的文本
            var item2 = $("select option[selected]").text();
            console.log(item2);

        });

        $('select').change(function() {
        	   console.log($(this).val());
            //1.获取选中项的值
            console.log($('select');
            // 2.获取选中项的文本
            console.log($("select option:selected").text());
            // 或者
            console.log($("select").find("option:selected").text());

            // 3.获取选中项的索引
            console.log($("select").get(0).selectedIndex);


        });

          // 设置值： 两种方式设置值
          $("select option").get(1).selected = true;
          $("select").get(0).selectedIndex = 2;

    });
    </script>
</body>

</html>
```



####  对DOM文档的操作

##### 一.插入操作

###### 知识点1：父子之间

语法：

```
父元素.append(子元素)

```

解释：追加某元素，在父元素中添加新的子元素。子元素可以为：stirng | element（js对象） | jquery元素

代码如下：

```
var oli = document.createElement('li');
oli.innerHTML = '哈哈哈';
$('ul').append('<li>1233</li>');
$('ul').append(oli);
$('ul').append($('#app'));

```

PS:如果追加的是jquery对象那么这些元素将从原位置上消失。简言之，就是一个移动操作。

 

###### 知识点2：父子之间

语法：

```
子元素.appendTo(父元素)

```

解释：追加到某元素 子元素添加到父元素

```javascript
$('<li>天王盖地虎</li>').appendTo($('ul')).addClass('active');
```

PS:要添加的元素同样既可以是stirng 、element(js对象) 、 jquery元素

 

###### 知识点3：父子之间

语法：

```javascript
父元素.prepend(子元素)；
```

解释：前置添加， 添加到父元素的第一个位置

```javascript
$('ul').prepend('<li>我是第一个</li>');
```

 

###### 知识点4：父子之间

语法：

```javascript
子元素.prependTo(父元素)；
```

解释：前置添加， 添加到父元素的第一个位置

```javascript
 $('<a href="#">路飞学诚</a>').prependTo('ul');
```

 

###### 知识点5：兄弟之间

语法：

```javascript
兄弟元素.after(要插入的兄弟元素)；
要插入的兄弟元素.inserAfter(兄弟元素)；
```

解释：在匹配的元素之后插入内容 

```javascript
$('ul').after('<h4>我是一个h3标题</h4>');
$('<h5>我是一个h2标题</h5>').insertAfter('ul');
```

 

###### 知识点6：兄弟之间

语法：

```javascript
兄弟元素.before(要插入的兄弟元素)；
要插入的兄弟元素.inserBefore(兄弟元素)；
```

解释：在匹配的元素之后插入内容 

```javascript
$('ul').before('<h3>我是一个h3标题</h3>');
$('<h2>我是一个h2标题</h2>').insertBefore('ul');
```



##### 二、替换操作

###### 知识点1：

语法：

```
$(selector).replaceWith(content);

```

将所有匹配的元素替换成指定的string、js对象、jquery对象。

```
//将所有的h5标题替换为a标签
$('h5').replaceWith('<a href="#">hello world</a>');
//将所有h5标题标签替换成id为app的dom元素
$('h5').replaceWith($('#app'));

```

###### 知识点2：

语法：

```
$('<p>哈哈哈</p>').replaceAll('h2');

```

解释：替换所有。将所有的h2标签替换成p标签。

```
$('<br/><hr/><button>按钮</button>').replaceAll('h4');

```

##### 三、删除操作

###### 知识点1：

语法：

```
$(selector).remove(); 

```

解释：删除节点后，事件也会删除（简言之，删除了整个标签）

```
$('ul').remove();

```

 

###### 知识点2：

语法：

```
$(selector).detach(); 

```

解释：删除节点后，事件会保留

```
 var $btn = $('button').detach()
 //此时按钮能追加到ul中
 $('ul').append($btn)
```

 

###### 知识点3：

语法：

```
$(selector).empty(); 

```

解释：清空选中元素中的所有后代节点

```
//清空掉ul中的子元素，保留ul
$('ul').empty()
```

### jQuery的位置信息

#### 一、宽度和高度

##### 获取宽度

```
.width()
```

描述：为匹配的元素集合中获取第一个元素的当前计算宽度值。这个方法不接受任何参数。`.css(width)` 和 `.width()`之间的区别是后者返回一个没有单位的数值（例如，`400`），前者是返回带有完整单位的字符串（例如，`400px`）。当一个元素的宽度需要数学计算的时候推荐使用`.width()` 方法 。

##### 设置宽度

```
.width( value )
```

描述：给每个匹配的元素设置CSS宽度。

 

##### 高度

##### 获取高度

```
.height()
```

描述：获取匹配元素集合中的第一个元素的当前计算高度值。

- 这个方法不接受任何参数。

##### 设置高度

```
 .height( value )
```

描述：设置每一个匹配元素的高度值。

 

#### 二、innerHeight()和innerWidth()

##### 获取内部宽

```
.innerWidth()
```

描述：为匹配的元素集合中获取第一个元素的当前计算宽度值,包括padding，但是不包括border。

ps:这个方法不适用于`window` 和 `document`对象，对于这些对象可以使用`.width()`代替。

 

##### 设置内部宽

```
.innerWidth(value);
```

描述： 为匹配集合中的每个元素设置CSS内部宽度。如果这个“value”参数提供一个数字，jQuery会自动加上像素单位（px）

##### 获取内部高

```
.innerHeight();
```

描述：为匹配的元素集合中获取第一个元素的当前计算高度值,包括padding，但是不包括border。

ps:这个方法不适用于`window` 和 `document`对象，对于这些对象可以使用`.height()`代替。

 

##### 设置内部宽

```
.innerHeight(value);
```

描述： 为匹配集合中的每个元素设置CSS内部高度。如果这个“value”参数提供一个数字，jQuery会自动加上像素单位（px）

 

#### 三、outerWidth和outerHeight()

 

##### 获取外部宽

```
 .outerWidth( [includeMargin ] )
```

描述：获取匹配元素集合中第一个元素的当前计算外部宽度（包括padding，border和可选的margin）

- includeMargin (默认: `false`)

  类型： `Boolean`

  一个布尔值，表明是否在计算时包含元素的margin值。

- 这个方法不适用于`window` 和 `document`对象，可以使用`.width()`代替

##### 设置外部宽

```
 .outerWidth( value )
```

描述： 为匹配集合中的每个元素设置CSS外部宽度。

 

##### 获取外部宽

```
 .outerHeight( [includeMargin ] )
```

描述：获取匹配元素集合中第一个元素的当前计算外部高度（包括padding，border和可选的margin）

- includeMargin (默认: `false`)

  类型： `Boolean`

  一个布尔值，表明是否在计算时包含元素的margin值。

- 这个方法不适用于`window` 和 `document`对象，可以使用`.width()`代替

##### 设置外部高

```
 .outerHeight( value )
```

描述： 为匹配集合中的每个元素设置CSS外部高度。

 

 

#### 四、偏移

##### 获取

```
.offset()
```

返回值：[Object](http://www.shouce.ren/api/view/a/13081#articleHeader15) 。`.offset()`返回一个包含`top` 和 `left`属性的对象 。

描述：在匹配的元素集合中，获取的第一个元素的当前坐标，坐标相对于文档。

注意：jQuery不支持获取隐藏元素的偏移坐标。同样的，也无法取得隐藏元素的 border, margin, 或 padding 信息。若元素的属性设置的是 `visibility:hidden`，那么我们依然可以取得它的坐标

 

##### 设置

```
 .offset( coordinates )
```

描述： 设置匹配的元素集合中每一个元素的坐标， 坐标相对于文档。

- coordinates

  类型: [Object](http://www.shouce.ren/api/view/a/13081#articleHeader25)

  一个包含`top` 和 `left`属性的对象，用整数指明元素的新顶部和左边坐标。

例子：

```
$("p").offset({ top: 10, left: 30 });
```

 

 

 

#### 五、滚动距离

##### 水平方向获取：

```
.scrollLeft()
```

描述：获取匹配的元素集合中第一个元素的当前水平滚动条的位置（页面卷走的宽度）

 

##### 水平方向设置：

```
.scrollLeft( value )
```

描述：设置每个匹配元素的水平方向滚动条位置。

 

##### 垂直方向获取：

```
.scrollTop()
```

描述：获取匹配的元素集合中第一个元素的当前迟滞滚动条的位置（页面卷走的高度）

 

##### 垂直方向获取：

```
.scrollLeft( value )
```

描述：设置每个匹配元素的垂直方向滚动条位置。



在学习jQuery的事件之前，大家必须要对JS的事件有所了解。看下文

### 事件的概念

HTML中与javascript交互是通过事件驱动来实现的，例如鼠标点击事件、页面的滚动事件onscroll等等，可以向文档或者文档中的元素添加事件侦听器来预订事件。想要知道这些事件是在什么时候进行调用的，就需要了解一下“事件流”的概念。

#### 什么是事件流

事件流描述的是从页面中接收事件的顺序

1、DOM事件流

“DOM2级事件”规定的事件流包括三个阶段：

① 事件捕获阶段；

② 处于目标阶段；

③ 事件冒泡阶段

那么其实呢，js中还有另外一种绑定事件的方式：看下面代码：

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>事件流</title>
    <script>

    window.onload = function(){

        var oBtn = document.getElementById('btn');

        oBtn.addEventListener('click',function(){
            console.log('btn处于事件捕获阶段');
        }, true);
        oBtn.addEventListener('click',function(){
            console.log('btn处于事件冒泡阶段');
        }, false);

        document.addEventListener('click',function(){
            console.log('document处于事件捕获阶段');
        }, true);
        document.addEventListener('click',function(){
            console.log('document处于事件冒泡阶段');
        }, false);

        document.documentElement.addEventListener('click',function(){
            console.log('html处于事件捕获阶段');
        }, true);
        document.documentElement.addEventListener('click',function(){
            console.log('html处于事件冒泡阶段');
        }, false);

        document.body.addEventListener('click',function(){
            console.log('body处于事件捕获阶段');
        }, true);
        document.body.addEventListener('click',function(){
            console.log('body处于事件冒泡阶段');
        }, false);

    };

    </script>
</head>
<body>
    <a href="javascript:;" id="btn">按钮</a>
</body>
</html>
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

当我们点击这个btn的时候，看看页面都输出了什么：

![img](https://images2018.cnblogs.com/blog/1364810/201806/1364810-20180603175814247-1842858419.png)

 

 在解释输出结果为什么是这样之前，还有几个知识点需要了解一下即可：

1、addEventListener

addEventListener 是DOM2 级事件新增的指定事件处理程序的操作，这个方法接收3个参数：要处理的事件名、作为事件处理程序的函数和一个布尔值。最后这个布尔值参数如果是true，表示在捕获阶段调用事件处理程序；如果是false，表示在冒泡阶段调用事件处理程序。

2、document、documentElement和document.body三者之间的关系：

document代表的是整个html页面；

document.documentElement代表的是`<html>`标签；

document.body代表的是`<body>`标签；

接着我们就来聊聊上面的例子中输出的结果为什么是这样：

在标准的“DOM2级事件”中规定，事件流首先是经过事件捕获阶段，接着是处于目标阶段，最后是事件冒泡阶段。这里可以画个图示意一下:

#### DOM2级事件图示

![img](https://images2018.cnblogs.com/blog/1364810/201806/1364810-20180603175954421-2080548028.png)

 

首先在事件捕获过程中，document对象首先接收到click事件，然后事件沿着DOM树依次向下，一直传播到事件的实际目标，就是id为btn的a标签。

接着在事件冒泡过程中，事件开始时由最具体的元素（a标签）接收，然后逐级向上传播到较为不具体的节点（document）。

需要注意的点：由于老版本的浏览器不支持事件捕获，因此在实际开发中需要使用事件冒泡，在由特殊需要时再使用事件捕获

补充知识了解即可：

1、IE中的事件流只支持“事件冒泡”，但是版本到了IE9+以后，实现了“DOM2级事件”，也就是说IE9+以后也可以在捕获阶段对元素进行相应的操作。

2、在DOM事件流中，实际的目标在“捕获阶段”不会接收到事件。而是在“处于目标阶段”被触发，并在事件处理中被看成“冒泡阶段”的一部分。然后，“冒泡阶段”发生，事件又传播回文档。

### jquery的常用事件

jquery常用的事件，大家一定要熟记在心

![img](https://images2018.cnblogs.com/blog/1364810/201806/1364810-20180603180055274-1034449014.png)

#### 解决单双击的冲突问题

```javascript
//定义setTimeout执行方法
var time = null;

$('div').click(function () {
    // 取消上次延时未执行的方法
    clearTimeout(time);
    //执行延时
    time = setTimeout(function(){
        //do function在此处写单击事件要执行的代码
    },300);
});

$('div').dblclick(functin () {
    // 取消上次延时未执行的方法
    clearTimeout(time);
    //双击事件的执行代码
});
```



### 事件委托 

通俗的讲，事件就是onclick，onmouseover，onmouseout，等就是事件，委托呢，就是让别人来做，这个事件本来是加在某些元素上的，然而你却加到别人身上来做，完成这个事件。
　　举个列子：有三个同事预计会在周一收到快递。为签收快递，有两种办法：一是三个人在公司门口等快递；二是委托给前台MM代为签收。现实当中，我们大都采用委托的方案（公司也不会容忍那么多员工站在门口就为了等快递）。前台MM收到快递后，她会判断收件人是谁，然后按照收件人的要求签收，甚至代为付款。这种方案还有一个优势，那就是即使公司里来了新员工（不管多少），前台MM也会在收到寄给新员工的快递后核实并代为签收。

**原理：**

　　利用冒泡的原理，把事件加到父级上，触发执行效果。

 

**作用：**

1.性能要好
2.针对新创建的元素，直接可以拥有事件

**事件源 :**

　　跟this作用一样(他不用看指向问题，谁操作的就是谁),event对象下的

**使用情景：**

　　•为DOM中的很多元素绑定相同事件；
　　•为DOM中尚不存在的元素绑定事件； 

### jQuery的ajax

#### 什么是ajax

AJAX = 异步的javascript和XML（Asynchronous Javascript and XML）

简言之，在不重载整个网页的情况下，AJAX通过后台加载数据，并在网页上进行显示。

通过 jQuery AJAX 方法，您能够使用 HTTP Get 和 HTTP Post 从远程服务器上请求文本、HTML、XML 或 JSON - 同时您能够把这些外部数据直接载入网页的被选元素中。

#### jquery的$.ajax()方法（重要）

先记住参数1、2、6、7、10、11

http://www.baidu.com/home

http://www.baidu.com/music

![image-20180910172234894](/var/folders/7b/sz6pt5jd3y3b51q1ngm_8pph0000gn/T/abnerworks.Typora/image-20180910172234894.png)

```
jquery的$.ajax()方法 是做ajax技术经常使用的一个方法。

它的参数很多，总会有一些初学者记不住，在这里，演示几个经常使用的参数。后面讲django课程部分会详细讲ajax技术的原理。大家先把每个参数做个笔记。
 
参数如下： 

1.url: 要求为String类型的参数，（默认为当前页地址）发送请求的地址。

2.type: 要求为String类型的参数，请求方式（post或get）默认为get。注意其他http请求方法，例如put和delete也可以使用，但仅部分浏览器支持。

3.timeout: 要求为Number类型的参数，设置请求超时时间（毫秒）。此设置将覆盖$.ajaxSetup()方法的全局设置。

4.async: 要求为Boolean类型的参数，默认设置为true，所有请求均为异步请求。如果需要发送同步请求，请将此选项设置为false。注意，同步请求将锁住浏览器，用户其他操作必须等待请求完成才可以执行。

5.cache: 要求为Boolean类型的参数，默认为true（当dataType为script时，默认为false），设置为false将不会从浏览器缓存中加载请求信息。

6.data: 要求为Object或String类型的参数，发送到服务器的数据。如果已经不是字符串，将自动转换为字符串格式。get请求中将附加在url后。防止这种自动转换，可以查看　　processData选项。对象必须为key/value格式，例如{foo1:"bar1",foo2:"bar2"}转换为&foo1=bar1&foo2=bar2。如果是数组，JQuery将自动为不同值对应同一个名称。例如{foo:["bar1","bar2"]}转换为&foo=bar1&foo=bar2。

7.dataType: 要求为String类型的参数，预期服务器返回的数据类型。如果不指定，JQuery将自动根据http包mime信息返回responseXML或responseText，并作为回调函数参数传递。可用的类型如下：

 

　　xml：返回XML文档，可用JQuery处理。

　　html：返回纯文本HTML信息；包含的script标签会在插入DOM时执行。

　　script：返回纯文本JavaScript代码。不会自动缓存结果。除非设置了cache参数。注意在远程请求时（不在同一个域下），所有post请求都将转为get请求。

　　json：返回JSON数据。

　   jsonp：JSONP格式。使用SONP形式调用函数时，例如myurl?callback=?，JQuery将自动替换后一个“?”为正确的函数名，以执行回调函数。

　　text：返回纯文本字符串。

8.beforeSend： 要求为Function类型的参数，发送请求前可以修改XMLHttpRequest对象的函数，例如添加自定义HTTP头。在beforeSend中如果返回false可以取消本次ajax请求。XMLHttpRequest对象是惟一的参数。 function(XMLHttpRequest){ this; //调用本次ajax请求时传递的options参数 } 9.complete：

要求为Function类型的参数，请求完成后调用的回调函数（请求成功或失败时均调用）。参数：XMLHttpRequest对象和一个描述成功请求类型的字符串。 function(XMLHttpRequest, textStatus){ this; //调用本次ajax请求时传递的options参数 }

10.success：

　　要求为Function类型的参数，请求成功后调用的回调函数，有两个参数。

　　(1)由服务器返回，并根据dataType参数进行处理后的数据。

　　(2)描述状态的字符串。 function(data, textStatus){ //data可能是xmlDoc、jsonObj、html、text等等 

11.error: 要求为Function类型的参数，请求失败时被调用的函数。该函数有3个参数，即XMLHttpRequest对象、错误信息、捕获的错误对象(可选)。ajax事件函数如下： function(XMLHttpRequest, textStatus, errorThrown){ //通常情况下textStatus和errorThrown只有其中一个包含信息 this; //调用本次ajax请求时传递的options参数 }

12.contentType： 要求为String类型的参数，当发送信息至服务器时，内容编码类型默认为"application/x-www-form-urlencoded"。该默认值适合大多数应用场合。

13.dataFilter： 要求为Function类型的参数，给Ajax返回的原始数据进行预处理的函数。提供data和type两个参数。data是Ajax返回的原始数据，type是调用jQuery.ajax时提供的dataType参数。函数返回的值将由jQuery进一步处理。 function(data, type){ //返回处理后的数据 return data; }

14.dataFilter： 要求为Function类型的参数，给Ajax返回的原始数据进行预处理的函数。提供data和type两个参数。data是Ajax返回的原始数据，type是调用jQuery.ajax时提供的dataType参数。函数返回的值将由jQuery进一步处理。 function(data, type){ //返回处理后的数据 return data; }

15.global： 要求为Boolean类型的参数，默认为true。表示是否触发全局ajax事件。设置为false将不会触发全局ajax事件，ajaxStart或ajaxStop可用于控制各种ajax事件。

16.ifModified： 要求为Boolean类型的参数，默认为false。仅在服务器数据改变时获取新数据。服务器数据改变判断的依据是Last-Modified头信息。默认值是false，即忽略头信息。

17.jsonp： 要求为String类型的参数，在一个jsonp请求中重写回调函数的名字。该值用来替代在"callback=?"这种GET或POST请求中URL参数里的"callback"部分，例如{jsonp:'onJsonPLoad'}会导致将"onJsonPLoad=?"传给服务器。

18.username： 要求为String类型的参数，用于响应HTTP访问认证请求的用户名。

19.password： 要求为String类型的参数，用于响应HTTP访问认证请求的密码。

20.processData： 要求为Boolean类型的参数，默认为true。默认情况下，发送的数据将被转换为对象（从技术角度来讲并非字符串）以配合默认内容类型"application/x-www-form-urlencoded"。如果要发送DOM树信息或者其他不希望转换的信息，请设置为false。

21.scriptCharset： 要求为String类型的参数，只有当请求时dataType为"jsonp"或者"script"，并且type是GET时才会用于强制修改字符集(charset)。通常在本地和远程的内容编码不同时使用
```

![image-20180910174413765](/var/folders/7b/sz6pt5jd3y3b51q1ngm_8pph0000gn/T/abnerworks.Typora/image-20180910174413765.png)





![image-20180910175048258](/var/folders/7b/sz6pt5jd3y3b51q1ngm_8pph0000gn/T/abnerworks.Typora/image-20180910175048258.png)



### 和风天气API

大家不要拿着我的key来玩啊，一天只能访问4000次，你们的好像是访问1000次（不要开定时器访问）

![image-20180910225929964](/var/folders/7b/sz6pt5jd3y3b51q1ngm_8pph0000gn/T/abnerworks.Typora/image-20180910225929964.png)

```html

<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title></title>
</head>
<body>
	<div class="tmp"></div>
	<div class="city"></div>
	<img src="" alt="">
	<script type="text/javascript" src="jquery-3.3.1.js"></script>
	<script type="text/javascript">
		$(function(){
			$.ajax({
				url:'https://free-api.heweather.com/s6/weather/now?location=beijing&key=4693ff5ea653469f8bb0c29638035976',
				type:"get",
				success:function (data) {
					console.log(data.HeWeather6[0].now.tmp);
					// 温度
					var tmp = data.HeWeather6[0].now.tmp;
					// 城市
					var city = data.HeWeather6[0].basic.location;
					// 天气状况码
					var cond_code= data.HeWeather6[0].now.cond_code;

					// 后面方法的参数使用的是es6的模板字符串拼接的变量
					$('.tmp').text(`${tmp}℃`);
					$('.city').text(city);
					// 后面的地址是使用的和风天气的天气状况cdn资源。您也可以使用本地图片加载
					$('img').attr('src',`https://cdn.heweather.com/cond_icon/${cond_code}.png`);

				}
			})
		});
	</script>
</body>
</html>
```

以上代码是请求的和风天气的实况天气的api。

大家可以去请求未来三天的天气api。提升一下自己的能力（不做强制要求）