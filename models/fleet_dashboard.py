from odoo import models, fields, api

import logging
_logger = logging.getLogger(__name__)

class ParcDashboard(models.TransientModel):
    _name = 'parc.automobile.dashboard'
    _description = "Vue Tableau de bord du parc"

    total_voitures = fields.Integer(string="Total véhicules", readonly=True)
    nb_voitures_service = fields.Integer(string="En service", readonly=True)
    nb_voitures_panne = fields.Integer(string="Hors service", readonly=True)
    kilometrage_total = fields.Float(string="Kilométrage cumulé", readonly=True)
    nb_entretien = fields.Integer(string="Total entretiens", readonly=True)
    consommation_moyenne = fields.Float(string="Consommation moyenne L/100km", readonly=True)

    def get_all_cars(self):
        voiture_obj = self.env['parc.automobile.voiture']
        all_voitures = voiture_obj.search([])
        count = 0 
        #_logger.info("=== Debug: voitures trouvées === %s", all_voitures)
        for a in all_voitures:
            count += 1 
            _logger.info(a.etat)
        return count


    def action_actualiser_stats(self):
        voiture_obj = self.env['parc.automobile.voiture']
        entretien_obj = self.env['parc.automobile.entretien']
        carburant_obj = self.env['parc.automobile.carburant']

        all_voitures = voiture_obj.search([])
        total_voitures = len(all_voitures)
        nb_en_service = len(all_voitures.filtered(lambda v: v.etat == 'service'))
        nb_hors_service = len(all_voitures.filtered(lambda v: v.etat == 'hs'))
        kilometrage_total = sum(float(v.kilometrage) for v in all_voitures if v.kilometrage)

        consommations = carburant_obj.search([])
        total_litres = sum(c.litres for c in consommations)
        total_km = sum(c.kilometres_parcourus for c in consommations)
        consommation_moyenne = (total_litres / total_km * 100) if total_km > 0 else 0

        for rec in self:
            rec.total_voitures = total_voitures
            rec.nb_voitures_service = nb_en_service
            rec.nb_voitures_panne = nb_hors_service
            rec.kilometrage_total = kilometrage_total
            rec.nb_entretien = entretien_obj.search_count([])
            rec.consommation_moyenne = consommation_moyenne
            return {
                        'type': 'ir.actions.act_window',
                        'res_model': self._name,
                        'view_mode': 'form',
                        'res_id': rec.id,
                        'target': 'new',
                        'views': [(self.env.ref('parc_automobile.view_form_parc_automobile_dashboard').id, 'form')],
                    }