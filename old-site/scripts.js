function changeView( picName, galName ) {
    var frame = document.getElementById('frame');
    var s = "<img src=\"images/gal" + galName + "/" + picName + ".png\" height=\"400\" />";
    frame.innerHTML = s;
    //frame.innerHTML=Date();
    return false;
}
