from django.urls import path
from . import views

urlpatterns = [
    path("", views.social_security_list, name="social_security_list"),
    path("create/", views.social_security_create, name="social_security_create"),
    path("update/<int:pk>/", views.social_security_update, name="social_security_update"),
    path("delete/<int:pk>/", views.social_security_delete, name="social_security_delete"),
    path("export/excel/", views.export_social_security_to_excel, name="export_social_security_to_excel"),
    path("report/word/", views.generate_social_security_report, name="generate_social_security_report"),
]

