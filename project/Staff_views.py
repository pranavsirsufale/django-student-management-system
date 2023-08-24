from django. shortcuts import render,redirect
from app.models import Staff,Staff_Notification,Staff_leave,Staff_feeback,Subject,Session_Year
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from app.models import Student,Attendance,Attendance_report,Student_result


@login_required(login_url="/")
def HOME(request):
    return render(request,'Staff/home.html')

@login_required(login_url="/")
def NOTIFICATIONS(request):
    staff = Staff.objects.filter( admin = request.user.id)
    for i in staff:
       staff_id = i.id
       notification = Staff_Notification.objects.filter( staff_id = staff_id)

       context =  {
           'notification':notification,
       }
       return render(request,'Staff/notification.html',context)

@login_required(login_url="/")
def STAFF_NOTIFICATION_MARK_AS_DONE(request,statuss):
    notification = Staff_Notification.objects.get( id = statuss )
    notification.statuss = 1
    notification.save()
    return redirect('notifications')


@login_required(login_url="/")
def STAFF_APPLY_LEAVE(request):
    staff = Staff.objects.filter( admin = request.user.id)
    for i in staff:
        staff_id = i.id

        staff_leave_history = Staff_leave.objects.filter(staff_id = staff_id)

        context = {
            'staff_leave_history':staff_leave_history,
        }


    return render(request,'Staff/apply_leave.html', context)




@login_required(login_url="/")
def STAFF_LEAVE_SAVE(request):
    if request.method == 'POST':
        leave_date = request.POST.get('leave_date')
        leave_message = request.POST.get('leave_message')
        staff = Staff.objects.get(admin = request.user.id)

        leave = Staff_leave (
            staff_id = staff,
            data = leave_date,
            message = leave_message,

        )
        leave.save()
        messages.success(request,' Leave Send To Admin Successfully ! ')

        return redirect('staff_apply_leave')


def STAFF_FEEDBACK(request):
    staff_id = Staff.objects.get( admin = request.user.id)

    feedback_history = Staff_feeback.objects.filter( staff_id = staff_id)

    context = {
        'feedback_history':feedback_history,

    }

    return render(request,'Staff/feedback.html',context)


def STAFF_FEEBACK_SAVE(request):
    if request.method == 'POST':
        feedback = request.POST.get('feedback')
        staff = Staff.objects.get(admin = request.user.id)

        feedback = Staff_feeback (
            staff_id = staff,
            feedback = feedback,
            feedback_reply = '',

        )
        feedback.save()
        messages.success(request,' Feedback Send Successfully ! ')



        return redirect('staff_feedback')


def STAFF_TAKE_ATTENDANCE(request):
    staff_id = Staff.objects.get(admin = request.user.id)

    subject = Subject.objects.filter(staff= staff_id)
    session_year = Session_Year.objects.all()
    students = None
    action = request.GET.get('action')
    get_subject = None
    get_session_year = None


    if action is not None:
        if request.method == 'POST':
            subject_id = request.POST.get('subject_id')
            session_year_id = request.POST.get('session_year_id')
            get_subject = Subject.objects.get(id = subject_id)
            get_session_year = Session_Year.objects.get( id= session_year_id)
            subject = Subject.objects.filter(id = subject_id)
            for i in subject:
                student_id = i.course.id
                students = Student.objects.filter( course_id = student_id)



    context = {
        'subject':subject,
        'session_year':session_year,
        'get_subject':get_subject,
        'get_session_year':get_session_year,
        'action':action,
        'students':students,
    }
    return render(request,'Staff/take_attendance.html',context)


def STAFF_SAVE_ATTENDANCE(request):
    if request.method == 'POST':
        subject_id = request.POST.get('subject_id')
        session_year_id = request.POST.get('session_year_id')
        attendance_date = request.POST.get('attendance_date')
        student_id = request.POST.getlist('student_id')

        get_subject = Subject.objects.get(id = subject_id)
        get_session_year = Session_Year.objects.get(id = session_year_id)
        attendance = Attendance(
            subject_id = get_subject,
            addendance_date = attendance_date,
            session_year_id = get_session_year,
        )
        attendance.save()
        for i in student_id:
            stud_id = i
            int_stud = int(stud_id)

            p_student = Student.objects.get(id = int_stud)
            attendance_report = Attendance_report(
                stud_id = p_student,
                attendance_id = attendance,
            )
            attendance_report.save()
    return redirect('staff_take_attendance')


def STAFF_VIEW_ATTENDANCE(request):
    staff_id = Staff.objects.get( admin = request.user.id)
    subject = Subject.objects.filter(staff_id = staff_id)
    session_year = Session_Year.objects.all()

    action = request.GET.get('action')
    context = {
        'subject':subject,
        'session_year':session_year,
        'action':action,
    }
    return render(request,'Staff/view_attendance.html',context)


def STAFF_ADD_RESULT(request):
    staff = Staff.objects.get(admin = request.user.id)
    subjects = Subject.objects.filter(staff_id = staff)
    session_year = Session_Year.objects.all()
    action = request.GET.get('action')

    get_subject = None
    get_session = None
    students = None
    if action is not None:
        if request.method == 'POST':
            subject_id = request.POST.get('subject_id')
            session_year_id = request.POST.get('session_year_id')

            get_subject = Subject.objects.get( id = subject_id)
            get_session = Session_Year.objects.get( id = session_year_id)

            subject = Subject.objects.filter(id = subject_id)
            for i in subject:
                student_id = i.course.id
                students = Student.objects.filter( course_id = student_id)


    context = {
        'subjects':subjects,
        'session_year':session_year,
        'action':action,
        'get_subject':get_subject,
        'get_session':get_session,
        'students':students,
    }
    return render(request,'Staff/add_result.html',context)


def STAFF_SAVE_RESULT(request):
    if request.method == 'POST':
        subject_id = request.POST.get('subject_id')
        session_year_id = request.POST.get('session_year_id')
        student_id = request.POST.get('student_id')
        assignment_mark = request.POST.get('assignment_mark')
        exam_mark = request.POST.get('exam_mark')

        get_student = Student.objects.get(admin = student_id)
        get_subject = Subject.objects.get(id = subject_id)
        check_exists = Student_result.objects.filter( subject_id = get_subject,student_id = get_student).exists()

        if check_exists:
            result = Student_result.objects.get( subject_id = get_subject, student_id = get_student)
            result.assignment_mark = assignment_mark
            result.exam_mark = exam_mark
            result.save()
            messages.success(request,' Result Updated Successfully !')
            return redirect('staff_add_result')
        else:
            result = Student_result(
                student_id = get_student,
                subject_id = get_subject,
                exam_mark = exam_mark,
                assignment_mark = assignment_mark,
            )
            result.save()
            messages.success(request,' Result Added Successfully ! ')
            return redirect('staff_add_result')

    return None
