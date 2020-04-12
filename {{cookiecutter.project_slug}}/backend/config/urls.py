from django.urls import path
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView


def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('graphql', csrf_exempt(GraphQLView.as_view(graphiql=settings.DEBUG))),
    path('sentry-debug/', trigger_error),
]
