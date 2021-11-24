# -*- coding: utf-8 -*-
import datetime
from odoo import models, fields, api


class hospital(models.Model):
    _name = 'hospital.hospital'
    _description = 'hospital.hospital'

    name = fields.Char()
    department = fields.Char()
    doc_reg_no = fields.Integer()
    dob = fields.Date()
    doc_age = fields.Integer(compute="age_calc", store = True)
    salary = fields.Float()
    patients = fields.Many2many("patients.patients")
    sale = fields.Many2one("sale.order")



    @api.depends('dob')
    def age_calc(self):
        for record in self:
            if record.dob == False:
                record.dob = datetime.datetime.now()

            record.doc_age = datetime.datetime.now().year - record.dob.year
