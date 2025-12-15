from django.urls import path
from . import views

urlpatterns = [
    path("", views.fak_list, name="fak_list"),
    path("create/", views.fak_create, name="fak_create"),
    path("update/<int:pk>/", views.fak_update, name="fak_update"),
    path("delete/<int:pk>/", views.fak_delete, name="fak_delete"),
    path("export/excel/", views.export_fak_to_excel, name="export_fak_to_excel"),
    path("report/word/", views.generate_fak_report, name="generate_fak_report"),
]

