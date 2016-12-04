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
