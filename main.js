const { spawn } = require('child_process')
const express = require('express')

spawn('python', ['main.py'])

const app = express()
app.use('/', express.static('public'))

app.listen(8000, () => {
  console.log('listening on port 8000')
})