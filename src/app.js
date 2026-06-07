const express = require('express')
const cors = require('cors')
const app = express()

app.use(cors())
app.use(express.json())

// Routes
const conversationRoutes = require('./routes/conversation.routes')
const messageRoutes = require('./routes/message.routes')
const notificationRoutes = require('./routes/notification.routes')

app.use('/conversations', conversationRoutes)
app.use('/messages', messageRoutes)
app.use('/notifications', notificationRoutes)

app.get('/', (req, res) => {
  res.json({ message: 'MentorLink API en ligne ✅' })
})

module.exports = app