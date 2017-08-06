# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponseRedirect

from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework import status

from .models import Notifications, NotificationsUsers, User
from .serializers import NotificationsSerializer
from .forms import NotificationsForm


class NotificationsViewSet(viewsets.ModelViewSet):
    lookup_field = 'pk'
    queryset = Notifications.objects.all()
    serializer_class = NotificationsSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(),)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

        return Response({
            'status': 'Bad request',
            'message': 'Notifications could not be created with received data.',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


def index(request):
    """
    django function based view to render the template to capture the notification
    data
    :param request:
    :return:
    """

    if request.method == 'POST':
        form = NotificationsForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            for user in request.POST.get("user"):
                # not handling the expection as not existing user id
                user = User.objects.get(pk=user)
                NotificationsUsers.objects.create(user=user, notification=obj)
        return HttpResponseRedirect('/panel')

    form = NotificationsForm()
    context = {'form': form}
    return render(request, 'panel/index.html', context)
