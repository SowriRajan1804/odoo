# -*- coding: utf-8 -
import datetime
from odoo import models, fields, api


class patients(models.Model):
    _name = 'patients.patients'
    _description = 'patients.patients'

    name = fields.Char()
    patient_no = fields.Integer()
    dob = fields.Date()
    patient_age = fields.Integer(compute="pat_age", store=True)

    @api.depends('dob')
    def pat_age(self):
        for record in self:
            if record.dob == False:
                record.dob = datetime.datetime.now()

            record.patient_age = datetime.datetime.now().year - record.dob.year

