function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function FetchDistributeDiv() {

    var div = document.getElementById('action_div');
    div.innerHTML = 'Loading...'

    var xhttp = new XMLHttpRequest();
    var url = '/hos/fetchdistributediv';
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var rtxt = (xhttp.responseText);
            div.innerHTML = rtxt;
        }
    };
    xhttp.open("GET", url, true);
    xhttp.send();
}

function Distribute() {
    var vac_code = document.getElementById('vac_code').value;
    var vac_num = document.getElementById('vac_num').value;
    var rate_parm = document.getElementById('rate_parm').value;
    var ratio_parm = document.getElementById('ratio_parm').value;

    var div = document.getElementById('assigned_list');
    div.innerHTML = 'Loading...'

    var data = new FormData();
    data.append('vac_code', vac_code);
    data.append('vac_num', vac_num);
    data.append('rate_parm', rate_parm);
    data.append('ratio_parm', ratio_parm);

    var xhttp = new XMLHttpRequest();
    var url = '/hos/distributevaccine/';
    var csrftoken = getCookie('csrftoken');

    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var rtxt = (xhttp.responseText);
            div.innerHTML = rtxt;
        }
    };
    xhttp.open("post", url, true);
    xhttp.setRequestHeader("X-CSRFToken", csrftoken);
    xhttp.send(data);

}


function Assign() {
    document.getElementById('assign_btn').disabled = true;

    var div = document.getElementById('action_div');

    var vac_code = document.getElementById('vac_code').value;
    var vac_num = document.getElementById('vac_num').value;
    var rate_parm = document.getElementById('rate_parm').value;
    var ratio_parm = document.getElementById('ratio_parm').value;

    var data = new FormData();
    data.append('vac_code', vac_code);
    data.append('vac_num', vac_num);
    data.append('rate_parm', rate_parm);
    data.append('ratio_parm', ratio_parm);

    var xhttp = new XMLHttpRequest();
    var url = '/hos/assignvaccine/';
    var csrftoken = getCookie('csrftoken');

    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var rtxt = (xhttp.responseText);
            div.innerHTML = rtxt;
        }
    };
    xhttp.open("post", url, true);
    xhttp.setRequestHeader("X-CSRFToken", csrftoken);
    xhttp.send(data);
}

function FetchQueueDiv() {

    var div = document.getElementById('action_div');
    div.innerHTML = 'Loading...'

    var xhttp = new XMLHttpRequest();
    var url = '/hos/fetchqueuediv';
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var rtxt = (xhttp.responseText);
            div.innerHTML = rtxt;
        }
    };
    xhttp.open("GET", url, true);
    xhttp.send();
}

function UpdateQueue() {
    var date = document.getElementById('vac_num').value;
    var per = document.getElementById('ratio_parm').value;
    var div = document.getElementById('action_div');

    var data = new FormData();
    data.append('date', date);
    data.append('per', per);

    var xhttp = new XMLHttpRequest();
    var url = '/hos/fetchqueuediv/';
    var csrftoken = getCookie('csrftoken');

    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var rtxt = (xhttp.responseText);
            div.innerHTML = rtxt;
        }
    };
    xhttp.open("post", url, true);
    xhttp.setRequestHeader("X-CSRFToken", csrftoken);
    xhttp.send(data);
}

function FetchUsersDiv() {
    var div = document.getElementById('action_div');
    div.innerHTML = 'Loading...'

    var xhttp = new XMLHttpRequest();
    var url = '/hos/fetchuserdiv';
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var rtxt = (xhttp.responseText);
            div.innerHTML = rtxt;
        }
    };
    xhttp.open("GET", url, true);
    xhttp.send();
}

function FetchHospitalsDiv() {
    var div = document.getElementById('action_div');
    div.innerHTML = 'Loading...'

    var xhttp = new XMLHttpRequest();
    var url = '/hos/fetchhospitalsdiv';
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var rtxt = (xhttp.responseText);
            div.innerHTML = rtxt;
        }
    };
    xhttp.open("GET", url, true);
    xhttp.send();
}

function RegisterHospital() {
    var div = document.getElementById('action_div');
    div.innerHTML = 'Registering...'

    var xhttp = new XMLHttpRequest();
    var url = '/hos/registerhospital';
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var rtxt = (xhttp.responseText);
            div.innerHTML = rtxt;
        }
    };
    xhttp.open("GET", url, true);
    xhttp.send();
}

function Cancel() {
    document.getElementById('vac_code').value = '';
    document.getElementById('vac_num').value = '';
    document.getElementById('rate_parm').value = '';
    document.getElementById('ratio_parm').value = '';
}

// Function to download data to a file
function download(data, filename, type) {
    var file = new Blob([data], {type: type});
    if (window.navigator.msSaveOrOpenBlob) // IE10+
        window.navigator.msSaveOrOpenBlob(file, filename);
    else { // Others
        var a = document.createElement("a"),
                url = URL.createObjectURL(file);
        a.href = url;
        a.download = filename;
        document.body.appendChild(a);
        a.click();
        setTimeout(function() {
            document.body.removeChild(a);
            window.URL.revokeObjectURL(url);
        }, 0);
    }
}

function GetDailyReport(){
    var xhttp = new XMLHttpRequest();
    var url = '/hos/dailyreport';
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            alert(xhttp.getResponseHeader('filename'))
            // alert(xhttp.getAllResponseHeaders())
            download(xhttp.response,xhttp.getResponseHeader('filename'),'.pdf')
        }
    };
    xhttp.responseType='blob'
    xhttp.open("GET", url, true);
    xhttp.send();
}