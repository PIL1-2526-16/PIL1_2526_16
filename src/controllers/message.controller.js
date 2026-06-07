const Message = require('../models/Message')
const Notification = require('../models/Notification')

// Envoyer un message
const envoyerMessage = async (req, res) => {
  try {
    const { id_conversation, id_expediteur, contenu } = req.body

    const message = await Message.create({
      id_conversation,
      id_expediteur,
      contenu
    })

    // Créer une notification
    await Notification.create({
      id_destinataire: req.body.id_destinataire,
      type: 'message',
      contenu: 'Vous avez reçu un nouveau message'
    })

    res.status(201).json(message)
  } catch (err) {
    res.status(500).json({ message: 'Erreur serveur', erreur: err.message })
  }
}

// Lister les messages d'une conversation
const listerMessages = async (req, res) => {
  try {
    const { id_conversation } = req.params

    const messages = await Message.findAll({
      where: { id_conversation },
      order: [['date_envoi', 'ASC']]
    })

    res.status(200).json(messages)
  } catch (err) {
    res.status(500).json({ message: 'Erreur serveur', erreur: err.message })
  }
}

// Marquer un message comme lu
const marquerCommeLu = async (req, res) => {
  try {
    const { id_message } = req.params

    await Message.update(
      { lu: true },
      { where: { id_message } }
    )

    res.status(200).json({ message: 'Message marqué comme lu ✅' })
  } catch (err) {
    res.status(500).json({ message: 'Erreur serveur', erreur: err.message })
  }
}

module.exports = { envoyerMessage, listerMessages, marquerCommeLu }