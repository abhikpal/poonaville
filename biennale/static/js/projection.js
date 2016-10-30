cx = 400;
cy = 400;

$(document).ready(function() {
    namespace = '/projection';

    // Connect to the Socket.IO server.
    var socket = io.connect('http://' + document.domain + ':' + location.port + namespace);

    socket.on('movement', function(msg) {
        cx = cx + 50*Number(msg.x);
        if (cx > 800) { cx = 800; }
        if (cx < 0) { cx = 0; }

        if (cy > 800) { cy = 800; }
        if (cy < 0) { cy = 0; }

        cy = cy - 50*Number(msg.y);
        console.log(msg.client);
    });
});
