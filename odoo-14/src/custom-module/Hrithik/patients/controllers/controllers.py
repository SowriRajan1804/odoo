# -*- coding: utf-8 -*-
# from odoo import http


# class Patients(http.Controller):
#     @http.route('/patients/patients/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/patients/patients/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('patients.listing', {
#             'root': '/patients/patients',
#             'objects': http.request.env['patients.patients'].search([]),
#         })

#     @http.route('/patients/patients/objects/<model("patients.patients"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('patients.object', {
#             'object': obj
#         })
