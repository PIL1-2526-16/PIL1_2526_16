const Notification = require('../models/Notification')

// Lister les notifications d'un utilisateur
const listerNotifications = async (req, res) => {
  try {
    const { id_utilisateur } = req.params

    const notifications = await Notification.findAll({
      where: { id_destinataire: id_utilisateur },
      order: [['date_creation', 'DESC']]
    })

    res.status(200).json(notifications)
  } catch (err) {
    res.status(500).json({ message: 'Erreur serveur', erreur: err.message })
  }
}

// Marquer une notification comme lue
const marquerCommeLue = async (req, res) => {
  try {
    const { id_notification } = req.params

    await Notification.update(
      { lue: true },
      { where: { id_notification } }
    )

    res.status(200).json({ message: 'Notification marquée comme lue ✅' })
  } catch (err) {
    res.status(500).json({ message: 'Erreur serveur', erreur: err.message })
  }
}

module.exports = { listerNotifications, marquerCommeLue }