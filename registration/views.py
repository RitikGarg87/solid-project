from copy import error
from .models import User
from django.shortcuts import render
from .serializers import RegisterSerializer
from django.core.mail import send_mail
# Create your views here.
from rest_framework.response import Response
from rest_framework import decorators, permissions, status
from cherrypicker import CherryPicker

def errors(b):
    picker = CherryPicker(b).flatten().get()    
    kk = {}
    for i,j in picker.items():
        td = i.count("_")
        if td>1:
            b = i.index("_")
            c = i.index("_",b+1)
            kk[i[:c]] = j
        else:
            b= i.index("_")
            kk[i[:b]] = j
    return kk

@decorators.api_view(["POST"])
@decorators.permission_classes([permissions.AllowAny])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        obj = serializer.save()
        subject = "User Registration"
        Message = "You are successfully Registered"
        mail = send_mail(subject, Message, 'gargritik2609@gmail.com',[obj.email], fail_silently = True)
        return Response({'status':status.HTTP_200_OK,'message':'Success', 'email_send':mail})

    error = errors(serializer.errors)
    return Response({"status":status.HTTP_400_BAD_REQUEST, "message":"data invalid","result":{"errors":error}})
    
@decorators.api_view(["GET"])
@decorators.permission_classes([permissions.AllowAny])
def show(request):
    try:
        data = User.objects.all()
        serializerdata = RegisterSerializer(data, many = True)
        return Response(serializerdata.data)

    except:
        return Response({'status':status.HTTP_200_OK, 'message':'data not found'}) 


