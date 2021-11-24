from odoo import models, fields, api


class staff(models.Model):
    _name = 'school.student'
    _description = 'student mark list'

    name=fields.Char()
    tamil=fields.Integer(string="Tamil")
    english=fields.Integer(string="English")
    maths=fields.Integer(string="Maths")
    science=fields.Integer(string="Science")
    social=fields.Integer(string="Social science")
    total=fields.Integer(compute="total_mark")

    def delete_method(self):
        print(self)
        for record in self:
            print(record)
            siva=self.env['school.student'].browse([self.id])
            siva.unlink()

    def edit_method(self):
        for record in self:
            siva = self.env['school.student'].browse([self.id])

            return siva
            # siva.unlink()
            # siva=data.browse([])
            # print(siva)
            # print(siva.name)
            # if siva.exists():
            #     print("yes")
            # else:
            #     print("no")
            # print("sdfdsfdsfdsfd")

    @api.depends('tamil','english','maths','science','social')
    def total_mark(self):
        for record in self:
            record.total = int(record.tamil)+int(record.english)+int(record.maths)+int(record.science)+int(record.social)

class edit(models.Model):
    _name = 'school.edit'
    _description = 'student mark list'

    name=fields.Char()
    tamil=fields.Integer(string="Tamil")
    english=fields.Integer(string="English")
    maths=fields.Integer(string="Maths")
    science=fields.Integer(string="Science")
    social=fields.Integer(string="Social science")
    total=fields.Integer(compute="total_mark")
