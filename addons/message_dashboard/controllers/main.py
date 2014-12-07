from openerp.http import request

__author__ = 'cysnake4713'
from openerp import http
from openerp.addons.dashboard.controllers import controller


class MessageDashboard(controller.DashboardController):
    @http.route('/dashboard/index', type='http', website=True)
    def index(self):
        return request.website.render("message.dashboard", {})

    @http.route('/dashboard/message', type='http', website=True)
    def message(self):
        return request.website.render("message.dashboard", {})

    @http.route('/dashboard/message/detail/<int:message_id>', type='http', website=True)
    def detail(self, message_id):
        cr, uid, context = request.cr, request.uid, request.context
        message_obj = request.registry.get('message.message')
        values = {
            'message': message_obj.browse(cr, uid, message_id, context)
        }
        return request.website.render('message.dashboard_detail', values)