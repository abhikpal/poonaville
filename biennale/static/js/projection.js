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
    namespace = '/projection';

    // Connect to the Socket.IO server.
    socket = io.connect('http://' + document.domain + ':' + location.port + namespace);


    socket.on('update', function(msg) {
        // things to do when a user moves.
        console.log(msg);
    });

    socket.on('user_joined', function(msg) {
        // code to run when a new player joins the game
        // msg is of the form:
        // {
        //      'email'         : <the user who joined the game>,
        //      'start_coord_x' : <user's stored x-coordinate from last sesison>,
        //      'start_coord_y' : <user's stored y-coordinate from last session>,
        //      'meter_life'    : <user's life meter status (in percent)>,
        //      'meter_status'  : <user's status meter status (in percent)>,
        //      'meter_karma'   : <user's karma meter status (in percent)>
        // }
        console.log(msg);
    });

    socket.on('user_left', function(msg) {
        // code to run when a player exits the game.
        // msg is of the form:
        // {
        //     'email'         : <email of the user who left the game>
        // }
        console.log(msg);
    });

    socket.on('movement', function(msg){
        // Code to run when a player moves
        // msg is of the form
        // {
        //     'email'     : <email of the user who moved>,
        //     'x'         : <movement in the x-direction>,
        //     'y'         : <movement in the y-direction>
        // }
        console.log(msg);
    });
});

// Call this when the allocated time for the player is over or the player
// "dies" naturally.
// 
// email: the email address of the player who needs to be eliminated
// location_x: x-coordinate of the user before elimination
// location_y: y-coordinate of the user before elimination
function eliminate_player(email, location_x, location_y) {
    socket.emit('remove_user', {
        'email': email,
        'locx': location_x,
        'locy': location_y
    });
    return false;
}

// Call this to update the meter the player.
// 
// email:   the email address for the player whose meter needs update
// karma:   new value for karma meter (from 0 to 100)
// life:    new value for life meter (from 0 to 100)
// status:  new value for the status meter (from 0 to 100)
function update_meter(email, karma, life, status) {
    socket.emit('update_meter', {
        'email': email,
        'karma': karma,
        'life': life,
        'status': status
    });
    return false;
}

