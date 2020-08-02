document.addEventListener('DOMContentLoaded', () => {
  var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port)
  socket.on('connect', () => {
    console.log("Connection established")
    documnt.querySelector('button').onclick = () => {
      
    }
  })
})
