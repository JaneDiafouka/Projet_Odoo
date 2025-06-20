# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Affectation(models.Model):
    _name = 'parc.automobile.affectation'
    _description = "Objet Affectation"
    
    
    name = fields.Char(string='Nom', required=True, copy=False, readonly=True, 
                        index=True,default=lambda self: 'Nouvelle affectation')
    date_debut_affectation = fields.Date(string="Date de debut d'affectation",  required=True)
    date_fin_affectation = fields.Date(string="Date de fin d'affectation",  required=True)
    client_id = fields.Many2one('parc.automobile.client', string="Client Associé", required=False)
    employe_id = fields.Many2one('parc.automobile.employe', string="Employe Associée", required=False)
    description = fields.Text(string='Description')
    
    _sql_constraints = [
        ('unique_client_id', 'unique(client_id)', 'Chaque affectation ne peut avoir qu\'un seul client.'),
        ('unique_employe_id', 'unique(employe_id)', 'Chaque affectation ne peut avoir qu\'un seul employe.')
    ]
    
    @api.model
    def create(self, vals):
        if vals.get('name', 'Nouvelle affectation') == 'Nouvelle affectation':
            vals['name'] = self.env['ir.sequence'].next_by_code('parc.automobile.affectation') or 'Nouvelle affectation'
        return super().create(vals)
    
    
    