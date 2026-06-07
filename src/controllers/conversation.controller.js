const { Op } = require('sequelize')
const Conversation = require('../models/Conversation')

const creerConversation = async (req, res) => {
  try {
    const { id_utilisateur1, id_utilisateur2 } = req.body

    const existante = await Conversation.findOne({
      where: { id_utilisateur1, id_utilisateur2 }
    })

    if (existante) {
      return res.status(200).json(existante)
    }

    const conversation = await Conversation.create({
      id_utilisateur1,
      id_utilisateur2
    })

    res.status(201).json(conversation)
  } catch (err) {
    res.status(500).json({ message: 'Erreur serveur', erreur: err.message })
  }
}

const listerConversations = async (req, res) => {
  try {
    const { id_utilisateur } = req.params

    const conversations = await Conversation.findAll({
      where: {
        [Op.or]: [
          { id_utilisateur1: id_utilisateur },
          { id_utilisateur2: id_utilisateur }
        ]
      }
    })

    res.status(200).json(conversations)
  } catch (err) {
    res.status(500).json({ message: 'Erreur serveur', erreur: err.message })
  }
}

module.exports = { creerConversation, listerConversations }