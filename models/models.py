# -*- coding: utf-8 -*-
from odoo import models, fields, api


class DietFacts(models.Model):
    _name = 'diet_facts.nutrition_facts'
    _inherit = 'product.template'

    _columns = {
        'active': fields.Boolean('Active', default=True,
                                 help="If unchecked, it will allow you to hide the product without removing it."),
        'website_published': fields.Boolean(string='Published',
                                           help="Visible on the website as a comment",
                                           copy=False, default=True),
    }

    # website_published = fields.Boolean(string='Published',
    #                                    help="Visible on the website as a comment",
    #                                    copy=False, default=True)

    product_id = fields.Many2one(comodel_name='product.template',
                                 string='Product')
    nutrients = fields.One2many(comodel_name='diet_facts.nutrient_info',
                                inverse_name='nutrition_facts_id',
                                string='Nutrients')


class Nutrient(models.Model):
    _name = 'diet_facts.nutrient'
    name = fields.Char('Nutrient Name')


class NutrientInfo(models.Model):
    _name = 'diet_facts.nutrient_info'

    nutrition_facts_id = fields.Many2one(
        comodel_name='diet_facts.nutrition_facts')
    nutrient_id = fields.Many2one(comodel_name='diet_facts.nutrient')

    unit_of_measure = fields.Char('Unit of measurement')

    parent_id = fields.Many2one(comodel_name='diet_facts.nutrient')
