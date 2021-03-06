function findPos(obj) {
    var curleft = 0, curtop = 0;
    if (obj.offsetParent) {
        do {
            curleft += obj.offsetLeft;
            curtop += obj.offsetTop;
        } while (obj = obj.offsetParent);
        return { x: curleft, y: curtop };
    }
    return undefined;
}

function rgbToHex(r, g, b) {
    if (r > 255 || g > 255 || b > 255)
        throw "Invalid color component";
    return ((r << 16) | (g << 8) | b).toString(16);
}



// set up some squares
// var example = document.getElementById('myCanvas');
// var context = example.getContext('2d');
// context.fillStyle = "rgb(255,0,0)";
// context.fillRect(0, 0, 50, 50);
// context.fillStyle = "rgb(0,0,255)";
// context.fillRect(55, 0, 50, 50);

// $('#example').mousemove(function(e) {
//     var pos = findPos(this);
//     var x = e.pageX - pos.x;
//     var y = e.pageY - pos.y;
//     var coord = "x=" + x + ", y=" + y;
//     var c = this.getContext('2d');
//     var p = c.getImageData(x, y, 1, 1).data; 
//     var hex = "#" + ("000000" + rgbToHex(p[0], p[1], p[2])).slice(-6);
//     $('#status').html(coord + "<br>" + hex);
// });


