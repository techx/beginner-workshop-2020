$(document).ready(function() {
    $("#post-button").click(function() {
        const url = "http://localhost:5000/post";
        const postInfo = {
            title: $("#title").val(),
            description: $("#description").val()
        };

        $.ajax({
            url: url,
            type: "POST",
            data: JSON.stringify(postInfo),
            processData: false,
            contentType: "application/json; charset=UTF-8",
            complete: function() {
                console.log("request complete!");
                window.location.reload();
            }
        });

    });
});