from django.urls import path
from . import views

urlpatterns = [
    path("", views.citizen_account_list, name="citizen_account_list"),
    path("create/", views.citizen_account_create, name="citizen_account_create"),
    path("update/<int:pk>/", views.citizen_account_update, name="citizen_account_update"),
    path("delete/<int:pk>/", views.citizen_account_delete, name="citizen_account_delete"),
    path("export/excel/", views.export_citizen_account_to_excel, name="export_citizen_account_to_excel"),
    path("report/word/", views.generate_citizen_account_report, name="generate_citizen_account_report"),
]

