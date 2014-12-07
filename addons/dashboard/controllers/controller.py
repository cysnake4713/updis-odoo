__author__ = 'cysnake4713'
from openerp import http
from openerp.http import request


class DashboardController(http.Controller):
    @http.route('/dashboard/index', type='http', auth='public', website=True)
    def index(self):
        return request.website.render("dashboard.index", {})