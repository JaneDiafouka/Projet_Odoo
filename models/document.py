# -*- coding: utf-8 -*-

from odoo import models, fields, api, _ 
from odoo.exceptions import ValidationError

class Document(models.Model):
    _name = 'parc.automobile.document'
    _description = "Objet Document"

    type_document = fields.Selection([
            ('assurance', 'Assurance'),
            ('controle_technique', 'Controle technique'),
            ('vignette', 'Vignette'),
        ], string="Type de Document", required=True)

    name = fields.Char(string="Numero de document", required=True, copy=False, readonly=True, 
                       index=True,default=lambda self: 'Nouveau document')
    date_delivrance = fields.Date(string="Date de délivrance")
    lieu_delivrance = fields.Char(string="Lieu de délivrance")
    date_expiration = fields.Date(string="Date d'expiration")

    voiture_id = fields.Many2one('parc.automobile.voiture', string="Voiture", required=False)

    @api.model
    def create(self, vals):
        if vals.get('name', 'Nouveau document') == 'Nouveau document':
            vals['name'] = self.env['ir.sequence'].next_by_code('parc.automobile.document') or 'Nouveau document'
        return super().create(vals)


    @api.constrains('date_delivrance', 'date_expiration')
    def _check_dates(self):
        for record in self:
            if record.date_delivrance and record.date_expiration:
                if record.date_delivrance > record.date_expiration:
                    raise ValidationError(_("La date de délivrance ne peut pas être supérieure à la date d'expiration."))
    