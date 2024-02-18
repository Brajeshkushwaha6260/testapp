from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from Medassistapp.models import Timings
from Medassistapp.serializers import TimingsSerializer
from Medassistapp.serializers import TimingsGetSerializer
from rest_framework import status

@api_view(['GET','POST','DELTE'])
def TimingSubmit(request):
    try:
        if request.method=="POST":
            print(request.data)
            timing_serializer=TimingsSerializer(data=request.data)
            if timing_serializer.is_valid():
                timing_serializer.save()
                return JsonResponse({'message':'Timings Submitted Successfully','status':True},safe=False)
            else:
                return JsonResponse({'message':'Fail to Submit timings','status':False},safe=False)
    except Exception as error:
        print('Error',error)
        return JsonResponse({'messgae':'Fail to submit timings','status':False},safe=False)
@api_view(['GET','POST','DELETE'])
def TimingList(request):
    if request.method=='GET':
        timing_list=Timings.objects.all()
        timing_serializer=TimingsGetSerializer(timing_list,many=True)
        return JsonResponse(timing_serializer.data,safe=False)
    else:
        return JsonResponse({},safe=False)
@api_view(['DELETE','POST','GET'])
def EditTimings(request):
    try:
        if(request.method=='POST'):
            timings=Timings.objects.get(pk=request.data['id'])
            timings.starttimings=request.data['starttimings']
            timings.endtimings=request.data['endtimings']
            timings.days=request.data['days']
            timings.status=request.data['status']
            timings.save()
            return JsonResponse({'message':'Doctor Timings Edit Successfully','status':True},safe=False)
    except Exception as error:
        return JsonResponse({'message':'Fail to Edit Doctor Timings','status':False},safe=False)
@api_view(['DELETE','POST','GET'])
def DeleteTimings(request):
    try:
        if(request.method=='POST'):
            timings=Timings.objects.get(pk=request.data['id'])
            timings.delete()
            return JsonResponse({'message':'Doctor Session Delete Successfully','status':True},safe=False)
    except Exception as error:
        JsonResponse({'message':'Doctor Timings not Deleted','status':False},safe=False)
@api_view(['DELETE','POST','GET'])
def TimingsList(request):
    if request.method=="POST":
        doctorid=request.data['doctorid']
        doctorlist=Timings.objects.all().filter(doctor_id=doctorid)
        doctorlist_serializers=TimingsGetSerializer(doctorlist,many=True)
        return JsonResponse(doctorlist_serializers.data,safe=False)
    return JsonResponse({},safe=False) 
