from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField()


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Companies"

class HiringManager(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    url = models.URLField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, default=None)
    hiring_manager = models.ForeignKey(HiringManager, on_delete=models.CASCADE, default=None)
    date_applied = models.DateField(default=None)

    def __str__(self):
        return self.title
