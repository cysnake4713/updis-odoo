__author__ = 'cysnake4713'

# coding=utf-8
from openerp import tools
from openerp import models, fields, api
from openerp.tools.translate import _


class MessageMessage(models.Model):
    _name = 'message.message'
    _inherit = ['mail.thread', 'ir.needaction_mixin']

    name = fields.Char('Name')
    category_id = fields.Many2one('message.category', 'Message Category')
    content = fields.Html('Content')


class MessageCategory(models.Model):
    _name = 'message.category'

    name = fields.Char('Name')
    active = fields.Boolean('Active')

    _defaults = {
        'active': True,
    }