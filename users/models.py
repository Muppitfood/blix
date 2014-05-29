from django.db import models
from django.db.models import permalink

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=20, db_index=True)
    last_name = models.CharField(max_length=25, db_index=True)
    date_created = models.DateField(db_index=True, auto_now_add=True)
    email = models.EmailField(unique=True)

    def __unicode__(self):
        return self.first_name + ':' + str(self.id)

    @permalink
    def get_absolute_url(self):
        return ('view_user', [str(self.id)])
