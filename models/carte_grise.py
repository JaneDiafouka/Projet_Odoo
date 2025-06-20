# -*- coding: utf-8 -*-

from odoo import models, fields, api, _ 
from odoo.exceptions import ValidationError

class CarteGrise(models.Model):
    _name = 'parc.automobile.carte.grise'
    _description = "Objet Carte Grise"
    
    
    
    name = fields.Char(string="Numéro de carte grise", required=True, copy=False, readonly=True, 
                       index=True,default=lambda self: 'Nouvelle carte grise')
    date_delivrance = fields.Date(string="Date de délivrance")
    lieu_delivrance = fields.Char(string="Lieu de délivrance")
    date_expiration = fields.Date(string="Date d'expiration")
    
    
    @api.model
    def create(self, vals):
        if vals.get('name', 'Nouvelle carte grise') == 'Nouvelle carte grise':
            vals['name'] = self.env['ir.sequence'].next_by_code('parc.automobile.carte.grise') or 'Nouvelle carte grise'
        return super().create(vals)
    
    
    @api.constrains('date_delivrance', 'date_expiration')
    def _check_dates(self):
        for record in self:
            if record.date_delivrance and record.date_expiration:
                if record.date_delivrance > record.date_expiration:
                    raise ValidationError(_("La date de délivrance ne peut pas être supérieure à la date d'expiration."))
    
    
    
    
    