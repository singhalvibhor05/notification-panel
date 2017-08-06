# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

class NotificationsUsers(models.Model):
    user = models.ForeignKey(User)
    notification = models.ForeignKey("Notifications")
    is_sent = models.BooleanField(default=False)
    modified_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "{} | {}".format(self.user, self.notification)


class Notifications(models.Model):
    """
    Model to save notifications requested to send
    """
    DEVICE = "D"
    EMAIL = "E"
    SMS = "S"

    NOTIFICATION_CHOICES = [
        (DEVICE, "Device"),
        (EMAIL, "E-Mail"),
        (SMS, "SMS")
    ]

    header = models.CharField(max_length=150)
    content = models.CharField(max_length=150)
    image_url = models.URLField()
    send_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    user = models.ManyToManyField(User, related_name='users', through=NotificationsUsers)
    category = models.CharField(choices=NOTIFICATION_CHOICES, max_length=2)
    is_cancelled = models.BooleanField(default=False)

    def __unicode__(self):
        return "{} | {}".format(self.header, self.created_at)
