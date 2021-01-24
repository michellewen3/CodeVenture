function fadeInPage() {
    if (!window.AnimationEvent) { return; }
    var fader = document.getElementById('fader');
    fader.classList.add('fade-out');
}

function wrong_answer(){
    var comment = document.getElementById("comment-wrong");
    comment.innerHTML = 'Incorrect Answer'
}

// function initialize_inventory(){
//     localStorage.setItem("inventory", "");
// }

function add_item(item){
    var list = localStorage.getItem("inventory");
    if (list == null) {
        localStorage.setItem("inventory", item);
    }
    else {
        var array = list.split(",");
        array.push(item);
        var new_array = array.join(",");
        localStorage.setItem("inventory", new_array);
    }
    if(item == 'potion'){
        document.getElementById("closedchest_image").src = "/static/img/openchest.png";
    }
}

function create_inventory(){
    var arrayStr = localStorage.getItem("inventory");
    if (arrayStr != null){
        var array = arrayStr.split(",");
        for (var i = 0; i < array.length; i++) {
            var item = document.getElementById(array[i] + '_inventory');
            item.style.visibility = 'visible';
            // var item = document.createElement('li');
            // item.textContent = array[i];
            // list.appendChild(item);
        }
    }
}