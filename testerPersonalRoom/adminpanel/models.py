from django.db import models


class departments(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    descriptionformat = models.IntegerField()
    parent = models.IntegerField()
    sortorder = models.IntegerField()
    coursecount = models.IntegerField()
    depth = models.IntegerField()
    path = models.CharField(max_length=100)

    def __str__(self):
        return self.id
