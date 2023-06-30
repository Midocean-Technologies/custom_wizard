# -*- coding: utf-8 -*-
# from odoo import http


# class CustomWizard(http.Controller):
#     @http.route('/custom_wizard/custom_wizard', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_wizard/custom_wizard/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_wizard.listing', {
#             'root': '/custom_wizard/custom_wizard',
#             'objects': http.request.env['custom_wizard.custom_wizard'].search([]),
#         })

#     @http.route('/custom_wizard/custom_wizard/objects/<model("custom_wizard.custom_wizard"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_wizard.object', {
#             'object': obj
#         })
