# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime,date,timedelta

class lod_pds_report(models.Model):
    _inherit = 'ir.config_parameter' 
    
     
    def auto_set_date_expiry_database(self):    
            
        expiry = self.search(
            [
            ('key','=','database.expiration_date'), 
            ])
        for res in expiry: 
            expiration_date = res.value
            current_datetime = fields.Datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            if expiration_date < current_datetime:
                print('Expiration date has passed:', current_datetime)
                res.value=fields.Datetime.now() + timedelta(days=30)
              
 
    
    def _cron_auto_expiry_database(self):  
        ir_cron_id = self.env.ref('yun_dev_database_expiry.ir_cron_auto_database_expiry') 
        trigger_obj = self.env['ir.cron.trigger'].sudo()
        trigger_obj.create({
            'cron_id': ir_cron_id.id,
            'call_at': fields.Datetime.now() + timedelta(minutes=3),
            
        })


class BrandModel(models.Model):
    _name = 'mod.model'
    
    name = fields.Char('name')
    brand_id = fields.Many2one('mod.brand', string='brand')
    
class ModelBrand(models.Model): 
    _name = "mod.brand" 
    name = fields.Char('name')
    
class ChangeBrand(models.Model): 
    _name = "mod.brand.change"
    
    name = fields.Char('name')
    brand_id = fields.Many2one('mod.brand', string='brand')
    model_id = fields.Many2one('mod.model', string='model')
    
    # @api.onchange('brand_id')
    # def sub_project_ids_onchange(self): 
    #     if self.brand_id:
    #         return {'domain': {'model_id': [('brand_id','=', self.brand_id.id)]}}
    #     else:
    #         return {'domain': {'model_id': []}}  
    