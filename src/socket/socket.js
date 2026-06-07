const socketIO = require('socket.io')

const initSocket = (server) => {
  const io = socketIO(server, {
    cors: {
      origin: '*',
      methods: ['GET', 'POST']
    }
  })

  io.on('connection', (socket) => {
    console.log(`Utilisateur connecté : ${socket.id}`)

    // Rejoindre une conversation
    socket.on('join_conversation', (id_conversation) => {
      socket.join(id_conversation)
      console.log(`Utilisateur a rejoint la conversation : ${id_conversation}`)
    })

    // Envoyer un message
    socket.on('send_message', (data) => {
      io.to(data.id_conversation).emit('receive_message', data)
    })

    // Envoyer une notification
    socket.on('send_notification', (data) => {
      io.to(data.id_destinataire).emit('new_notification', data)
    })

    // Déconnexion
    socket.on('disconnect', () => {
      console.log(`Utilisateur déconnecté : ${socket.id}`)
    })
  })

  return io
}

module.exports = initSocket