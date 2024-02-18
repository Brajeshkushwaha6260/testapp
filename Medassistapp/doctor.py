from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.shortcuts import render
from  Medassistapp.models import States
from  Medassistapp.models import City

 
from  Medassistapp.models import Doctors
from  Medassistapp.serializers import DoctorSerializer
from  Medassistapp.serializers import DoctorGetSerializer
from Medassistapp.models import Questions
from Medassistapp.serializers import QuestionSerializer
from Medassistapp.serializers import QuestionGetSerializer

from Medassistapp.models import SubQuestions
from Medassistapp.serializers import SubQuestionsGetSerializer
from Medassistapp.serializers import SubQuestionsSerializer

from rest_framework.decorators import api_view

@api_view(['GET', 'POST', 'DELETE'])
def Doctors_List(request):
 if request.method=='GET':
    doctorlist=Doctors.objects.all()
    doctor_serializer = DoctorGetSerializer(doctorlist,many=True)
    return JsonResponse(doctor_serializer.data,safe=False)
 return JsonResponse({},safe=False) 


@api_view(['GET', 'POST', 'DELETE'])
def Submit_Doctor(request):
  
 try:
   if request.method=='POST':
    doctor_serializer=DoctorSerializer(data=request.data)
    # print(doctor_serializer,doctor_serializer.is_valid(),request.data)
    if(doctor_serializer.is_valid()):
    
      doctor_serializer.save()
      return JsonResponse({"message":'Doctor Submitted Successfully',"status":True},safe=False)
    else:
      return JsonResponse({"message":'Fail to  submit doctor',"status":False},safe=False) 
 except Exception as e:
    print("Error submit:",e)
    return JsonResponse({"message":'Fail to  submit doctor',"status":False},safe=False)
@api_view(['GET', 'POST', 'DELETE'])
def Doctors_P(request):
 try:
   if request.method=='POST':
      doctors=Doctors.objects.get(pk=request.data['id'])
      doctors.password=request.data['password']
      doctors.save()
      return JsonResponse({"message":'Doctor Edited Successfully',"status":True},safe=False)
 except Exception as e:
    print("Error edit:",e)
    return JsonResponse({"message":'Fail to  Edit doctor',"status":False},safe=False)  
 
@api_view(['GET', 'POST', 'DELETE'])
def Edit_Doctor(request):
  
 try:
   if request.method=='POST':
   
      doctors=Doctors.objects.get(pk=request.data['id'])
      doctors.category_id=request.data['category']
      doctors.doctorname=request.data['doctorname']
      doctors.gender=request.data['gender']
      doctors.dob=request.data['dob']
      doctors.states_id=request.data['states']
      doctors.city_id=request.data['city']
      doctors.address=request.data['address']
      doctors.qualification=request.data['qualification']
      doctors.emailid=request.data['emailid']
      doctors.mobileno=request.data['mobileno']
      doctors.password=request.data['password']
      doctors.save()
      return JsonResponse({"message":'Doctor Edited Successfully',"status":True},safe=False)
   
 except Exception as e:
    print("Error edit:",e)
    return JsonResponse({"message":'Fail to  Edit doctor',"status":False},safe=False) 
 
@api_view(['GET', 'POST', 'DELETE'])
def Delete_Doctor(request):
  
 try:
   if request.method=='POST':
      print(request.data)
      doctors=Doctors.objects.get(pk=request.data['id'])
      doctors.delete()
      return JsonResponse({"message":'Doctor Deleted Successfully',"status":True},safe=False)
   
 except Exception as e:
    print("Error delete:",e)
    return JsonResponse({"message":'Fail to Delete submit doctor',"status":False},safe=False) 
  


@api_view(['GET', 'POST', 'DELETE'])
def Edit_Picture(request):
  
 try:
   if request.method=='POST':
      doctors=Doctors.objects.get(pk=request.data['id'])
      doctors.photograph=request.data['photograph']
      doctors.save()
      return JsonResponse({"message":'Doctor Image Edited Successfully',"status":True},safe=False)
   
 except Exception as e:
    print("Error Picture:",e)
    return JsonResponse({"message":'Fail to edit  doctor image',"status":False},safe=False) 
@api_view(['GET', 'POST', 'DELETE'])
def Doctor_Login(request): 
   if request.method=='POST':
      email=request.data['emailid']
      pwd=request.data['password']
      doctor=Doctors.objects.all().filter(emailid=email,password=pwd)
      doctor_serializer=DoctorSerializer(doctor,many=True)
      if(len(doctor_serializer.data)==1):
         return JsonResponse({'data':doctor_serializer.data,'status':True},safe=False)
      else:
         return JsonResponse({'data':[],'status':False},safe=False)
   return JsonResponse({"data":{},"status":False},safe=False)
@api_view(['GET', 'POST', 'DELETE'])
def Doctor_Forgot(request): 
   if request.method=='POST':
      emailid=request.data['emailid']
      doctor=Doctors.objects.all().filter(emailid=emailid)
      doctor_serializer=DoctorSerializer(doctor,many=True)
      if(doctor_serializer.data):
         return JsonResponse({'data':doctor_serializer.data,'status':True},safe=False)
      else:
         return JsonResponse({'data':[],'status':False},safe=False)
   return JsonResponse({"data":{},"status":False},safe=False)

@api_view(['GET', 'POST', 'DELETE'])
def Doctor_Questions(request):
   if request.method=='POST':
     doctorid=request.data['doctorid']
     questions=SubQuestions.objects.all().filter(doctor_id=doctorid)
     questions_serializer = SubQuestionsGetSerializer(questions,many=True)
     return JsonResponse({"data":questions_serializer.data,"status":True },safe=False)
   else:
     return JsonResponse({"data":[],"status":False },safe=False) 
@api_view(['GET', 'POST', 'DELETE'])
def Doctor_C(request):
   if request.method=='POST':
     id=request.data['id']
     questions=Doctors.objects.all().filter(id=id)
     questions_serializer = DoctorGetSerializer(questions,many=True)
     return JsonResponse({"data":questions_serializer.data,"status":True },safe=False)
   else:
     return JsonResponse({"data":[],"status":False },safe=False) 