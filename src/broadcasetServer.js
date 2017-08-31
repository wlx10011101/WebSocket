let WebSocketServer = require('ws').Server,
websocket = new WebSocketServer({ port: 8181 });

let socketPool = {};

let tetrisList = [];

let shapeNum = 7;

websocket.on('connection', function (ws) {
    console.log('client connected');
    ws.on('message', function (message) {
        resObj = JSON.parse(message);
        switch(resObj['action']) {
            case 'createRoom':
                console.log('createRoom');
                createRoom(resObj['data'], ws)
                break;
            case 'joinRoom':
                console.log('joinRoom');
                joinRoom(resObj['data'], ws)
                break;
            case 'start':
                console.log('start');
                startGame(resObj['data'])
                break;
            default:
                break;
        }
        // for (let i=0; i<users.length; i++) {
        // 	users[i].send(message);
        // }
        console.log('data updated');
    });
});

websocket.on('close', function(ws) {
    console.log('ws closed')
})


function createRoom (roomId, ws) {
    if (socketPool[roomId] === undefined) {
        socketPool[roomId] = [ws]
    }
    ws.send('success')
}

function joinRoom (roomId, ws) {
    if (socketPool[roomId] === undefined) {
        ws.send('room not exist')
        return
    } else if (socketPool[roomId].length == 2)  {
        ws.send('room is full')
        return
    } else {
        socketPool[roomId].push(ws);
        socketPool[roomId][0].send('ready')
    }

}

function startGame (roomId) {
    for (let i=0; i<socketPool[roomId].length; i++) {
        socketPool[roomId][i].send('start')
    }
}

function generateRandomId(originList) {
	for (let i=0; i< 254; i++) {
		originList.push(Math.floor( Math.random() * shapeNum ));
	}
}