from django.contrib import admin
from .models import BDE,User ,DEVELOPER ,Company ,Questions,Interview

admin.site.register(User)

class BDEAdmin(admin.ModelAdmin):
  # list_display=['scheduled_by','interview_schedule_date','candidate_name']
  list_display=['bde_name']
admin.site.register(BDE,BDEAdmin)

class DEVELOPERAdmin(admin.ModelAdmin):
  list_display=['developer_name']
admin.site.register(DEVELOPER,DEVELOPERAdmin)

class CompanyAdmin(admin.ModelAdmin):
  list_display=['company_name','location']
admin.site.register(Company,CompanyAdmin)


class QuestionsAdmin(admin.ModelAdmin):
  list_display=['company_name','question','answer','technology','question_level']
admin.site.register(Questions,QuestionsAdmin)
# Register your models here.

class InterviewAdmin(admin.ModelAdmin):
  list_display=['company_name','scheduled_by','interview_mode','technology','Interview_rounds','interviewer_name','candidate_name','interview_type','date','created_date','updated_date','email','job_title','position']
admin.site.register(Interview,InterviewAdmin)