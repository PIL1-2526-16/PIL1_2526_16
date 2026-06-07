const app = require('./src/app')
const http = require('http')
const sequelize = require('./src/config')
const initSocket = require('./src/socket/socket')
const server = http.createServer(app)

require('dotenv').config()

const Conversation = require('./src/models/Conversation')
const Message = require('./src/models/Message')
const Notification = require('./src/models/Notification')

const PORT = process.env.PORT || 3000

initSocket(server)

sequelize.sync({ force: false })
  .then(() => {
    console.log('Tables créées ✅')
    server.listen(PORT, () => {
      console.log(`Serveur démarré sur le port ${PORT}`)
    })
  })
  .catch((err) => {
    console.error('Erreur ❌', err)
  })