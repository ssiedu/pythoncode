from django.db import models

# Create your models here.
class ManageUser(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=500)
    userType = models.CharField(max_length=20, default='Student')
    def __str__(self):
        return self.firstName + " " + self.lastName
class Category(models.Model):
    cname = models.CharField(max_length=250)
    def __str__(self):
        return self.cname
class Notice(models.Model):
    notice_subject = models.CharField(max_length=100)
    notice_date = models.DateTimeField()
    notice_text = models.CharField(max_length=500)
    cname = models.ForeignKey(Category, related_name = 'category_name', on_delete='Cascade')
    def __str__(self):
        return self.notice_text

