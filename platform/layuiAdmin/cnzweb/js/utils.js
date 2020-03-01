function get_projects(call_back) {
    layui.$.ajax({
        url: host + '/api/project',
        method: 'get',
        success: function (data) {
            call_back(data);
        }
    })
}

function add_project(project_data) {
    project = project_data;
    var str = '';
    for (let num in project_data.data) {
        var item = project_data.data[num];
        var project_name = item.name;
        var project_id = item.id;
        str += '<option value="' + project_id + '">' + project_name + '</option>'
    }
    layui.$('#project').append(str);
    layui.form.render('select');
}

function fill_interface_for_project_id(project_id) {
    layui.$.ajax({
        url: host + '/api/interface',
        data: {project_id: project_id},
        method: 'get',
        success: function (data) {
            layui.$('#interface').empty();
            let interface_data = data.data;
            var str = '';
            for (let num in interface_data) {
                var item = interface_data[num];
                var interface_name = item.name;
                var interface_id = item.id;
                str += '<option value="' + interface_id + '">' + interface_name + '</option>'
            }
            layui.$('#interface').append(str);
            layui.form.render('select');
        }
    })
}


function addParams(tab_id) {
    // 目的 将两个input 两个按钮 放到页面上
    // insertAdjacentHTML 将html的字符串添加到页面上
    // let childCount = document.getElementById(tab_id).childElementCount;
    // 解决 bug  由于 特殊操作 会导致childCount和下一个相同，所以这里修改为使用时间戳
    let timeTmp = new Date().valueOf(); // 时间戳
    let params_key = `${tab_id}_key_${timeTmp}`;
    let params_value = `${tab_id}_value_${timeTmp}`;
    let css_selector = tab_id == 'params' ? 'kv_div' : 'header_div';
    // if(tab_id == 'params'){
    //     return 'kv_div'
    // }else {
    //     return ''
    // }
    let html = `<div class="layui-form-item ${css_selector}" > <div class="layui-input-inline"><input type="text" name="${params_key}" required lay-verify="required"  placeholder="key" autocomplete="on" class="layui-input"> </div> <div class="layui-input-inline" style="margin-left: 10px"><input type="text" name="${params_value}" required lay-verify="required"  placeholder="value" autocomplete="on" class="layui-input"></div> <button type="button" class="layui-btn " lay-filter="add_input" onclick="addParams('${tab_id}')"  >增加</button> <button type="button" class="layui-btn-danger layui-btn" onclick="deleteParams('${tab_id}',this)">删除</button> </div>`
    document.getElementById(tab_id).insertAdjacentHTML('beforeEnd', html)
}


function deleteParams(tab_id, ths) {
    let css_selector = tab_id == 'params' ? 'kv_div' : 'header_div';
    let element = document.getElementsByClassName(css_selector);
    let tab_obj = document.getElementById(tab_id);

    if (element.length == 1) {
        layer.alert('没有了不能再删了。')
    } else {
        tab_obj.removeChild(ths.parentElement);
    }
}


function get_data(data) {
    default_headers = {};
    default_params = {};
    for (let key in data) {
        // 通过判断headers 是否在key中 来判断是否数据是参数或header
        if (key.indexOf('headers_key') != -1) {
            // 获得header中填写的key
            let header_key = data[key];
            // 根据key 替换取value的key
            let header_value_str = key.replace('headers_key', 'headers_value');
            // 取出 key对应的value
            let header_value = data[header_value_str];
            // 添加到临时的map中
            default_headers[header_key] = header_value;
            // 删除key 和value 保证提交的数据干净
            delete data[key];
            delete data[header_value_str];
        } else if (key.indexOf('params_key') != -1) {
            let params_key = data[key];
            let params_value_str = key.replace('params_key', 'params_value');
            let params_value = data[params_value_str];
            if (params_key && params_value){
                default_params[params_key] = params_value;
            }
            delete data[key];
            delete data[params_value_str];
        }
    }
    // 根据接口文档 添加需要的key
    data['headers'] = Object.keys(default_headers).length > 0 ? JSON.stringify(default_headers):null;
    data['params'] = Object.keys(default_params).length > 0 ? JSON.stringify(default_params):null;

    return data

}


function fill_interface_for_edit_data(interface_id, interface_name) {
    // 先删掉默认的请选择的option
    layui.$('#interface').empty();
    let optionStr = `<option value="${interface_id}">${interface_name}</option>`;
    layui.$('#interface').append(optionStr);
}


