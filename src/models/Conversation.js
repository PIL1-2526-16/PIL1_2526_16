const { DataTypes } = require('sequelize')
const sequelize = require('../config')

const Conversation = sequelize.define('Conversation', {
  id_conversation: {
    type: DataTypes.INTEGER,
    primaryKey: true,
    autoIncrement: true
  },
  id_utilisateur1: {
    type: DataTypes.INTEGER,
    allowNull: false
  },
  id_utilisateur2: {
    type: DataTypes.INTEGER,
    allowNull: false
  },
  date_creation: {
    type: DataTypes.DATE,
    defaultValue: DataTypes.NOW
  }
}, {
  tableName: 'conversations',
  timestamps: false
})

module.exports = Conversation