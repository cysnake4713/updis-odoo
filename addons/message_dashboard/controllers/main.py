import simplejson
from openerp.http import request

__author__ = 'cysnake4713'
from openerp import http
import openerp


class MessageDashboard(http.Controller):

    @http.route('/dashboard/message', type='http', auth='public', website=True)
    def message(self):
        return request.website.render("message.dashboard", {})

    @http.route('/dashboard/message/detail/<int:message_id>', type='http', auth='public', website=True)
    def detail(self, message_id):
        cr, uid, context = request.cr, request.uid, request.context
        message_obj = request.registry.get('message.message')
        values = {
            'message': message_obj.browse(cr, openerp.SUPERUSER_ID, message_id, context)
        }
        return request.website.render('message.dashboard_detail', values)


    # @http.route('/dashboard/message/list', type='json', auth='public', website=True)
    # def get_messages_by_category(self, category_id, count=10):
    #     cr, uid, context = request.cr, request.uid, request.context
    #     message_obj = request.registry['message.message']
    #     category_obj = request.registry['message.category']
    #     category = category_obj.read(cr, openerp.SUPERUSER_ID, category_id, ['name'], context=context)
    #     message_ids = message_obj.search(cr, openerp.SUPERUSER_ID, [('category_id', '=', int(category_id))], limit=count, context=context)
    #     messages = message_obj.read(cr, openerp.SUPERUSER_ID, message_ids, ['name'], context=context)
    #     return {'category': category, 'messages': messages}