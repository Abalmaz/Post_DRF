var postSocket = new WebSocket(
    'ws://' + window.location.host + '/ws/');

    postSocket.onmessage = function(e) {
        var data = JSON.parse(e.data);
        var message = data['message'];
        $.getJSON('http://127.0.0.1:8000/api/post/' + message,
        function(data){
            var post = '<td>' + data.title + '</td>' +
                       '<td>' + data.category + '</td>' +
                       '<td>' + data.user + '</td>' +
                       '<td>' + data.status + '</td>' +
                       '<td>' + data.created_on + '</td>'
            $('#posts').prepend(post);

        });

    };

    postSocket.onclose = function(e) {
        console.error('Post socket closed unexpectedly');
    };