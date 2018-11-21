// This script constantly fetches the submissions data, sorts it acc to the score
// and updates the webpage every 2 seconds
// The audience gets a nice real time view of how all the players are doing

const ip = "192.168.0.106:8000"

let sort_submission_data = (data) => {
    if(data.length == 1){
        return data
    }

    let id = Object.keys(data);
    let flag = true;

    // bubble sort
    while(flag){
        flag = false

        for(i=0; i<id.length-1; i++){
            let a = data[id[i]][1].reduce((x,y) => x+y, 0) // finding the sum of the scores
            let b = data[id[i+1]][1].reduce((x,y) => x+y, 0)
            
            if(a<b){ // swapping
                let temp = data[id[i]]
                data[id[i]] = data[id[i+1]]
                data[id[i+1]] = temp

                flag = true
            }   
        }
    }
    // console.log(data)
    return data
}

let add_submissions_html = (data) => {
    let id_list = Object.keys(data)
    
    let total_submissions_html = document.getElementById("main_subheader_span")
    total_submissions_html.innerHTML = id_list.length
    
    let data_sorted = sort_submission_data(data);
    let id_data_sorted = Object.keys(data_sorted);

    let submissions_html = document.getElementById("submissions_list")
    submissions_html.innerHTML = ""

    for(i=0; i<id_data_sorted.length; i++){
        let score = data_sorted[id_data_sorted[i]][1].reduce((x,y) => x+y, 0);

        submissions_html.innerHTML += `
        <div class="card" style="width: auto; height: 170px; float: left; margin: 10px;">
            <div class="card-body">
                <h5 style="float: right"><span class="badge badge-dark">#${i+1}</span></h5>
                <h4 class="card-title"><b>${data_sorted[id_data_sorted[i]][0]}</b></h4>
                <a class="btn btn-warning" style="float: right; margin: 10px; font-weight: bolder">Score: ${score}</a>
            </div>
        </div>
        `
    }
}

// sending requests every 2 seconds
let get_submissions_data = () => {
    $.ajax({
        type: "GET",
        url: `http://${ip}/api/get/submissions`,
        success: (data) => {
            add_submissions_html(data);
            setTimeout(function(){get_submissions_data();},2000);
        }
    });
}

get_submissions_data();