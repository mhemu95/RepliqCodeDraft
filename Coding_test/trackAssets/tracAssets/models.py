from django.db import models


class AssetCategory(models.Model):
    category_name = models.CharField(max_length=20)

    def __str__(self):
        return self.category_name


class AssetType(models.Model):
    category = models.ForeignKey(AssetCategory, on_delete=models.CASCADE)
    service_tag = models.CharField(max_length=50)
    asset_model = models.CharField(max_length=50)
    active = models.BooleanField(default=False)
    purchase_date= models.DateField(auto_now=False)

    class Meta:
        verbose_name = 'Asset'
        verbose_name_plural = 'Assets'
        ordering = ['-id']

    def __str__(self):
        return self.asset_model


class Employee(models.Model):
    name = models.CharField(max_length=50)
    emp_id = models.CharField(max_length=15)
    email = models.EmailField(unique=True, null=False, blank=False)
    phone = models.CharField(max_length=15)
    department = models.CharField(max_length=20)
    com_name = models.CharField(max_length=20)
    com_address = models.TextField(default='-')
    com_contact = models.CharField(max_length=15)

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

    def __str__(self):
        return self.name


class AssetTracks(models.Model):
    asset = models.ForeignKey(AssetType, on_delete=models.CASCADE)
    taken_by = models.ForeignKey(Employee, on_delete=models.CASCADE)
    take_out_time = models.DateField(auto_now=False)
    return_time = models.DateField(null=True, blank=True)
    return_condition = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        db_table = 'asset_track'
        managed = True
        verbose_name_plural = 'Asset_Track'

    def __str__(self):
        return self.asset.asset_model


class Inventory(models.Model):
    asset_type = models.ForeignKey(AssetCategory, on_delete=models.CASCADE)
    in_stock = models.PositiveIntegerField()
    left_for_check_out = models.PositiveIntegerField()
    
    class Meta:
        db_table = 'inventory'
        managed = True
        verbose_name_plural = 'Inventory'

    def __str__(self):
        return self.asset_type.category_name + ' | ' + str(self.in_stock)
