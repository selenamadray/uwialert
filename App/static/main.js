
const server = "https://uwi-alert-default-rtdb.firebaseio.com/"

async function getUserData(){
    const response = await fetch('/api/users');
    return response.json();
}

function loadTable(users){
    const table = document.querySelector('#result');
    for(let user of users){
        table.innerHTML += `<tr>
            <td>${user.id}</td>
            <td>${user.username}</td>
        </tr>`;
    }
}
f
function notifTable(reports){
    const table = document.querySelector('#result');
    for(let report of reports){
        table.innerHTML += `<tr>
            <td>${report.type}</td>
            <td>${report.location}</td>
            <td>${report.date}</td>
            <td>${report.details}</td>
        </tr>`;
    }
}

async function main(){
    const users = await getUserData();
    loadTable(users);
}



main();