
# https://www.w3schools.com/django/django_queryset_filter.php

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from Medassistapp.models import Patient
from Medassistapp.serializers import PatientSerializer


from rest_framework.decorators import api_view

@api_view(['GET','POST','DELETE'])
def Submit_User(request):
    try:
        if request.method == 'POST':
            user_serializer=PatientSerializer(data=request.data)
            print(request.data)
            if(user_serializer.is_valid()):
                print("Data is valid")
                user_serializer.save()
                return JsonResponse({"message":'User Details Submitted Successfully',"status":True},)
            else:
                return JsonResponse({"message":'Fail to Submit User Details',"status":False},)
    except Exception as e:
        print('Error:',e)
        return JsonResponse({"message":'Fail to Submit User Details',"status":False},)

@api_view(['GET', 'POST', 'DELETE'])
def User_Search(request):
  if request.method=='POST':
  
    email=request.data['emailid']
    pwd=request.data['password']
    patient=Patient.objects.all().filter(emailid=email,password=pwd)
     
    patient_serializer = PatientSerializer(patient,many=True)
    if(len(patient_serializer.data)==1):
     return JsonResponse({"data":patient_serializer.data,"status":True },safe=False)
    else:
     return JsonResponse({"data":[],"status":False },safe=False)  
       
  return JsonResponse({"data":{},"status":False },safe=False)    
       

@api_view(['GET', 'POST', 'DELETE'])
def Edit_UserPhoto(request):
 try:
   if request.method=='POST':
      patient=Patient.objects.get(pk=request.data['emailid'])
      patient.userphoto=request.data['userphoto']
      patient.save()
      return JsonResponse({"message":'User Image Edited Successfully',"status":True},safe=False)
 except Exception as e:
    print("Error Picture:",e)
    return JsonResponse({"message":'Fail to edit user image',"status":False},safe=False) 
@api_view(['GET', 'POST', 'DELETE'])
def Edit_UserPatient(request):
  try:
   if request.method=='POST':
      patient=Patient.objects.get(pk=request.data['emailid'])
      patient.usernamee=request.data['username']
      patient.dob=request.data['dob']
      patient.gender=request.data['gender']
      patient.city=request.data['city']
      patient.mobileno=request.data['mobileno']
      #patient.emailid=request.data['emailid']
      patient.save()
      return JsonResponse({"message":'User Edited Profile Successfully',"status":True},safe=False)
  except Exception as e:
    print("Error Picture:",e)
    return JsonResponse({"message":'Fail to Edit User Profile',"status":False},safe=False) 
@api_view(['GET', 'POST', 'DELETE'])
def Edit_UserDetials(request):
 try:
   if request.method=='POST':
      patient=Patient.objects.get(pk=request.data['emailid'])
      patient.password=request.data['password']
      patient.save()
      return JsonResponse({"message":'User Edited Successfully',"status":True},safe=False)
 except Exception as e:
    print("Error Picture:",e)
    return JsonResponse({"message":'Fail to edit user',"status":False},safe=False) 
@api_view(['GET', 'POST', 'DELETE'])
def Edit_UserDelete(request):
 try:
   if request.method=='POST':
      patient=Patient.objects.get(pk=request.data['emailid'])
      patient.delete()
      return JsonResponse({"message":'User Deleted Successfully',"status":True},safe=False)
 except Exception as e:
    print("Error delete:",e)
    return JsonResponse({"message":'Fail to Delete User',"status":False},safe=False) 
@api_view(['GET', 'POST', 'DELETE'])
def Check_Emailid(request):
  if request.method=='POST':  
    emailid=request.data['emailid']
    checkmobile=Patient.objects.all().filter(emailid=emailid)
    checkmobile_serializer =PatientSerializer(checkmobile,many=True)
    if(checkmobile_serializer.data):
     return JsonResponse({"data":checkmobile_serializer.data,"status":True },safe=False)
    else:
     return JsonResponse({"data":[],"status":False },safe=False)  
       
  return JsonResponse({"data":{},"status":False },safe=False)  

