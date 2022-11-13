from django.db import models


class Assets(models.Model):
    name = models.CharField(max_length=80)
    brand = models.CharField(max_length=80)
    device_model = models.CharField(max_length=80)
    purchase_date = models.DateField(auto_now=False)
    condition_checkedOut = models.CharField(max_length=50)
    condition_returned = models.CharField(max_length=50)

    class Meta:
        ordering = ('-purchase_date',)
        verbose_name_plural = 'Asstes'

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=80, blank=False, null=False)
    employee_id = models.CharField(max_length=10, blank=False, null=False)
    company_name = models.CharField(max_length=20, blank=False, null=False)
    company_address = models.TextField(default="-",)
    employee_contact = models.CharField(max_length=15, blank=False, null=False)
    employee_email = models.EmailField(unique=True, blank=False, null=False)
    employee_dept = models.CharField(max_length=50)

    class Meta:
        ordering = ('-employee_id',)
        verbose_name_plural = 'Emploies'

    def __str__(self):
        return self.name
