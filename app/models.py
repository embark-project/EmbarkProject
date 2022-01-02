from django.db import models

# Create your models here.
class User_type(models.Model):
    username = models.CharField(max_length=20, blank=True)
    password = models.CharField(max_length=20, null=True)
    email = models.EmailField(max_length=20, null=True)
    address = models.CharField(max_length=40, null=True)
    dob = models.DateField(max_length=15, null=True)
    phone = models.CharField(max_length=10, null=True)

    class Meta:
      db_table = "User_type"

    def __unicode__(self):
        return "{0} {1} {2} {3} {4}".format(
            self, self.username, self.password, self.email, self.address, self.dob, self.phone)

    