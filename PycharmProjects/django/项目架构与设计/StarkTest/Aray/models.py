from django.db import models

# Create your models here.

class Host(models.Model):
    hostname = models.CharField(max_length=32)
    key = models.TextField()
    status_choices = ((0,"Waiting Approval"),
                      (1,"Accepted"),
                      (2,"Rejected"))
    status = models.SmallIntegerField(choices=status_choices)

    def __str__(self):
        return self.hostname

class HostGroup(models.Model):
    name = models.CharField(max_length=64,unique=True)
    hosts = models.ManyToManyField(Host,blank=True)

    def __str__(self):
        return self.name
