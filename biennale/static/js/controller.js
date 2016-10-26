$(document).ready(function() {
    namespace = '/controller';

    // Connect to the Socket.IO server.
    var socket = io.connect('http://' + document.domain + ':' + location.port + namespace);

    $('.controller#up').click(function() {
        socket.emit('update', {x: '0',  y:'1', cmd:'up'});
        return false;
    });
    $('.controller#down').click(function() {
        socket.emit('update', {x: '0',  y:'-1', cmd:'down'});
        return false;
    });
    $('.controller#left').click(function() {
        socket.emit('update', {x: '-1',  y:'0', cmd:'left'});
        return false;
    });
    $('.controller#right').click(function() {
        socket.emit('update', {x: '1',  y:'0', cmd:'right'});
        return false;
    });
});
