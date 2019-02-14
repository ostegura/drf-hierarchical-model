from django.db import models
from mptt.models import MPTTModel, TreeForeignKey, TreeManyToManyField


vehicle_images_path = 'static/groups/images/vehicle_images'
vehicle_type_images_path = 'static/groups/images/vehicle_type_images'


class VehicleType(MPTTModel):
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        db_index=True,
        related_name='children'
    )
    picture = models.ImageField(upload_to=vehicle_type_images_path)
    name = models.CharField(max_length=64)
    description = models.TextField(
        max_length=512,
        blank=True,
        default=''
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(VehicleType, self).save(*args, **kwargs)


class Vehicle(models.Model):
    picture = models.ImageField(upload_to=vehicle_images_path)
    name = models.CharField(max_length=64)
    model_name = models.CharField(max_length=64)
    description = models.TextField(max_length=512, blank=True, default='')
    date = models.DateTimeField('date', auto_now=True)
    verified = models.BooleanField(blank=True)

    owner = models.ForeignKey(
        'auth.User',
        related_name='vehicles',
        on_delete=models.CASCADE,
        blank=True
    )

    types = TreeManyToManyField(
        'VehicleType',
        related_name='types',
        blank=True
    )

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Vehicle, self).save(*args, **kwargs)
