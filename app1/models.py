from django.db import models
from django.contrib.auth.models import AbstractUser,User


class User(AbstractUser):
  first_name=models.CharField(max_length=20)
  last_name=models.CharField(max_length=20)
  username=models.CharField(max_length=20)
  password=models.CharField(max_length=50)
  email = models.EmailField(max_length=254, unique=True)  
  USERNAME_FIELD="email"
  REQUIRED_FIELDS=['first_name','last_name','username','password']
  def __str__(self):
    return self.first_name

class BDE(models.Model):
  bde_name=models.CharField(max_length=50)
  def __str__(self):
    return self.bde_name

class DEVELOPER(models.Model):
  developer_name=models.CharField(max_length=100)
  def __str__(self):
    return self.developer_name

class Company(models.Model):
  company_name=models.CharField(max_length=50)
  location=models.CharField(max_length=150)
  def __str__(self):
    return self.company_name

class Questions(models.Model):  
  company_name=models.ForeignKey(Company,on_delete=models.CASCADE,max_length=20)
  question=models.TextField(max_length=200)
  answer=models.TextField(max_length=500)
  technology=models.CharField(max_length=20)
  question_level=models.CharField(max_length=50)

  def __str__(self):
    return self.technology


class Interview(models.Model):
  company_name=models.ForeignKey(Company,on_delete=models.CASCADE,max_length=20)
  scheduled_by=models.ForeignKey(BDE,on_delete=models.SET_NULL,max_length=20,null=True)
  interview_mode=models.CharField(max_length=20)
  technology=models.CharField(max_length=20)
  Interview_rounds=models.IntegerField(default=1)
  interviewer_name=models.ForeignKey(DEVELOPER,on_delete=models.CASCADE,max_length=20)
  candidate_name=models.CharField(max_length=100)
  interview_type=models.CharField(max_length=20)
  date=models.DateTimeField()
  created_date=models.DateTimeField(auto_now_add=True)
  updated_date=models.DateTimeField(auto_now=True)
  email=models.EmailField()
  job_title=models.CharField(max_length=50)
  position=models.CharField(max_length=30)




