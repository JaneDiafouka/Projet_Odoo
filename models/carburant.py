from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class CarburantConsommation(models.Model):
    _name = 'parc.automobile.carburant'
    _description = 'Consommation de carburant'


    name = fields.Char(string='Nom', required=True, copy=False, readonly=True, default='Nouvelle consommation')
    date = fields.Date(string="Date", required=True)
    litres = fields.Float(string="Quantité (litres)", required=True)
    kilometres_parcourus = fields.Float(string="Kilomètres parcourus", required=True)
    consommation_moyenne = fields.Float(string="Consommation moyenne (L/100km)", compute="_compute_consommation_moyenne", store=True)
    commentaire = fields.Text(string="Remarque / Station")
    voiture_id = fields.Many2one('parc.automobile.voiture', string="Voiture Associée", required=False)

    @api.model
    def create(self, vals):
        rec = super().create(vals)
        if rec.consommation_moyenne > 15:  # seuil arbitraire
            _logger.warning(f"⚠️ Anomalie conso : {rec.voiture_id.name} a consommé {rec.consommation_moyenne:.2f} L/100km")
        return rec

    @api.model
    def create(self, vals):
        if vals.get('name', 'Nouvelle consommation') == 'Nouvelle consommation':
            vals['name'] = self.env['ir.sequence'].next_by_code('parc.automobile.carburant') or 'Nouvelle consommation'
        return super().create(vals)
