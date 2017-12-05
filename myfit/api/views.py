# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from api.models import Data,User,Trainer,Workout
from api.serializers import DataSerializer, UserSerializer,TrainerSerializer,WorkoutSerializer


class DataViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Data objects """
    queryset = Data.objects.all()
    serializer_class = DataSerializer


class UserViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing User objects """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class WorkoutViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Workout objects """
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

class TrainerViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing trainer objects """
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer