# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime


class office(models.Model):
    _name = 'office.office'
    _description = 'office.office'

    first_name = fields.Char()
    last_name = fields.Char()
    employee_id = fields.Integer(string="Employee ID")
    email = fields.Char()
    department = fields.Selection([('accounts','ACCOUNTS'),('manager','MANAGER'),('hr','HR')])
    job_title = fields.Selection([('supervisor','SUPERVISOR'),('team leader','TEAM LEADER'),('developer','DEVELOPER'),('testing','TESTING')])
    location = fields.Selection([('qwer','QWER'),('tyui','TYUI'),('asdf','ASDF'),('ghjk','GHJK'),('zxcv','ZXCV'),('lop','LOP'),('nbm','NBM')])
    work_shift = fields.Selection([('day','DAY'),('night','NIGHT')])
    salary = fields.Char()
    date_of_birth = fields.Date(default=datetime.datetime.now())    #depends onchange
    age = fields.Integer(compute="age_cal",store=True)
    marital_status = fields.Selection([('single','SINGLE'),('married','MARRIED')])
    mobile_number = fields.Integer(sting = "mobile number")     #constraints
    permanent_address = fields.Text()
    city = fields.Selection([('arul','ARUL'),('siva','SIVA'),('sowri','SOWRI')])
    state = fields.Selection([('raj','RAJ'),('prakash','PRAKASH'),('rajan','RAJAN'),('priyan','PRIYAN')])
    pincode = fields.Integer()
    country = fields.Selection([('asguard','ASGUARD'),('atlantis','ATLANTIS'),('krypton','KRYPTON'),('narnia','NARNIA')])


    @api.depends('date_of_birth')
    def age_cal(self):
        for record in self:
            age = datetime.datetime.now().year - record.date_of_birth.year
            record.age = age
