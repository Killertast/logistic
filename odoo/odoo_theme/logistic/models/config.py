from odoo import api, fields, models

class Config_rider(models.Model):
    _name = "config.rider"
    _description = "Config rider"
   
    name = fields.Char('Name')
    phone = fields.Integer('Phone')
    
class Configvillage(models.Model):
    _name = "config.village"
    _description = "Config village"
    
    village = fields.Char('Village') 
    
class Configdistrict(models.Model):
    _name = "config.district"
    _description = "Config district"
    
    district = fields.Char('District') 
    
class Configprovince(models.Model):
    _name = "config.province"
    _description = "Config province"
    
    province = fields.Char('Province') 