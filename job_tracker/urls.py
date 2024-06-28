from django.urls import path

from . import views

app_name = "jobs_app"
urlpatterns = [
    path ("", views.index, name="index"),
    path ("all_jobs/", views.all_jobs, name="all_jobs"),
    path ("detail/<int:job_id>/", views.detail, name="detail"),
    path ("create_job/", views.create_job, name="create_job"),
    path ("delete_job/<int:job_id>/", views.delete_job, name="delete_job"),

    path ("companies/", views.companies, name="companies"),
    path ("company_detail/<int:company_id>/", views.company_detail, name="company_detail"),
    path ("creating_company/", views.creating_company, name="creating_company"),
    path ("delete_company/<int:company_id>/", views.delete_company, name="delete_company"),
    
    path ("hiring_managers/", views.hiring_managers, name="hiring_managers"),
    path ("hiring_manager_detail/<int:hiring_manager_id>/", views.hiring_manager_detail, name="hiring_manager_detail"),
    path ("creating_hiring_manager/", views.creating_hiring_manager, name="creating_hiring_manager"),
    path ("delete_hiring_manager/<int:hiring_manager_id>/", views.delete_hiring_manager, name="delete_hiring_manager"),
]