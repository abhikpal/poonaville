$(document).ready(function() {
    namespace = '/controller';

    // Connect to the Socket.IO server.
    socket = io.connect('http://' + document.domain + ':' + location.port + namespace);

    $('.controller#up').on("tap", function() { sendCommand('up', '0', '1'); });
    $('.controller#up').on("click", function() { sendCommand('up', '0', '1'); });

    $('.controller#down').on("tap", function() { sendCommand('down', '0', '-1') });
    $('.controller#down').on("click", function() { sendCommand('down', '0', '-1') });

    $('.controller#left').on("tap", function() { sendCommand('left', '-1', '0') });
    $('.controller#left').on("click", function() { sendCommand('left', '-1', '0') });

    $('.controller#right').on("tap", function() { sendCommand('right', '1', '0') });
    $('.controller#right').on("click", function() { sendCommand('right', '1', '0') });

});

function sendCommand(command, xdir, ydir) {
    socket.emit('update', {x:xdir, y:ydir, cmd:command});
    return false;
}
