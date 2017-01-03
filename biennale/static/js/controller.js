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

    socket.on('connect', function () {
        console.log('Client has connected to the server!');
        document.getElementById("socketconn").style.color = "green";
    });
    
    socket.on('update_meter', function(msg) {
        // What to do when the meter is updates
        // This should change progress bars on the controller, etc.
        // msg is of the form 
        //  {
        //      'karma': <KARMA METER VALUE>,
        //      'life': <LIFE METER VALUE>,
        //      'status': <STATUS METER VALUE>
        //  }
        // 
        console.log(msg);
        return false;
    });

    socket.on('remove_user', function(msg) {
        // What to do when the user is eliminated from the game
        // msg is of the form:
        // {
        //      'email': <email of the user>
        // }
        console.log(msg);
        return false;
    });

});

function send_command(xdir, ydir) {
    socket.emit('movement', {
        x:xdir,
        y:ydir
    });
    return false;
}

function up() { send_command('0', '1'); }
function down() { send_command('0', '-1') }
function left() { send_command('-1', '0') }
function right() { send_command('1', '0') }
