from rest_framework import  serializers
from .models import User

class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(allow_null=True, required=False)
    class Meta:
        model = User
        fields = ['username','fullname', 'phone', 'email','datebirth']

    def validate_phone(self, value):
        gg = ''' !()-[]{};:'",<>.=/?@#$%^&*_~ '''

        for kk in range(65,91):
            if chr(kk) in value:
                raise serializers.ValidationError({'phone': 'Enter only numbers.'})
        for kk in range(97,123):
            if chr(kk) in value:
                raise serializers.ValidationError({'phone': 'Enter only numbers.'})
        for kk in gg:
            if kk in value:
                raise serializers.ValidationError({'phone': 'Enter only numbers.'})
        if User.objects.filter(phone=value):
            raise serializers.ValidationError({'phone':'This phone has already taken'}) 
        if len(value)>10 or len(value)<10:
            raise serializers.ValidationError({'phone': 'Enter only 10 digits active number'}) 
        return value