from odoo import api, fields, models

class MaintenanceEquipment(models.Model):
    _inherit = 'maintenance.equipment'

    @api.model
    def create(self, vals):
        record = super(MaintenanceEquipment, self).create(vals)
        record.generate_maintenance_request()
        return record

    def write(self, vals):
        res = super(MaintenanceEquipment, self).write(vals)
        for record in self:
            record.generate_maintenance_request()
        return res
# Definimos una nueva función para generar una solicitud de mantenimiento
    def generate_maintenance_request(self):
         # Creamos una nueva solicitud de mantenimiento usando los datos de este registro
        self.env['maintenance.request'].create({
             # El nombre de la solicitud es una combinación de una cadena fija y el nombre del equipo
            'name': 'Maintenance Request for ' + self.name,
            'equipment_id': self.id,
             # La fecha de la solicitud es la fecha de hoy
            'request_date': fields.Date.today(),
            'maintenance_type': 'preventive',
           # Puedes añadir aquí cualquier otro campo que necesites para tus solicitudes de mantenimiento
        })

