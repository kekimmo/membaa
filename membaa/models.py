
from django.db import Models

class Member (models.Model):
  nick = Models.CharField(max_length=50)
  name = Models.CharField(max_length=255)
  email = Models.EmailField(max_length=255)
  residence = Models.CharField(max_length=255)
  hyy_membership = Models.BooleanField()


