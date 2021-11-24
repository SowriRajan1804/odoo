# -*- coding: utf-8 -*-
# from odoo import http


# class Pubg(http.Controller):
#     @http.route('/pubg/pubg/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pubg/pubg/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pubg.listing', {
#             'root': '/pubg/pubg',
#             'objects': http.request.env['pubg.pubg'].search([]),
#         })

#     @http.route('/pubg/pubg/objects/<model("pubg.pubg"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pubg.object', {
#             'object': obj
#         })
