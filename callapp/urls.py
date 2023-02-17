from django.urls import path
from callapp import views as callapp_views
app_name = "callapp"
urlpatterns = [

    path('',callapp_views.home_page , name='home_page'),
    path('intiate-call/',callapp_views.intiate_call , name='intiate_call'),
    path('call-report/',callapp_views.call_report , name='call_report'),
    path('delete/<int:id>/<str:number>',callapp_views.delete_call , name='delete_call'),
   
    
]