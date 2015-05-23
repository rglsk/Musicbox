$(document).ready(function(){
    namespace = '/test';
    var socket = io.connect('http://' + document.domain + ':' + location.port + namespace);
    socket.on('connect', function() {
        socket.emit('my event', {data: 'I\'m connected!'});
    });

    socket.on('my response', function(msg) {
        alert("Added new song to playlist: " + msg.data.split("\\")[2]);
    });

    socket.on('current song response', function(msg) {
        $('#current_song').html('<center><h1>' + msg.current_song + '</h1></center>');
        var list = "";
        for(i=0; i<msg.song_list.length; i++){
            var diss = "";
            if (msg.song_list[i] == msg.current_song.substring(0, 26)){
                diss = "disabled"
            };
            list +="<a href='#' class='list-group-item " + diss + "'><i class='glyphicon glyphicon-music'></i>  " + i+ ": " + msg.song_list[i]+"</li></a>";
            diss = "";
        }
        $(".list-group").html(list);
    });

    $('form#upload_data').submit(function(event) {
        socket.emit('my broadcast event', {data: $('#upload_name').val()});
        document.getElementById("upload_data").submit();
        return false;
    });

});