$(document).ready(function () {
  $("#addStudentForm").on("submit", function (event) {
    $.ajax({
      type: "POST",
      url: "/student/add",
      data: {
        id: $("#student_id").val(),
        firstname: $("#student_first_name").val(),
        lastname: $("#student_last_name").val(),
        course_code: $("#student_course_code").val(),
        year: $("#student_year").val(),
        gender: $("#student_gender").val(),
      },
    }).done(function (data) {
      if (data.error) {
        $("#erroraddstdmsg").text(data.error).show();
      } else {
        alert("Successfully added student");
        window.location.href = "/student";
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
        data: { csasdsda: studentId },
      }).done(function (data) {
        if (data.error) {
          $("#errordeletstdemsg").text(data.error).show();
        } else {
          alert("Sucessfully deleted student: " + studentId);
          window.location.href = "/student";
        }
      });
    });
  });

  $(".edit-Student").on("click", function () {
    var id = $(this).data("student-id");
    var firstname = $(this).data("student-firstname");
    var lastname = $(this).data("student-lastname");
    var course_code = $(this).data("student-course");
    var year = $(this).data("student-year");
    var gender = $(this).data("student-gender");

    $("#edit_student_id").val(id);
    $("#edit_student_first_name").val(firstname);
    $("#edit_student_last_name").val(lastname);
    $("#edit_student_course_code").val(course_code);
    $("#edit_student_year").val(year);
    $("#edit_student_gender").val(gender);

    $('#editStudentForm').on("submit", function (event) {
        $.ajax({
            type : "POST",
            url : "/student/edit",
            data: {
                pastid : id,
                id: $("#edit_student_id").val(),
                firstname: $("#edit_student_first_name").val(),
                lastname: $("#edit_student_last_name").val(),
                course_code: $("#edit_student_course_code").val(),
                year: $("#edit_student_year").val(),
                gender: $("#edit_student_gender").val()

            }

        }).done(function (data) {
            if (data.error) {
                $("#erroreditstdmsg").text(data.error).show();
            }
            else {
                alert("Successfully edited student")
                window.location.href = "/student"
            }
        });
        event.preventDefault()
    });
  });
});
