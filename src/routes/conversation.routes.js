const express = require('express')
const router = express.Router()
const { creerConversation, listerConversations } = require('../controllers/conversation.controller')

router.post('/', creerConversation)
router.get('/:id_utilisateur', listerConversations)

module.exports = router