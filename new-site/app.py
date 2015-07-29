from flask import Flask, request, render_template, url_for, redirect
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

@site.route( '/photos/<GAL_NAME>.html' )
@site.route( '/photos.html' )
def photos(GAL_NAME = None):

    print GAL_NAME
    
    if not GAL_NAME:
        post = '/thumbs/1.jpg'
        print GALLERIES
        return render_template( "photos.html", galleries = GALLERIES, pre = GALLERY_LOCATION + '/', post = post )
    
    else:
        if GAL_NAME not in GALLERIES.values():
            return redirect( url_for('photos') )

        location = GALLERY_LOCATION + '/' + GAL_NAME + '/full/'
        pics = os.listdir( location )
        i = 0
        while i < len(pics):
            pics[i] = '/' + location + pics[i]
            i+= 1            
        return render_template( 'gallery.html', pics = pics )

""""    
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
    
