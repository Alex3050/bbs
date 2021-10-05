function getcookie(name) {
    var cookiearray = document.cookie.split(";"); // 分割字符串
    for (var i = 0; i < cookiearray.length; i++){
        var arr = cookiearray[i].split("=")
        if (arr[0] == name){
            return arr[1]
        }
    }
    return ""
}

function sendpost() {
    var form = document.getElementById("posts-form")
    // var form = document.createElement("form")
    // form.method = "post";
    // form.action = "\\page\\send_post\\";
    var content = document.getElementById("write-area");
    content.name = "content";
    // var csrftoken = getcookie("csrftoken")
    document.body.appendChild(form);
    // form.append("csrfmiddlewaretoken", csrftoken)
    form.appendChild(content);
    alert(content)
    form.submit();
    document.body.removeChild(form);
}