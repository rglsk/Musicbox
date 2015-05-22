$(document).ready(function(){
    namespace = '/test';
    var socket = io.connect('http://' + document.domain + ':' + location.port + namespace);
    socket.on('connect', function() {
        socket.emit('my event', {data: 'I\'m connected!'});
    });

    socket.on('my response', function(msg) {
        $('#log').append('<br>Received #' + msg.count + ': ' + msg.data);
    });

    $('form#upload_data').submit(function(event) {
        socket.emit('my broadcast event', {data: $('#upload_name').val()});
        document.getElementById("upload_data").submit();
        return false;
    });
});