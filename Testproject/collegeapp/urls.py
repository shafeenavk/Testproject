
from django.urls import path
from . import views
app_name='collegeapp'

urlpatterns = [
    path("",views.index,name="index"),
    path("login/",views.login,name='login'),
    path("register/",views.register,name='register'),
    path("new/",views.new,name='new'),
    path("submit/",views.submit,name='submit')

]