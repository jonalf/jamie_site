from flask_frozen import Freezer
from app import site

freezer = Freezer( site )

if __name__ == '__main__':
    freezer.freeze()
