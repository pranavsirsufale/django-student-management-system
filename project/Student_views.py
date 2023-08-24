from django. shortcuts import render,redirect
from app.models import Student_Notification,Student,Student_feedback,Student_leave,Student_result
from django.contrib import messages



def STUEDENT_HOME(request):
    return render(request,'Student/home.html')


def STUDENT_NOTIFICATION(request):
    student = Student.objects.filter(admin = request.user.id)
    for i in student:
        student_id = i.id
        notification = Student_Notification.objects.filter( student_id = student_id)

        context = {
            'notification':notification,
        }



    return render(request,'Student/notification.html',context)


def STUDENT_NOTIFICATION_MARK_AS_DONE(request,status):
    notification = Student_Notification.objects.get( id = status)
    notification.status = 1
    notification.save()

    return redirect('student_notification')


def STUDENT_FEEDBACK(request):
    student_id = Student.objects.get(admin = request.user.id)
    feedback_history = Student_feedback.objects.filter(student_id = student_id)
    context = {
        'feedback_history':feedback_history,
    }
    return render(request,'Student/feedback.html',context)


def STUDENT_FEEDBACK_SAVE(request):
    if request.method == 'POST':
        feedback = request.POST.get('feedback')
        student_id = Student.objects.get(admin=request.user.id)

        feedbacks = Student_feedback(
            student_id = student_id,
            feedback = feedback,
            feedback_reply = '',
        )
        feedbacks.save()
        messages.success(request,'Feedback  Successfully ! ')

    return redirect('student_feedback')


def STUDENT_LEAVE(request):
    student = Student.objects.filter(admin = request.user.id)
    for i in student:
        student_id = i.id
        student_leave_history = Student_leave.objects.filter(student_id = student_id)

        context = {
            'student_leave_history':student_leave_history,
        }
    return render(request,'Student/student_leave.html',context)


def STUDENT_LEAVE_SAVE(request):
    if request.method == 'POST':
        leave_date = request.POST.get('leave_date')
        leave_message = request.POST.get('leave_message')
        student_id = Student.objects.get( admin = request.user.id)

        student_leave = Student_leave(
            student_id = student_id,
            data = leave_date,
            message = leave_message,
        )
        student_leave.save()
        # data saved in database in Student_leave table
        messages.success(request,' Leave Application Successfully Send ! ')

    return redirect('student_leave')


def VIEW_RESULT(request):
    student = Student.objects.get( admin = request.user.id )
    result = Student_result.objects.filter(student_id = student)
    mark = None

    for i in result:
        assignment_mark = i.assignment_mark
        exam_mark = i.exam_mark
        mark = assignment_mark + exam_mark



    context = {
        'result':result,
        'mark':mark,
    }

    return render(request,'Student/view_result.html',context)