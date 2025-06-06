from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Customer
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator


class SignUpSerializer(serializers.ModelSerializer):
    date_of_birth = serializers.DateField(required=True)
    gender = serializers.ChoiceField(choices=Customer.GENDER_CHOICES, required=True)

    # Address fields
    address_line_1 = serializers.CharField(required=False, allow_blank=True)
    address_line_2 = serializers.CharField(required=False, allow_blank=True)
    city = serializers.CharField(required=False, allow_blank=True)
    state = serializers.CharField(required=False, allow_blank=True)
    country = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'password',
            'date_of_birth',
            'gender',
            'address_line_1',
            'address_line_2',
            'city',
            'state',
            'country',
        )
        extra_kwargs = {
            'first_name': {'required': True, 'allow_blank': False},
            'last_name': {'required': True, 'allow_blank': False},
            'email': {'required': True, 'allow_blank': False},
            'password': {'required': True, 'allow_blank': False, 'min_length': 6},
        }

    def create(self, validated_data):
        date_of_birth = validated_data.pop('date_of_birth')
        gender = validated_data.pop('gender')

        address_line_1 = validated_data.pop('address_line_1', '')
        address_line_2 = validated_data.pop('address_line_2', '')
        city = validated_data.pop('city', '')
        state = validated_data.pop('state', '')
        country = validated_data.pop('country', '')

        email = validated_data['email']
        user = User.objects.create_user(
            username=email,
            email=email,
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            is_active=False  # Email verify అయ్యే వరకు యూజర్ active కాదు
        )
        Customer.objects.create(
            user=user,
            date_of_birth=date_of_birth,
            gender=gender,
            address_line_1=address_line_1,
            address_line_2=address_line_2,
            city=city,
            state=state,
            country=country
        )
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = (
            'date_of_birth',
            'gender',
            'address_line_1',
            'address_line_2',
            'city',
            'state',
            'country',
        )


class UserSerializer(serializers.ModelSerializer):
    userprofile = UserProfileSerializer()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'userprofile')


class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError("No user is associated with this email address.")
        return value


class PasswordResetSerializer(serializers.Serializer):
    new_password = serializers.CharField(write_only=True, min_length=6)
    token = serializers.CharField(write_only=True)
    uidb64 = serializers.CharField(write_only=True)

    def validate(self, data):
        try:
            uid = force_str(urlsafe_base64_decode(data['uidb64']))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            raise serializers.ValidationError("Invalid token or user ID")
        
        if not default_token_generator.check_token(user, data['token']):
            raise serializers.ValidationError("Invalid token")

        return data

    def save(self):
        uid = force_str(urlsafe_base64_decode(self.validated_data['uidb64']))
        user = User.objects.get(pk=uid)
        user.set_password(self.validated_data['new_password'])
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            if not User.objects.filter(email=email).exists():
                raise serializers.ValidationError('No user found with this email address.')

        return data
