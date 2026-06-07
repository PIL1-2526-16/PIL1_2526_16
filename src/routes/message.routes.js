const express = require('express')
const router = express.Router()
const { envoyerMessage, listerMessages, marquerCommeLu } = require('../controllers/message.controller')

router.post('/', envoyerMessage)
router.get('/:id_conversation', listerMessages)
router.put('/:id_message/lu', marquerCommeLu)

module.exports = router