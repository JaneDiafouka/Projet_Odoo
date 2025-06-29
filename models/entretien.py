# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class Entretien(models.Model):
    _name = 'parc.automobile.entretien'
    _description = "Objet Entretien"
    
    
    name = fields.Char(string="Numéro d'entretien", required=True)
    montant = fields.Float(string="Montant total")
    type_entretien = fields.Selection(string="Type d'entretien",
        selection=[('vidange', 'Vidange'),
                   ('change', 'Changement des pièces'),
                   ('revision', 'Révision')],
        default=''
    )
    type_maintenance = fields.Selection(string="Type de Maintenance", required=True,
        selection=[('entretien', 'entretien'),
                   ('reparation', 'reparation'),], 
        default='reparation'
    )
    date_entretien = fields.Date(string="Date d'entretien")
    cout = fields.Integer(string='Côut')
    date_prochain_entretien = fields.Date(string="Prochain Entretien")
    description_entretien = fields.Text(string="Description")
    devise = fields.Selection([
        ('FCFA', 'FCFA'),
        ('EURO', 'EURO(s)'),
        ('DOLLAR', 'DOLLAR(s)')
    ], string="devise", required=True, default='FCFA')


    # @api.model
    # def _cron_notify_date_prochain_entretien(self):
    #     today = fields.Date.today()
    #     entretiens = self.search([('date_prochain_entretien', '=', today)])
    #     for entretien in entretiens:
    #         _logger.info(f"Entretien prévu aujourd'hui pour le véhicule {entretien.voiture_id.name}")
    
    
    
    
    
    