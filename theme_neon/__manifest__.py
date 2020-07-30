# -*- coding: utf-8 -*-

{
    'name': 'Theme Neon',
    'category': 'Theme/Ecommerce',
    'summary': """Multipurpose Premium Responsive Odoo Themes""",
    'version': '1.4',
    'sequence': 1000,
    'author': 'Atharva System',
    'license' : 'OPL-1',
    'support': 'support@atharvasystem.com',
    'website' : 'https://www.atharvasystem.com',
    'description': """
    Theme Neon is  All in One Odoo theme with responsive, customize  & beautifully designed.
    Multipurpose Premium Responsive Odoo Themes - Fashion, Furniture, Sports, Jewellery, Corporate.
Creative theme,
Ecommerce theme,
Entertainment theme,
Personal theme,
Services theme,
Technology theme,
Business theme,
Multipurpose odoo theme,
Multi-purpose theme,
Theme Neon, 
Odoo new themes,
Neon Theme
Bootstrap4 odoo themes,
eCommerce Businesses,
Fashio Theme,
Food Theme,
Sports Theme,
Bicycle Theme,
Watch Theme,
Accessories Theme,
Bag Theme,
Gym Theme,
Coffee Theme,
Electronic Gadgets Theme,
Odoo RTL Theme,
Right to left theme
        """,
    'depends': ['atharva_theme_general','website_theme_install'],
    'data': [
        'views/assets.xml',
        'views/customize_theme_templates.xml',
        'views/snippets.xml',
    ],
    'demo': [
        'data/demo.xml',
    ],
    'live_test_url': 'http://theme-neon.atharvasystem.com',
    'images': ['static/description/neon_banner.png','static/description/neon_banner_screenshot.gif'],
    'price': 135.00,
    'currency': 'EUR',
    'application': True,
}
