$(document).ready(function () {
    $('#gobackcollege').on("click", function() {
        window.location.href = "/college"
    });

    $("#addCollegeForm").on("submit", function (event) {
        $.ajax({
            data: {
                code: $("#college_code").val(),
                name: $("#college_name").val(),
            },
            type: "POST",
            url: "/college/add",
        }).done(function (data) {
            if (data.error) {
                $("#errorcollegeaddmsg").text(data.error).show();
            }
            else {
                alert("Successfully added college")
                window.location.href = "/college"
            }
        });x
        event.preventDefault();
    });


    $(".delete-College").click(function ( ) {
        var collegeCode = $(this).data("college-code")

        $("#deleteCollegeForm").click(function () {
            $.ajax({
                type : "POST",
                url: "college/delete",
                data: {
                    code : collegeCode
                }
            }).done( function (data) {
                if (data.error) {
                    $("#errorcoldeletemsg").text(data.error).show();
                }
                else {
                    alert("Succesfully deleted coursE:" + collegeCode)
                    window.location.href = "/college"
                }
            });
        });
    });


});