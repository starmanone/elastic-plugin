from django.urls import path

from . import views

app_name = 'api'
urlpatterns = [
    path('elastic', views.ElasticData.as_view()),
    path('mail/actions/', views.MailActionsList.as_view()),
    path('mail/<int:pk>/actions/', views.MailActionsView.as_view()),
    path('mail/<int:pk>/metadata/', views.MailMetadataView.as_view()),
]