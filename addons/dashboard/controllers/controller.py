__author__ = 'cysnake4713'
from openerp import http
from openerp.http import request
from openerp import SUPERUSER_ID


class DashboardController(http.Controller):
    @http.route('/dashboard/index', type='http', auth='public', website=True)
    def index(self):
        return request.website.render("dashboard.index", {})


    @http.route('/dashboard/search_read', type="json", auth='public', website=True)
    def search_read(self, model, domain=[], fields=None, limit=10, order=None):
        fields = fields.split(',') if fields else []
        cr, uid, context = request.cr, request.uid, request.context
        target_obj = request.registry[model]
        ids = target_obj.search(cr, SUPERUSER_ID, domain, limit=int(limit), order=order, context=context)
        results = target_obj.read(cr, SUPERUSER_ID, ids, fields, context=context)
        return {'results': results}