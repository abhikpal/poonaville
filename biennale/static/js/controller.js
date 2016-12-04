/*
 * Poonaville
 * (for the Pune Biennale 2017)
 * Copyright (C) 2016  Abhik Pal
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */


$(document).ready(function() {
    namespace = '/controller';

    // Connect to the Socket.IO server.
    socket = io.connect('http://' + document.domain + ':' + location.port + namespace);

    $('.controller#up').on("tap",      function() { sendCommand('up', '0', '1'); });
    $('.controller#up').on("click",    function() { sendCommand('up', '0', '1'); });

    $('.controller#down').on("tap",    function() { sendCommand('down', '0', '-1') });
    $('.controller#down').on("click",  function() { sendCommand('down', '0', '-1') });

    $('.controller#left').on("tap",    function() { sendCommand('left', '-1', '0') });
    $('.controller#left').on("click",  function() { sendCommand('left', '-1', '0') });

    $('.controller#right').on("tap",   function() { sendCommand('right', '1', '0') });
    $('.controller#right').on("click", function() { sendCommand('right', '1', '0') });

});

function sendCommand(command, xdir, ydir) {
    socket.emit('update', {x:xdir, y:ydir, cmd:command});
    return false;
}
