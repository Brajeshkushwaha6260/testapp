"""medassist_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Medassistapp import statecity
from Medassistapp import category
from Medassistapp import doctor,timings,questions,user,subquestions
from Medassistapp import answer
from Medassistapp import presciption
from django.urls import include, re_path


urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path(r'^api/statelist', statecity.State_List),
    re_path(r'^api/citylist', statecity.City_List),
    re_path(r'^api/scitylist', statecity.SCity_List),
    re_path(r'^api/categorylist', category.Category_List),
    re_path(r'^api/categorylists', category.Category_ListP),
    re_path(r'^api/doctorsubmit', doctor.Submit_Doctor),
    re_path(r'^api/doctoredit', doctor.Edit_Doctor),
    re_path(r'^api/doctorg', doctor.Doctors_P),
    re_path(r'^api/doctordelete', doctor.Delete_Doctor),
    re_path(r'^api/doctorpictureedit', doctor.Edit_Picture),
    re_path(r'^api/doctorlist', doctor.Doctors_List),
    re_path(r'^api/doctorc', doctor.Doctor_C),
    re_path(r'^api/edittimings',timings.EditTimings),
    re_path(r'^api/deletetimings',timings.DeleteTimings),
    re_path(r'^api/timingsubmit',timings.TimingSubmit),
    re_path(r'^api/dtiminglist',timings.TimingList),
    re_path(r'^api/dtimingslist',timings.TimingsList),
    re_path(r'^api/questionlist',questions.QuestionList),
    re_path(r'^api/usersubmit',user.Submit_User),
    re_path(r'^api/usersearch1',user.Check_Emailid),
    re_path(r'^api/edituserphoto',user.Edit_UserPhoto),
    re_path(r'^api/profileuseredit',user.Edit_UserPatient),
    re_path(r'^api/edituserdetials',user.Edit_UserDetials),
    re_path(r'^api/userdelete',user.Edit_UserDelete),
    re_path(r'^api/questionsubmit',questions.QuestionSubmit),
    re_path(r'^api/subquestionsubmit',subquestions.SubQuestionsSubmit),
    re_path(r'^api/usersearch',user.User_Search),
    re_path(r'^api/doctorlogin',doctor.Doctor_Login),
     re_path(r'^api/doctorforgot',doctor.Doctor_Forgot),
    re_path(r'^api/doctorquestions',doctor.Doctor_Questions),
    re_path(r'^api/answersubmit',answer.AnswerSubmit),
    re_path(r'^api/answerlist',answer.Answer_List),
    re_path(r'^api/prescriptionsubmit',presciption.Prescription_Submit),
    re_path(r'^api/showprescription',presciption.Prescription_List),
    re_path(r'^api/patientprescription',answer.Ans_Patient),

]
