const ip = "192.168.0.106:8000";

let add_participant_html = (data) => {
    let id_list = Object.keys(data)
    let user_list_html = document.getElementById("users_list");
    
    let subheader_span = document.getElementById("main_subheader_span");
    subheader_span.innerHTML = id_list.length;
    user_list_html.innerHTML = "";

    for(i=0; i<id_list.length; i++){
        user_list_html.innerHTML += `
        <div class="card" style="width: auto; float: left; margin: 10px;">
            <div class="card-body">
                <h4 class="card-title"><b>${data[id_list[i]]}</b><br><span style="font-size: 85%;">joined</h4>
                <a href="#" class="btn btn-warning" style="float: right">${id_list[i]}</a>
            </div>
        </div>
        `;
    }
}

let get_registered_participants = ()=>{
    $.ajax({
        type: 'GET',
        url: `http://${ip}/api/get/registered_users` ,
        success: (data) => {                          
            add_participant_html(data);
            setTimeout(function(){get_registered_participants();},2000);
        }
    })

}

get_registered_participants();