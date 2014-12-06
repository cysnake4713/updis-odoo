__author__ = 'cysnake4713'

# coding=utf-8
from openerp import tools
from openerp import models, fields, api
from openerp.tools.translate import _


class ProjectProject(models.Model):
    _name = 'up.project.project'
    _inherit = ['mail.thread', 'ir.needaction_mixin']

    name = fields.Char('Name')
    # TODO: change this to configurable
    state = fields.Selection([("project_active", u"Project Active"),
                              ("project_cancelled", u"Project Cancelled"),
                              ("project_processing", u"Project Processing"),
                              ("project_stop", u"Project Stop"),
                              ("project_pause", u"Project Pause"),
                              ("project_filed", u"Project Filing"),
                              ("project_finish", u"Project Filed"),
                             ], string="State", track_visibility='onchange')
