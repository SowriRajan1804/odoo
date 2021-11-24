from odoo import models, fields, api
import datetime


class staff(models.Model):
    _name = 'school.staff'
    _description = 'school.staff'

    name = fields.Char()
    work=fields.Selection([
            ('teach', 'Teaching'),
            ('non_teach', 'Non_Teaching'),
             ], )
    salary=fields.Integer()
    subject = fields.Selection([
            ('teach', 'Teaching'),
            ('non_teach', 'Non_Teaching'),
             ],)
    age = fields.Date(default=datetime.datetime.now())
    perform=fields.Integer(String="last year performance")
    status=fields.Char(compute="_perform",store="true")
    img=fields.Image("Logo", max_width=128, max_height=128)

    def create_method(self):

            for record in self:

                record.create({'name':"kiklkjlkjlk"})
                # print(text)
            print("name")

    @api.depends('age')
    def _perform(self):

        for record in self:
            current=datetime.datetime.now().year
            # record.status=current


            print(type(record.age))
            print(record.age)
            print(current)

            record.status=record.age.year



