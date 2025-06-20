# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class ContratLocation(models.Model):
    _name = 'parc.automobile.contrat.location'
    _description = "Objet Contrat de Location" 
    
    
    name = fields.Char(string="Numéro de contrat", required=True, copy=False, readonly=True, 
                       index=True,default=lambda self: 'Nouveau contrat de location')
    date_debut = fields.Date(string="Date de début")
    date_fin = fields.Date(string="Date de fin")
    montant_total = fields.Integer(string="La somme totale")
    voiture_ids = fields.Many2many('parc.automobile.voiture', string="Liste des voitures")
    client_id = fields.Many2one('parc.automobile.client', string="Liste des clients")
    
    
    @api.model
    def create(self, vals):
        if vals.get('name', 'Nouveau contrat de location') == 'Nouveau contrat de location':
            vals['name'] = self.env['ir.sequence'].next_by_code('parc.automobile.contrat.location') or 'Nouveau contrat de location'
        return super().create(vals)
    
    
    
    
    
    