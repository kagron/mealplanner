from django.urls import include, path
from django.contrib import admin
from meals import views
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql', csrf_exempt(GraphQLView.as_view(graphiql=True)))
]