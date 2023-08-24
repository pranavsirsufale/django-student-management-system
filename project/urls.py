"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from . import views,Hod_views,Staff_views,Student_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('base/',BASE,name='base'),
    # login path
    path('',LOGIN,name='login'),
    path('doLogin/',doLogin,name='doLogin'),
    path('doLogout',LogOut,name='logout'),

    # profile update
    path('profile',PROFILE,name='profile'),
    path('profile/update',PROFILE_UPDATE,name='profile_update'),

    # this is Hod panel url student related
    path('hod/home',Hod_views.HOME, name='hod_home'),
    path('hod/student/add',Hod_views.ADD_STUDENT,name='add_student'),
    path('hod/student/view',Hod_views.VIEW_STUDENT,name='view_student'),
    path('hod/student/edit/<str:id>',Hod_views.EDIT_STUDENT,name='edit_student'),
    path('hod/student/update',Hod_views.UPDATE_STUDENT,name='update_student'),
    path('hod/student/delete/<str:admin>',Hod_views.DELETE_STUDENT,name='delete_student'),

    # this is course url
    path('hod/course/add',Hod_views.ADD_COURSE,name='add_course'),
    path('hod/course/view',Hod_views.VIEW_COURSE,name='view_course'),
    path('hod/course/edit/<str:id>',Hod_views.EDIT_COURSE,name='edit_course'),
    path('hod/course/update',Hod_views.UPDATE_COURSE,name='update_course'),
    path('hod/course/delete/<str:id>',Hod_views.DELETE_COURSE,name='delete_course'),

    # staff related urls
    path('hod/staff/add',Hod_views.ADD_STAFF,name='add_staff'),
    path('hod/staff/view',Hod_views.VIEW_STAFF,name='view_staff'),
    path('hod/staff/edit/<str:id>',Hod_views.EDIT_STAFF,name='edit_staff'),
    path('hod/staff/update',Hod_views.UPDATE_STAFF,name='update_staff'),
    path('hod/staff/delete/<str:admin>',Hod_views.DELETE_STAFF,name='delete_staff'),

    # subject related urls
    path('hod/subject/add',Hod_views.ADD_SUBJECT,name='add_subject'),
    path('hod/subject/view',Hod_views.VIEW_SUBJECT,name='view_subject'),
    path('hod/subject/edit/<str:id>',Hod_views.EDIT_SUBJECT,name='edit_subject'),
    path('hod/subject/update',Hod_views.UPDATE_SUBJECT,name='update_subject'),
    path('hod/subject/delete/<str:id>',Hod_views.DELETE_SUBJECT,name='delete_subject'),


    # session related urls
    path('hod/session/add',Hod_views.ADD_SESSION,name='add_session'),
    path('hod/session/view',Hod_views.VIEW_SESSION,name='view_session'),
    path('hod/session/edit/<str:id>',Hod_views.EDIT_SESSION,name='edit_session'),
    path('hod/session/update',Hod_views.UPDATE_SESSION,name='update_session'),
    path('hod/session/delete/<str:id>',Hod_views.DELETE_SASSION,name='delete_session'),

    path('hod/staff/send_notification',Hod_views.STAFF_SEND_NOTIFICATION,name='staff_send_notification'),
    path('hod/staff/save_notification',Hod_views.SAVE_STAFF_NOTIFICATION,name='save_staff_notification'),

    path('hod/student/send_notification',Hod_views.STUDENT_SEND_NOTIFICATION,name='student_send_notification'),
    path('hod/student/save_notification',Hod_views.SAVE_STUDENT_NOTITFICATION,name='save_student_notification'),

    path('hod/student/feedback',Hod_views.HOD_STUDENT_FEEDBACK,name='hod_student_feedback'),
    path('hod/student/feedback/reply',Hod_views.HOD_STUDENT_FEEDBACK_REPLY,name='hod_student_feedback_reply'),

    path('hod/staff/leave_view',Hod_views.STAFF_LEAVE_VIEW,name='staff_leave_view'),
    path('hod/staff/approve_leave/<str:id>',Hod_views.STAFF_APPROVE_LEAVE,name='staff_approve_leave'),
    path('hod/staff/reject_leave/<str:id>', Hod_views.STAFF_REJECT_LEAVE, name='staff_reject_leave'),

    path('hod/student/leave_view',Hod_views.STUDENT_LEAVE_VIEW,name='hod_student_leave_view'),
    path('hod/student/approve_leave/<str:id>',Hod_views.STUDENT_APPROVE_LEAVE,name='student_approve_leave'),
    path('hod/student/reject_leave/<str:id>',Hod_views.STUDENT_REJECT_LEAVE,name='student_reject_leave'),



    path('hod/staff/feedback',Hod_views.HOD_STAFF_FEEDBACK_REPLY,name='hod_staff_feedback_reply'),
    path('hod/staff/feedback/save', Hod_views.HOD_STAFF_FEEDBACK_REPLY_SAVE, name='hod_staff_feedback_reply_save'),





                  # Staff related urls
    path('staff/home',Staff_views.HOME,name='staff_home'),


    path('staff/notifications',Staff_views.NOTIFICATIONS,name='notifications'),
    path('staff/mark_as_done/<str:statuss>',Staff_views.STAFF_NOTIFICATION_MARK_AS_DONE,name='staff_notification_mark_as_done'),


    path('staff/apply_leave',Staff_views.STAFF_APPLY_LEAVE,name='staff_apply_leave'),
    path('staff/apply_leave_save',Staff_views.STAFF_LEAVE_SAVE,name='staff_apply_leave_save'),

    path('staff/feedback',Staff_views.STAFF_FEEDBACK,name='staff_feedback'),
    path('staff/feedback/save',Staff_views.STAFF_FEEBACK_SAVE,name='staff_feedback_save'),

    path('staff/take_attendance',Staff_views.STAFF_TAKE_ATTENDANCE,name='staff_take_attendance'),
    path('staff/save_attendance',Staff_views.STAFF_SAVE_ATTENDANCE,name='staff_save_attendance'),
    path('staff/view_attendance',Staff_views.STAFF_VIEW_ATTENDANCE,name='staff_view_attendance'),


    path('staff/add/result',Staff_views.STAFF_ADD_RESULT,name='staff_add_result'),
    path('staff/save/result',Staff_views.STAFF_SAVE_RESULT,name='staff_save_result'),




    # student related urls
    path('student/home',Student_views.STUEDENT_HOME,name='student_home'),

    path('student/notification',Student_views.STUDENT_NOTIFICATION,name='student_notification'),
    path('student/mark_as_done/<str:status>',Student_views.STUDENT_NOTIFICATION_MARK_AS_DONE,name='student_notification_mark_as_done'),

    path('student/feedback',Student_views.STUDENT_FEEDBACK,name='student_feedback'),
    path('student/feedback/save',Student_views.STUDENT_FEEDBACK_SAVE,name='student_feedback_save'),

    path('student/apply_for_leave',Student_views.STUDENT_LEAVE,name='student_leave'),
    path('student/leave_save',Student_views.STUDENT_LEAVE_SAVE,name='student_leave_save'),


    path('student/view_result',Student_views.VIEW_RESULT,name='view_result'),

    path('index/',index, name='index'),
    path('analyze',analyze , name='analyze'),

    path('qrdir',qrredire,name='qrdir'),
    path('qrmaker',qrmaker, name='qrmaker'),
    path('showqr', showqr, name='showqr'),

]+static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)
