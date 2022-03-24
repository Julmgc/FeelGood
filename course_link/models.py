from django.db import models
from sinta_se_bem.base_classes import GenericWithUUID
# Create your models here.

class CourseLink(GenericWithUUID):
    link = models.CharField(max_length=256)
