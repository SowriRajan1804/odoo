# -*- coding: utf-8 -*-
# from odoo import http


# class Office(http.Controller):
#     @http.route('/office/office/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/office/office/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('office.listing', {
#             'root': '/office/office',
#             'objects': http.request.env['office.office'].search([]),
#         })

#     @http.route('/office/office/objects/<model("office.office"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('office.object', {
#             'object': obj
#         })
