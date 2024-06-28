from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Job, Company, HiringManager

# Create your views here.


def index(request):
    jobs_list_latest = Job.objects.all()[:5]

    context = {"jobs_list": jobs_list_latest}
    return render(request, "jobs/index.html", context)

def detail(request, job_id):
    job = Job.objects.get(pk=job_id)
    return render(request, "jobs/detail.html", {"job": job})

def all_jobs(request):
    jobs_list = Job.objects.all()
    companies_list = Company.objects.all()
    hiring_managers_list = HiringManager.objects.all()
    
    context = {
        "jobs_list": jobs_list,
        "companies_list": companies_list,
        "hiring_managers_list": hiring_managers_list
    }
    return render(request, "jobs/all_jobs.html", context)


def create_job(request):
    if request.method == "POST":
        title = request.POST.get("job_title")
        description = request.POST.get("job_description")
        company_id = request.POST.get("company")
        hiring_manager_id = request.POST.get("hiring_manager")
        date_applied = request.POST.get("date_applied")
        
        company = Company.objects.get(id=company_id)
        hiring_manager = HiringManager.objects.get(id=hiring_manager_id)
        
        job = Job(
            title=title,
            description=description,
            company=company,
            hiring_manager=hiring_manager,
            date_applied=date_applied
        )
        job.save()
        return redirect("jobs_app:detail", job_id=job.id)
    companies_list = Company.objects.all()
    hiring_managers_list = HiringManager.objects.all()
    return render(request, "jobs/create_job.html", {
        "companies_list": companies_list,
        "hiring_managers_list": hiring_managers_list
    })

def delete_job(request, job_id):
    job = Job.objects.get(pk=job_id)
    job.delete()
    return redirect("jobs:all_jobs")

def companies(request):
    companies_list = Company.objects.all()
    context = {"companies_list": companies_list}
    return render(request, "jobs/companies.html", context)

def company_detail(request, company_id):
    company = Company.objects.get(pk=company_id)
    return render(request, "jobs/company_detail.html", {"company": company})


def creating_company(request):
    if request.method == "POST":
        name = request.POST.get("company_name")
        location = request.POST.get("company_location")
        description = request.POST.get("company_description")
        company = Company(name=name, location=location, description=description)
        company.save()
        return render(request, "jobs/company_detail.html", {"company": company})
    return render(request, "jobs/creating_company.html")

def delete_company(request, company_id):
    company = Company.objects.get(pk=company_id)
    company.delete()
    return redirect("jobs:companies")


def hiring_managers(request):
    hiring_managers_list = HiringManager.objects.all()
    context = {"hiring_managers_list": hiring_managers_list}
    return render(request, "jobs/hiring_managers.html", context)

def hiring_manager_detail(request, hiring_manager_id):
    hiring_manager = HiringManager.objects.get(pk=hiring_manager_id)
    return render(request, "jobs/hiring_manager_detail.html", {"hiring_manager": hiring_manager})

def creating_hiring_manager(request):
    if request.method == "POST":
        name = request.POST.get("hiring_manager_name")
        company_name = request.POST.get("company_name")
        url = request.POST.get("linkedIn_url")
        email = request.POST.get("email")
        hiring_manager = HiringManager(name=name, url=url, company_name=company_name,email=email)
        hiring_manager.save()
        return render(request, "jobs/hiring_manager_detail.html", {"hiring_manager": hiring_manager})
    return render(request, "jobs/creating_hiring_manager.html")

def delete_hiring_manager(request, hiring_manager_id):
    hiring_manager = HiringManager.objects.get(pk=hiring_manager_id)
    hiring_manager.delete()
    return redirect("jobs:hiring_managers")


