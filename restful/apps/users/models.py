from __future__ import unicode_literals
from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# NAME_REGEX = re.compile(r'^[a-zA-Z]*$')

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['fullname']) < 2:
            errors['fullname'] = "Fullname must contain at least 3 characters"
        # elif not NAME_REGEX.match(postData['fullname']):
        #     errors['fullname'] = 'Fullname cannot contain special characters or numbers'

        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'Email is not valid!'
        return errors

class User(models.Model):
    fullname = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
    def __str__(self):
        return self.fullname
