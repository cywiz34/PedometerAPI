from rest_framework import serializers
from api.models import Data,Trainer,User,Workout


class UserSerializer(serializers.ModelSerializer):
    """ Serializer to represent the User model """
    class Meta:
        model = User
        fields = ("uid","name","password","age","weight","bmi")


class TrainerSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Trainer model """
    class Meta:
        model = Trainer
        fields = ("tid","name","contact","lat","lon","location")


class WorkoutSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Workout model """
    class Meta:
        model = Workout
        fields = ("type","wid","efficiency")

class DataSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Data model """
    class Meta:
        model = Data
        fields = ("slno","uid","cal_intake","cal_burn","steps","run","cycle","cal_month","cal_week","cal_yesterday")