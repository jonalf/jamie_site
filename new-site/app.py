from flask import Flask, request, render_template, url_for, redirect
import os

site = Flask( __name__ )

GALLERY_LOCATION = 'static/img/galleries'
GALLERIES = [ ('Cabaret','cabaret'), ('The Marvelous Wonderettes','marvelous'), ('Carousel','carousel'), ('A Funny Thing Happened on the Way to the Forum','forum'), ('Disney Dreams','disney'), ('Eleemosynary','eleemosynary') ]

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

    if not GAL_NAME:
        post = '/square/1.jpg'
        return render_template( "photos.html", galleries = GALLERIES, pre = GALLERY_LOCATION + '/', post = post )
    
    else:
        if not any( GAL_NAME in item for item in GALLERIES ):
            return redirect( url_for('photos') )

        local = GALLERY_LOCATION + '/' + GAL_NAME + '/square/'
        location = 'img/galleries/' + GAL_NAME + '/square/'
        pics = os.listdir( local )
        i = 0
        while i < len(pics):
            pics[i] = location + pics[i]
            i+= 1            
        return render_template( 'gallery.html', pics = pics )

@site.route( '/contact.html' )
def contact():
    return render_template( 'main.html' )

if __name__ == '__main__':
    site.debug = True
    site.run()
    
