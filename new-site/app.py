from flask import Flask, request, render_template
import os
#from flask_frozen import Freezer
#import sys

site = Flask( __name__ )

#freezer = Freezer( site )

GALLERY_LOCATION = 'static/img/galleries'
GALLERIES = { 'Cabaret':'cabaret', 'Carousel':'carousel', 'The Marvelous Wonderettes':'marvelous' }

@site.route( '/' )
def root():
    return render_template( 'main.html' )

@site.route( '/bio.html' )
def bio():
    return render_template( 'bio.html' )

@site.route( '/resume.html' )
def resume():
    return render_template( 'resume.html' )

@site.route( '/audio.html' )
def audio():
    return render_template( 'main.html' )

@site.route( '/video.html' )
def video():
    return render_template( 'main.html' )

@site.route( '/photos/<GAL_NAME>' )
@site.route( '/photos.html' )
def photos(GAL_NAME = None):

    if not GAL_NAME:
        gs = {}
        for gallery in GALLERIES:
            gs[ gallery ] = GALLERY_LOCATION + '/' + GALLERIES[gallery] + '/thumbs/1.jpg'
        return render_template( "photos.html", galleries = gs)
    else:
        return render_template( "main.html" )
    
"""
def photos():
    location = [GALLERY_LOCATION]
    all_pics = []
    galleries = os.listdir( location[0] + '/' )
    for g in galleries: 
        location.append(g)
        gallery = os.listdir( '/'.join(location) )
        pics = []
        for p in gallery:
            location.append( p )
            #print '/'.join( location )
            pics.append( '/'.join( location ) )
            location.pop()
        all_pics.append( pics )
        location.pop()
    #print all_pics
    return render_template( 'photos.html', all_pics = all_pics )
"""

@site.route( '/contact.html' )
def contact():
    return render_template( 'main.html' )

if __name__ == '__main__':
    #if len(sys.argv) > 1 and sys.argv[1] == "build":
    #    FREEZER_RELATIVE_URLS = True
    #    freezer.freeze()
    #else:
    site.debug = True
    site.run()
    
