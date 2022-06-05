from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django import forms


class mdl_events(models.Model):
    id = models.BigIntegerField('id', primary_key=True)
    eventname = models.CharField('eventname', max_length=255, default='')
    component = models.CharField('component', max_length=100, default='')
    action = models.CharField('action', max_length=100, default='')
    target = models.CharField('target', max_length=100, default='')
    objecttable = models.CharField('objecttable', max_length=50, default='')
    objectid = models.BigIntegerField('objectid', default=0)
    crud = models.CharField('crud', max_length=1, default='')
    edulevel = models.SmallIntegerField('edulevel')
    contextid = models.BigIntegerField('contextid')
    contextlevel = models.BigIntegerField('contextlevel')
    contextinstanceid = models.BigIntegerField('contextinstanceid')
    userid = models.BigIntegerField('userid')
    courseid = models.BigIntegerField('courseid', default=0)
    relateduserid = models.BigIntegerField('relateduserid', default=0)
    anonymous = models.SmallIntegerField('anonymous', default=0)
    other = models.TextField('other', max_length=255, default='')
    timecreated = models.BigIntegerField('timecreated')
    origin = models.CharField('origin', max_length=255, default='')
    ip = models.CharField('ip', max_length=255, default='')
    realuserid = models.BigIntegerField('realuserid', default=0)


class userRegistration(UserCreationForm):
    firstname = forms.CharField(max_length=255)
    lastname = forms.CharField(max_length=255)
    email = forms.EmailField(required=True)
