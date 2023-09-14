from django.shortcuts import render
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from django.db.models import signals
from tastypie.authentication import BasicAuthentication,Authentication,ApiKeyAuthentication
from tastypie.models import create_api_key
# from django.db.models.us
# Create your views here.
from Movies.models import Movie,Genre
# Create your models here.

signals.post_save.connect(create_api_key,sender=Movie)


class CustomeAuthentication(Authentication):
    def is_authenticated(self, request, **kwargs):
        if "smart" in request.user.username :
            return True
        return False
    def get_identifier(self, request):
        return request.user.username

class MovieResource(ModelResource):
    class Meta:
        queryset = Movie.objects.all()
        excludes = ['date_created',"dispo"]
        fields = ["title","type","related_year","number_in_stock","daily_rate"]
        allowed_methods = ["get","put"]
        authentication = BasicAuthentication()
        Authorization = Authorization()


class GenreResource(ModelResource):
    class Meta:
        queryset = Genre.objects.all()
        resource_name = "type"