const { DataTypes } = require('sequelize')
const sequelize = require('../config')

const Notification = sequelize.define('Notification', {
  id_notification: {
    type: DataTypes.INTEGER,
    primaryKey: true,
    autoIncrement: true
  },
  id_destinataire: {
    type: DataTypes.INTEGER,
    allowNull: false
  },
  type: {
    type: DataTypes.STRING,
    allowNull: false
  },
  contenu: {
    type: DataTypes.TEXT,
    allowNull: false
  },
  lue: {
    type: DataTypes.BOOLEAN,
    defaultValue: false
  },
  date_creation: {
    type: DataTypes.DATE,
    defaultValue: DataTypes.NOW
  }
}, {
  tableName: 'notifications',
  timestamps: false
})

module.exports = Notification