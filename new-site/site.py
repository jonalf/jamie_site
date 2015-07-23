from flask import Flask, request, render_template

site = Flask( __name__ )

@site.route( '/' )
def root():
    return render_template( 'main.html' )

@site.route( '/bio' )
def bio():
    return render_template( 'main.html' )

@site.route( '/resume' )
def resume():
    return render_template( 'main.html' )

@site.route( '/audio' )
def audio():
    return render_template( 'main.html' )

@site.route( '/video' )
def video():
    return render_template( 'main.html' )

@site.route( '/photos' )
def photos():
    return render_template( 'main.html' )

@site.route( '/contact' )
def contact():
    return render_template( 'main.html' )

if __name__ == '__main__':
    site.debug = True
    site.run()
    
