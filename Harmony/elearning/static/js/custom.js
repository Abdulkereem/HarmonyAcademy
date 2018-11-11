function myFunction() {
    var input, filter, ul, li, a, i;
    input = document.getElementById("myInput");
    filter = input.value.toUpperCase();
    ul = document.getElementById("MyUL");
    li = ul.getElementsByClassName("list");
    for (i = 0; i < li.length; i++) {
        a = li[i].getElementsByTagName("p")[0];
        if (a.innerHTML.toUpperCase().indexOf(filter) > -1) {
            if (li[i].classList.length > 1){
                li[i].classList.remove('revile');
            }    
        } else {
            li[i].classList.add("revile");
        }
    }
}
var buttons = ["teacher", "student"];
function menubar(val) {
    var unselected = []
    var choice = document.getElementById(val);
    for (var i = 0; i <= buttons.length - 1; i++) {''
        if (buttons[i] == val){
            if (val == "teacher"){
                document.getElementById("teacher_select").style.display = 'block';
                document.getElementById("student_select").style.display = 'none';
            }
            else{
                document.getElementById("student_select").style.display = 'block';
                document.getElementById("teacher_select").style.display = 'none';
            }
            continue;
        }
        else {
            unselected.push(buttons[i]);
        }
    }
    for (var i = 0; i < unselected.length; i++){
        if (document.getElementById(unselected[i]).classList.length > 0){
            document.getElementById(unselected[i]).classList.remove('choice');
        }
    }
    choice.classList.add("choice");
    /*console.log(current_session);*/
}
var clickable = document.getElementById('file_collector');
var New_val;
function file_collect(){
    clickable.click();
}
function file_passer(){
    val = clickable.value;
    New_val = val.substr(12, (val.length - 1));
    document.getElementById("ex_change").value = New_val;
}

function check(){
    if (document.getElementById('ex_change').value <= 0){
        alert("please upload your cv")
        document.getElementById("T_form").action = "javascript:void(0)"
    }
    else{
        document.getElementById("T_form").action = "home.html";
    }
}