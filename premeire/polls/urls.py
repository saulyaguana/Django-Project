from django.urls import path
from . import views

urlpatterns = [
    # example: /polls/
    path("", views.index, name="index"),
    # example: /polls/5
    path("<int:question_id>/", views.detail, name="The Detail"),
    # example: /polls/5/results
    path("<int:question_identifier>/results/", views.results, name="The Results"),
    # example: /polls/5/vote
    path("<int:question_id>/vote/", views.vote, name="voting")
]