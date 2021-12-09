const robot = require('robotjs')
const ws = require('ws');
const express = require('express')
const fs = require('fs')

// const { spawn } = require('child_process')
var net = require('net');

// var py = new net.Socket();
// py.connect(65432, '127.0.0.1', function () {
//   console.log('Connected');
//   // py.write('5\n8\n50\n10\n80');
// });

const wss = new ws.WebSocketServer({ port: 3001 });
const app = express()

const ACC = 3

// let py = spawn('python', ['move.py'])

// for (let i = 0; i < 10; i++) {
//   console.log('here')
//   py.stdin.write('1,1\n')
//   // py.stdin.end()
// }

// robot.setMouseDelay(1)


// let {x, y} = robot.getMousePos()
// console.log(robot.getMousePos())
// robot.moveMouse(x + 100, y)
// console.log(robot.getMousePos())


// console.log(robot.getMousePos())
// let mouse = robot.getMousePos()
// for (let i = 0; i < 10; i++) {
//   console.log(robot.getMousePos())
//   robot.moveMouse(mouse.x, mouse.y )
//   console.log(robot.getMousePos())
//   console.log('--')
// }

const moveMouse = (xInc, yInc) => {
  // let { x, y } = robot.getMousePos()
  // console.log('x,y: ', x, y)

  xInc = xInc > 0 ? Math.ceil(xInc) : Math.floor(xInc)
  yInc = yInc > 0 ? Math.ceil(yInc) : Math.floor(yInc)
  py.write(`${xInc},${yInc}\n`)
  // console.log(y, yInc)
  // console.log('new: ', x + xInc, y + yInc)
  // robot.moveMouse(x + xInc, y + yInc)
  // console.log(robot.getMousePos())
}


wss.on('connection', socket => {
  console.log('client connected')
  // console.log(socket)
  let lastMoveTs = 0
  socket.on('message', msg => {
    let data = msg.toString()
    console.log(data)

    let [x, y] = data.split(',')
    if (!x || !y) {
      return
    }
    // console.log(+x * ACC, +y * ACC)
    // if (lastMoveTs == 0) {
    //   lastMoveTs = new Date().getTime()
    // }
    // let ts = new Date().getTime()
    // console.log(ts, lastMoveTs, ts - lastMoveTs)
    // let acc = ACC * 10/(ts - lastMoveTs)
    // lastMoveTs = ts
    // console.log(x, y)
    acc = ACC

    moveMouse(x * acc, y * acc)
    // console.log(x, y)
    return

    let [move,fingers] = data.split(':')
    console.log(move, fingers)
    let moves = {
      'panup': () => moveMouse(0, -ACC),
      'pandown': () => moveMouse(0, ACC),
      'panleft': () => moveMouse(-ACC, 0),
      'panright': () => moveMouse(ACC, 0)
    }
    if (!moves[move]) {
      console.log('oi')
      return
    }
    moves[move]()
  })

  socket.on('close', () => {
    console.log('client disconnected')
  })

})

console.log('listening on port 3000')

app.get('/', (req, res) => {
  // console.log(fs.readFileSync('index.html').toString())
  console.log('/')
  // res.send('hello')
  let content = fs.readFileSync('index.html').toString()
  res.send(content)
})

app.get('/manifest.webmanifest', (req, res) => {
  console.log('manifest')
  let content = fs.readFileSync('manifest.webmanifest')
  res.send(content)
})

app.get('/nosleep.min.js', (req, res) => {
  console.log('manifest')
  let content = fs.readFileSync('nosleep.min.js')
  res.send(content)
})

app.listen(8000, () => {
  console.log('listening on port 8000')
})