function wrong_answer(){
    var comment = document.getElementById("comment");
    comment.innerHTML = 'Incorrect Answer'
}

function initialize_inventory(){
    localStorage.setItem("inventory", "");
}

function add_item(item){
    var list = localStorage.getItem("inventory");
    var array = list.split(",");
    array.push(item);
    var new_array = array.join(",");
    localStorage.setItem("inventory", new_array);
}

function get_inventory(){
    var list = localStorage.getItem("inventory");
    var array = list.split(",");
    return array;
}

function create_inventory(){
    var list = document.getElementById('inventory_list_2');
    var array = get_inventory();
    
    for (var i = 0; i < array.length; i++) {
        var item = document.createElement('li');
        item.textContent = array[i];
        list.appendChild(item);
    }
}