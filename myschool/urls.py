from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^teachers/$', views.ShowTeacherList.as_view(), name='teachers_list'),
    url(r'^teachers/$', views.ShowTeacherList.as_view(), name='teachers_list'),
    url(r'^students/$', views.ShowStudentsList.as_view(), name='students_list'),
    url(r'^subjects/$', views.ShowSubjectsList.as_view(), name='subjects_list'),
]