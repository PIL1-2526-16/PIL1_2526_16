const express = require('express')
const router = express.Router()
const { listerNotifications, marquerCommeLue } = require('../controllers/notification.controller')

router.get('/:id_utilisateur', listerNotifications)
router.put('/:id_notification/lu', marquerCommeLue)

module.exports = router