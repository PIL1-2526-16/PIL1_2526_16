const { DataTypes } = require('sequelize')
const sequelize = require('../config')

const Message = sequelize.define('Message', {
  id_message: {
    type: DataTypes.INTEGER,
    primaryKey: true,
    autoIncrement: true
  },
  id_conversation: {
    type: DataTypes.INTEGER,
    allowNull: false
  },
  id_expediteur: {
    type: DataTypes.INTEGER,
    allowNull: false
  },
  contenu: {
    type: DataTypes.TEXT,
    allowNull: false
  },
  date_envoi: {
    type: DataTypes.DATE,
    defaultValue: DataTypes.NOW
  },
  lu: {
    type: DataTypes.BOOLEAN,
    defaultValue: false
  }
}, {
  tableName: 'messages',
  timestamps: false
})

module.exports = Message