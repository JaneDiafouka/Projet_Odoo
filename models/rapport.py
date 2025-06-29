import io
import xlsxwriter
from odoo.http import request, content_disposition

class ParcDashboard(models.TransientModel):
    _name = 'parc.automobile.dashboard'
    _description = "Vue Tableau de bord du parc"
    
@http.route('/parc/carburant/export_excel', type='http', auth="user")
def export_excel(self):
    output = io.BytesIO()
    workbook = xlsxwriter.Workbook(output)
    sheet = workbook.add_worksheet("Consommation")

    sheet.write(0, 0, "Véhicule")
    sheet.write(0, 1, "Litres")
    sheet.write(0, 2, "Km")
    ...

    workbook.close()
    output.seek(0)

    return request.make_response(output.read(), [
        ('Content-Type', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'),
        ('Content-Disposition', content_disposition('rapport_consommation.xlsx'))
    ])
