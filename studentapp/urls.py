from django.urls import path

from . import views


urlpatterns=[
    path('studentapp/',views.index,name='index'),
    path('studentdetails/',views.studentdetails,name='studentdetails'),
    # path('formhandling/',views.formhandling,name='form'),
    path('adduser/',views.adduser,name='adduser'),
    path('delete/',views.delete,name='delete')
]