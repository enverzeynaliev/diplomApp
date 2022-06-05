from django.db import models


class departments(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    descriptionformat = models.IntegerField()
    parent = models.IntegerField()
    sortorder = models.IntegerField()
    coursecount = models.IntegerField()
    depth = models.IntegerField()
    path = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class course_on_categories(models.Model):
    id = models.IntegerField(primary_key=True)
    fullname = models.TextField(default='')
    displayname = models.TextField(default='')
    shortname = models.CharField(max_length=250, default='')
    categoryid = models.IntegerField()
    categoryname = models.CharField(max_length=250, default='')
    # sortorder = models.CharField(max_length=200, default='')
    # summary = models.CharField(max_length=200, default='')
    # summaryformat = models.CharField(max_length=200, default='')
    # summaryfiles = models.JSONField(decoder=json.JSONDecoder)
    # overviewfiles = models.JSONField(decoder=json.JSONDecoder)
    # # overviewfiles_filename = models.CharField(max_length=200, default='')
    # # overviewfiles_filepath = models.CharField(max_length=200, default='')
    # # overviewfiles_filesize = models.CharField(max_length=200, default='')
    # # overviewfiles_fileurl = models.CharField(max_length=200, default='')
    # # overviewfiles_timemodified = models.CharField(max_length=200, default='')
    # # overviewfiles_mimetype = models.FloatField(default=0)
    # contacts = models.JSONField(decoder=json.JSONDecoder)
    # # contacts_id = models.CharField(max_length=200, default='')
    # # contacts_fullname = models.FloatField(default=0)
    # enrollmentmethods = models.JSONField(decoder=json.JSONDecoder)

    def __int__(self):
        return self.categoryid
