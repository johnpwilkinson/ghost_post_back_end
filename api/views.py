from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from .serializers import PostSerializer
from back_end.models import Posts
from rest_framework.decorators import action
from rest_framework.response import Response


class AllPostsViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer

    @action(detail=True, methods=['post'])
    def up_vote(self, request, pk):
        print(pk)
        post = Posts.objects.get(pk=pk)
        post.votes += 1
        post.save()
        return Response()

    @action(detail=True, methods=['post'])
    def down_vote(self, request, pk):
        print(pk)
        post = Posts.objects.get(pk=pk)
        post.votes -= 1
        post.save()
        return Response()

   

class BoastPostsViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.filter(boast_or_roast=False).order_by('-submission_time')
    serializer_class = PostSerializer

class RoastPostsViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.filter(boast_or_roast=True).order_by('-submission_time')
    serializer_class = PostSerializer

class TopPostsViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.filter(boast_or_roast=True).order_by('-votes')
    serializer_class = PostSerializer