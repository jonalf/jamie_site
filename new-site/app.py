from flask import Flask, request, render_template
import os
#from flask_frozen import Freezer
#import sys

site = Flask( __name__ )

#freezer = Freezer( site )

GALLERY_LOCATION = 'static/img/galleries'

@site.route( '/' )
def root():
    return render_template( 'main.html' )

@site.route( '/bio' )
def bio():
    return render_template( 'bio.html' )

@site.route( '/resume' )
def resume():
    return render_template( 'resume.html' )

@site.route( '/audio' )
def audio():
    return render_template( 'main.html' )

@site.route( '/video' )
def video():
    return render_template( 'main.html' )

@site.route( '/photos' )
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
    print all_pics
    return render_template( 'photos.html', all_pics = all_pics )

@site.route( '/contact' )
def contact():
    return render_template( 'main.html' )

if __name__ == '__main__':
    #if len(sys.argv) > 1 and sys.argv[1] == "build":
    #    FREEZER_RELATIVE_URLS = True
    #    freezer.freeze()
    #else:
    site.debug = True
    site.run()
    
