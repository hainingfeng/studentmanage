"""StudentManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app01 import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^classes_list/',views.classes_list),
    url(r'^add_class/',views.add_class),
    url(r'^del_class/',views.del_class),
    url(r'^edit_class/',views.edit_class),

    url(r'^students_list/',views.students_list),
    url(r'^add_student/',views.add_student),
    url(r'^del_student/',views.del_student),
    url(r'^edit_student/',views.edit_student),

    url(r'^teachers_list/',views.teachers_list),
    url(r'^add_teacher/',views.add_teacher),
    url(r'^del_teacher/',views.del_teacher),
    url(r'^edit_teacher/',views.edit_teacher),

    url(r'^courses_list/',views.courses_list),
    url(r'^add_course/',views.add_course),
    url(r'^del_course/',views.del_course),
    url(r'^edit_course/',views.edit_course),



]
