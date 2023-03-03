from django.urls import path
from . import views

app_name = "polls"

urlpatterns = [
    # example: /polls/
    path("", views.index, name="index"),
    # example: /polls/5
    path("<int:question_id>/the_best_details/", views.detail, name="The Detail"),
    # example: /polls/5/results
    path("<int:question_identifier>/results/", views.results, name="The Results"),
    # example: /polls/5/vote
    path("<int:question_id>/vote/", views.vote, name="voting")
]