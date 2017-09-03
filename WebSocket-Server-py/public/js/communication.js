let ws = new WebSocket("ws://" + serverIp + ":8181");
let currentRoom = undefined;

ws.onopen = function (e) {
    console.log('Connection to server opened');
}
ws.onClose = function() {
                console.log("Socket closed.");
            }
ws.onError = function() {
                console.log("We got an error.");
            },
ws.onmessage = function (message) {
    switch (message['data']) {
        case 'ready':
            document.getElementById('button-list').innerHTML += '<button onclick="requestForStart()">start</button>'
            return;
        case 'start':
            startGame();
            break;
        default:
            break;
    }
}

function sendMessage(action, value) {
    dataObj = {
        "action": action,
        'data': value
    }
    ws.send(JSON.stringify(dataObj));
}

function createRoom (roomNum) {
    sendMessage('createRoom', roomNum);
    currentRoom = roomNum;
}

function joinRoom (roomNum) {
    sendMessage('joinRoom', roomNum);
    currentRoom = roomNum;
}

function requestForStart() {
    sendMessage('start', currentRoom)
}

function startGame () {
    // setInterval(render, 30);
    // newGame();
}
// ws.onmessage = function (e) {
//     console.log(e);
//     document.getElementById('msg').innerHTML += e.data;
// }