$(document).ready(function () {
    $("#addCourseForm").on("submit", function (event) {
        $.ajax({
            data: {
                code: $("#code").val(),
                name: $("#name").val(),
                college_code: $("#college_code").val()
            },
            type: "POST",
            url: "/course/add",
        }).done(function (data) {
            if (data.error) {
                $("#erroraddmsg").text(data.error).show();
            }
            else {
                alert("Successfully added course")
                window.location.href = "/course"
            }
        });
        event.preventDefault();
    });
    
    $(".delete-Course").click(function () {
        var courseCode = $(this).data("course-code");
    

        $("#deleteCourseForm").click(function () {
            $.ajax({
                type: "POST",
                url: "/course/delete",
                data: { csasdsda: courseCode },
            }).done(function (data) {
                if (data.error) {
                    $("#errordeletemsg").text(data.error).show();
                }
                else {
                    alert("Sucessfully deleted course: " + courseCode)
                    window.location.href = "/course"
    
                }
            });    
        });


      });



   

    $('#gobackcourse').on("click", function() {
        window.location.href = "/course"


    });


});
