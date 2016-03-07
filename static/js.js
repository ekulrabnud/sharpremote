$(document).ready(function() {


    console.log('ready')


    $("#on").click(function() {

        console.log("on clicked")
        $.get("/remote/on", function(data) {
            console.log(data);
        });
    });

        $("#off").click(function() {

        console.log("off clicked")
        $.get("/remote/off", function(data) {
            console.log(data);
        });
    });



});