from django.shortcuts import render,redirect
from .forms import UserForm,FormBDE,FormDEVELOPER,FormCompany,FormQuestion,FormInterview
from .models import User,BDE,DEVELOPER,Company,Questions,Interview


def createUser(request):
  if request.method=="POST":
    form=UserForm(request.POST)
    if form.is_valid():
      form.save()
      return  redirect("retrive")

  else:
    form=UserForm()
  return render(request,'create.html',{'form':form})


def update_data(request,id):
  identity=User.objects.get(id=id)
  if request.method=="POST":
    form=UserForm(request.POST,instance=identity)
    if form.is_valid():
      form.save()
      return redirect('retrive')
  else:
    form=UserForm(instance=identity)
  return render(request,'create.html',{'form':form})

def delete_data(request,id):
  identity=User.objects.get(id=id)
  identity.delete()
  return redirect('retrive')


def createBDE(request):
  if request.method=="POST":
    form=FormBDE(request.POST)
    if form.is_valid():
      form.save()
      return  redirect("retrive")
  else:
    form=FormBDE()
  return render(request,'create.html',{'form':form})


def update_bde_data(request,id):
  identity=BDE.objects.get(id=id)
  if request.method=="POST":
    form=FormBDE(request.POST,instance=identity)
    if form.is_valid():
      form.save()
      return redirect('retrive')
  else:
    form=FormBDE(instance=identity)
  return render(request,'create.html',{'form':form})

def delete_bde_data(request,id):
  identity=BDE.objects.get(id=id)
  identity.delete()
  return redirect('retrive')

def createDEVELOPER(request):
  if request.method=="POST":
    form=FormDEVELOPER(request.POST)
    if form.is_valid():
      form.save()
      return redirect("retrive")
  else:
    form=FormDEVELOPER()
  return render(request,'createde.html',{'form':form})

def update_developer_data(request,id):
  identity=DEVELOPER.objects.get(id=id)
  if request.method=="POST":
    form=FormDEVELOPER(request.POST,instance=identity)
    if form.is_valid():
      form.save()
      return redirect('retrive')
  else:
    form=FormDEVELOPER(instance=identity)
  return render(request,'create.html',{'form':form})

def delete_developer_data(request,id):
  identity=DEVELOPER.objects.get(id=id)
  identity.delete()
  return redirect('retrive')

def createCompany(request):
  if request.method=="POST":
    form=FormCompany(request.POST)
    if form.is_valid():
      form.save()
      return redirect("retrive")
  else:
    form=FormCompany()
  return render(request,'create.html',{'form':form})

def update_company_data(request,id):
  identity=Company.objects.get(id=id)
  if request.method=="POST":
    form=FormCompany(request.POST,instance=identity)
    if form.is_valid():
      form.save()
      return redirect('retrive')
  else:
    form=FormCompany(instance=identity)
  return render(request,'create.html',{'form':form})

def delete_company_data(request,id):
  identity=Company.objects.get(id=id)
  identity.delete()
  return redirect('retrive')

def createQuestions(request):
  if request.method=="POST":
    form=FormQuestion(request.POST)
    if form.is_valid():
      form.save()
      return redirect("retrive")
  else:
    form=FormQuestion()
  return render(request,'create.html',{'form':form})

def updatequestions(request,id):
  identity=Questions.objects.get(id=id)
  if request.method=="POST":
    form=FormQuestion(request.POST,instance=identity)
    if form.is_valid():
      form.save()
      return redirect('retrive')
  else:
    form=FormQuestion(instance=identity)
  return render(request,'create.html',{'form':form})

def deletequestions(request,id):
  identity=Questions.objects.get(id=id)
  identity.delete()
  return redirect('retrive')
    



 # Create your views here.

def createInterview(request):
  if request.method=="POST":
    form=FormInterview(request.POST)
    if form.is_valid():
      form.save()
      return redirect("retrive")
  else:
    form=FormInterview()
  return render(request,'create.html',{'form':form})

def updateInterview(request,id):
  identity=Interview.objects.get(id=id)
  if request.method=="POST":
    form=FormInterview(request.POST,instance=identity)
    if form.is_valid():
      form.save()
      return redirect('retrive')
  else:
    form=FormInterview(instance=identity)
    return render(request,'create.html',{'form':form})

def deleteInterview(request,id):
  identity=Interview.objects.get(id=id)
  identity.delete()
  return redirect('retrive')


def RetrieveBDE(request):
  if request.method=="GET":
    datauser = User.objects.all()
    data=BDE.objects.all()
    datadeveloper = DEVELOPER.objects.all()
    company=Company.objects.all()
    question=Questions.objects.all()
    interview=Interview.objects.all()
    context ={
                'data':data,
                'datauser':datauser,
                'datadeveloper':datadeveloper,
                'company':company,
                'question':question,
                'interview':interview
              }
  return render(request,'retrieve.html',context)
  






