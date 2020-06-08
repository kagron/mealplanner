from django.urls import include, path
from django.contrib import admin
from meals import views
from graphene_django.views import GraphQLView

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql', GraphQLView.as_view(graphiql=True))
]