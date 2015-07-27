from flask_frozen import Freezer
from app import site

site.config['FREEZER_DESTINATION'] = '../../jamie_site_live/'
site.config['FREEZER_BASE_URL'] = 'file:///Users/jdyrlandweaver/github/jamie_site_live'
#site.config['SERVER_NAME'] = 'file:///Users/jdyrlandweaver/github/jamie_site_live'

"""
site.add_url_rule('/static/<path:filename>',
                 endpoint='static',
                 subdomain='static',
                 view_func=site.send_static_file)
"""

freezer = Freezer( site )

if __name__ == '__main__':
    freezer.freeze()
