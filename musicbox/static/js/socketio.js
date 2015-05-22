$(document).ready(function(){
    namespace = '/test';
    var socket = io.connect('http://' + document.domain + ':' + location.port + namespace);
    socket.on('connect', function() {
        socket.emit('my event', {data: 'I\'m connected!'});
    });

    socket.on('my response', function(msg) {
        alert("Added new song to playlist: " + msg.data.split("\\")[2]);
        // $('#log').append('<br>Received #' + msg.count + ': ' + msg.data);
    });

    socket.on('current song response', function(msg) {
        $('#current_song').html('<h1>Current played song: ' + msg.current_song + '</h1>');
    });

    // $(document).ready(function() {
    //     socket.emit('broadcast current song', {});
    //     return false;
    // });

    $('form#upload_data').submit(function(event) {
        socket.emit('my broadcast event', {data: $('#upload_name').val()});
        document.getElementById("upload_data").submit();
        return false;
    });

});