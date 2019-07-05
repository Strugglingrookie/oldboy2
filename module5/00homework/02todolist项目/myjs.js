function $(id) {
	return document.getElementById(id);
}

function clear() {
	localStorage.clear();
	load();
}

function postaction() {
	if($('title').value == ''){
		alert('不可为空！')
	}else{
		var data = loadData();
		var todo = {'title':$('title').value,'done':false};
		data.push(todo);
		saveData(data);
		$('form').reset();
		load();
	}
}

function loadData() {
	var collection = localStorage.getItem('todo');
	if(collection){
		return JSON.parse(collection);
	}else{
		return [];
	}
}

function saveData(data) {
	localStorage.setItem('todo',JSON.stringify(data))
}

function remove(i) {
	var data = loadData();
	data.splice(i,1);
	saveData(data);
	load();
}

function update(i,field,value) {
	var data = loadData();
	var todo = data.splice(i,1)[0];
	todo[field] = value;
	data.splice(i,0,todo);
	saveData(data);
	load();
}

function edit(i) {
	load();
	var p = document.getElementById('p-'+i);
	title = p.innerHtml;
	p.innerHTML =  "<input id='input-" + i + "' value='" + title + "' />";
	var input = $("input-" + i);
	input.setSelectionRange(0,input.value.length);  // 选中value
	input.focus();
	input.onblur = function () {
		if(input.value.length == 0){
			p.innerHTML = title;
			alert('不能为空！');
		}else{
			update(i,'title',input.value);
		}
    }
}

function load() {
	var todolist = $('todolist');
	var donelist = $('donelist');
	var collection = localStorage.getItem('todo');
	if(collection != null){
		var data = JSON.parse(collection);
		var todoCount = 0;
        var doneCount = 0;
        var todoString = "";
        var doneString = "";
        for(var i = data.length - 1;i >= 0; i--){
        	if(data[i].done){
        		doneString += "<li draggable='true'><input type='checkbox' onchange='update(" + i + ",\"done\",false)' checked='checked' />" +
                    "<p id='p-" + i + "' onclick='edit(" + i + ")'>" + data[i].title + "</p>" +
                    "<a href='javascript:remove(" + i + ")'>-</a></li>";
                doneCount++;
			}else{
        		todoString += "<li draggable='true'><input type='checkbox' onchange='update(" + i + ",\"done\",true)' />" +
                    "<p id='p-" + i + "' onclick='edit(" + i + ")'>" + data[i].title + "</p>" +
                    "<a href='javascript:remove(" + i + ")'>-</a></li>";
                todoCount++;
			}
		}
		todocount.innerHTML = todoCount;
        todolist.innerHTML = todoString;
        donecount.innerHTML = doneCount;
        donelist.innerHTML = doneString;
	}else{
		todocount.innerHTML = 0;
        todolist.innerHTML = "";
        donecount.innerHTML = 0;
        donelist.innerHTML = "";
	}
}

window.onload = load;