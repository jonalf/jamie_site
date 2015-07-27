from flask_frozen import Freezer
from app import site
from socket import gethostname

if gethostname() == 'fry':
    BASE_URL = 'http://fry.jonalf.com/jamie_site_live'
else:
    BASE_URL = 'file:///Users/jdyrlandweaver/github/jamie_site_live'
    
site.config['FREEZER_DESTINATION'] = '../../jamie_site_live/'
site.config['FREEZER_BASE_URL'] = BASE_URL

freezer = Freezer( site )

if __name__ == '__main__':
    freezer.freeze()
