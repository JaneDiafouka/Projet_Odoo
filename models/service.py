from odoo import models, fields

class FleetCentre(models.Model):
    _name = 'parc.automobile.centre'
    _description = 'Centre / Service'

    name = fields.Char(string="Nom du centre", required=True)
    code = fields.Char(string="Code du centre")
    responsable = fields.Many2one('res.partner', string="Responsable")
    adresse = fields.Char(string="Adresse")
    telephone = fields.Char(string="Téléphone")
    email = fields.Char(string="Email")