// 例子填充方法
function demo_fill(data) {
    // 0、每次填充时需要 先删掉默认的空的 input
    layui.$('.kv_div').remove();
    // 1、根据后台返回的参数的格式，来判断填充的方法
    let params = data.params;
    // 2、由于后端返回的params是字符串  将获取到的params 变成对象
    let paramsObj = JSON.parse(params);
    // 3、根据paramsObj 进行 循环，每次循环生成一对input
    // {"username":"niuhanyang"}
    for (let item in paramsObj) {
        // 4、取key 和 value
        let key = item;
        let value = paramsObj[item];
        // 4.1 定义时间戳 用于区分每次循环的两个input的name属性保持唯一。
        // 定义时间戳的目的，根据时间戳来拼接name  能够自成一对
        let time = new Date().valueOf();
        // 5、拼接字符串
        let html = `<div class="layui-form-item kv_div"><div class="layui-input-inline"><input type="text" name="params_key_${time}"  value="${key}" placeholder="key" autocomplete="on" class="layui-input"></div><div class="layui-input-inline" style="margin-left: 10px"><input type="text" name="params_value_${time}" value="${value}" placeholder="value" autocomplete="on" class="layui-input"></div><button type="button" class="layui-btn " lay-filter="add_input" onclick="addParams('params')">增加</button><button type="button" class="layui-btn-danger layui-btn" onclick="deleteParams('params',this)">删除</button></div>`;
        // 6、将拼好的html 渲染到页面上
        let element = document.getElementById('params');
        element.insertAdjacentHTML('beforeEnd', html)
    }
}


// es6 语法的类已经和 python很像了
// 1、 根据处理的是参数还是header来区分开kv_div、header_div
// 2、根据是参数还是header 来取不同的数据  如： params Headers
// 3、div的class 属性 需要根据是参数还是header进行替换
// 4、name属性也需要根据参数还是header进行替换
// 5、添加时 需要判断 参数还是header 插入的的父元素不相同。

class fillInput {
    fill(tab_id, data) {
        // tab_id : params  headers
        this.tab_id = tab_id;
        this.data = data;
        // 根据tabid 取 对应数据
        this.fillData = this.get_data();
        // 将字符串转对象
        // 如果 fillData 为空 则不填充
        // 为了参数中的json数据而做的特殊处理 必须保证isjson为真 并且处理的是params 才可以去渲染json
        if (this.data.is_json && this.tab_id == 'params') {
            this.fillJson();
        } else {
            // fillData 需要有数据才去填充
            if (this.fillData) {
                this.fillData = JSON.parse(this.fillData);
                this.fillKv();
            }

        }
    }

    fillJson(){
        layui.$('.kv_div').css('display','none');
        layui.$('#json_div').css('display','')
    }

    fillKv() {
        // 根据params 和 headers 来判断 divclass
        let divFlag = this.tab_id == 'params' ? 'kv_div' : 'header_div';
        // 根据class 进行删除默认的那对input
        layui.$(`.${divFlag}`).remove();
        let index=0;
        for (let item in this.fillData) {
            let key = item;
            let value = this.fillData[item];
            // 由于渲染太快导致时间戳一样，所以废弃这个方法
            // let time = new Date().valueOf();
            // class、删除和添加的第一个参数也要替换、两个input的name属性也要替换
            let html = `<div class="layui-form-item ${divFlag}"><div class="layui-input-inline"><input type="text" name="${this.tab_id}_key_${index}"  value="${key}" placeholder="key" autocomplete="on" class="layui-input"></div><div class="layui-input-inline" style="margin-left: 10px"><input type="text" name="${this.tab_id}_value_${index}" value="${value}" placeholder="value" autocomplete="on" class="layui-input"></div><button type="button" class="layui-btn " lay-filter="add_input" onclick="addParams('${this.tab_id}')">增加</button><button type="button" class="layui-btn-danger layui-btn" onclick="deleteParams('${this.tab_id}',this)">删除</button></div>`;
            // 根据tab_id 定位到父级
            let element = document.getElementById(this.tab_id);
            // 进行插入
            element.insertAdjacentHTML('beforeEnd', html)
            index+=1;

        }
    }


    get_data() {
        // 如果是header  就返回header数据
        if (this.tab_id == 'headers') {
            return this.data.headers;
        } else {
            // 返回params的数据;
            return this.data.params;
        }
    }
}

// class fillInput(Object):
//     def fillParams(self,name):
//         self.name = name
//         self.consoleParams()
//
//     def consoleParams(self):
//         print(self.name)








