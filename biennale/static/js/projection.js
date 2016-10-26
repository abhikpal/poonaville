$(document).ready(function() {
    namespace = '/projection';

    // Connect to the Socket.IO server.
    var socket = io.connect('http://' + document.domain + ':' + location.port + namespace);

    socket.on('movement', function(msg) {
        $('#projection').append('<br>' + $('<div/>').text(msg.data).html());
    });
});   
