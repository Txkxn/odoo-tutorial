from odoo import api, models, fields

class EstateProperty(models.Model):
    _name = "estate.property" # Apparently a table...
    _description = "Real Estate Properties"

    name = fields.Char(required = True) # single line
    description = fields.Text() # .Text() Multiline 
    expected_price = fields.Float() # Price excpeted
    selling_price = fields.Float() # Price given by market
    bedrooms = fields.Integer() # Self Explanatory
    living_area = fields.Integer() # sqft
    has_garden = fields.Boolean() # True or False
    garden_area = fields.Integer() # sqft(garden) show if has_garden = True

