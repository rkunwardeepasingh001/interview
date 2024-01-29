from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("createUser/",views.createUser,name="createuser"),
    path("createBDE/",views.createBDE,name="createBDE"),
    path("createdeveloper/",views.createDEVELOPER ,name="createDEVELOPER"),
    path("createcompany/",views.createCompany ,name="createCompany"),
    path("createinterview/",views.createInterview,name="createInterview"),
    path("createquestion/",views.createQuestions,name="createQuestion"),
    path("",views.RetrieveBDE,name="retrive"),

    path("update/<int:id>/",views.update_data,name="update"),
    path("delete/<int:id>/",views.delete_data,name="delete"),

    path("update/bde/<int:id>/",views.update_bde_data,name="bdeupdate"),
    path("delete/bde/<int:id>/",views.delete_bde_data,name="bdedelete"),

    path("update/developer/<int:id>/",views.update_developer_data,name="developerupdate"),
    path("delete/developer/<int:id>/",views.delete_developer_data,name="developerdelete"),

    path("update/company/<int:id>/",views.update_company_data,name="companyupdate"),
    path("delete/company/<int:id>/",views.delete_company_data,name="companydelete"),

    path("update/question/<int:id>/",views.updatequestions,name="questionupdate"),
    path("delete/question/<int:id>/",views.deletequestions,name="questiondelete"),

    path("update/interview/<int:id>/",views.updateInterview,name="interviewupdate"),
    path("delete/interview/<int:id>/",views.deleteInterview,name="interviewdelete"),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)