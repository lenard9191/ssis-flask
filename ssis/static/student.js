$(document).ready(function () {

    $("#addStudentForm").on("submit", function (event) {  
        $.ajax({
            type : "POST",
            url : "/student/add",
            data : {
                id : $("#student_id").val(),
                firstname: $("#student_first_name").val(),
                lastname: $("#student_last_name").val(),
                course_code: $("#student_course_code").val(),
                year: $("#student_year").val(),
                gender : $("#student_gender").val(),
            }
        }).done (function (data) {
            if (data.error) {
                $("#erroraddstdmsg").text(data.error).show()
            }
            else {
                alert("Successfully added student")
                window.location.href = "/student"
            }
        });
        event.preventDefault();
    });

    $(".delete-Student").click(function () {
        var studentId = $(this).data("student-id");
    

        $("#deleteStudentForm").click(function () {
            $.ajax({
                type: "POST",
                url: "/student/delete",
                data: { csasdsda: studentId }
            }).done(function (data) {
                if (data.error) {
                    $("#errordeletstdemsg").text(data.error).show();
                }
                else {
                    alert("Sucessfully deleted student: " + studentId)
                    window.location.href = "/student"
    
                }
            });    
        });


      });



});