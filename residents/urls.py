from django.urls import path
from . import views

urlpatterns = [
    path("", views.residents_list, name="residents_list"),
    path("create/", views.residents_create, name="residents_create"),
    path("update/<int:pk>/", views.residents_update, name="residents_update"),
    path("delete/<int:pk>/", views.residents_delete, name="residents_delete"),
    path("export/excel/", views.export_residents_to_excel, name="export_residents_to_excel"),
    path("report/word/", views.generate_residents_report, name="generate_residents_report"),
]

