from django.urls import path
from . import views

app_name = "polls"

urlpatterns = [
    # example: /polls/
    path("", views.IndexView.as_view(), name="index"),
    # example: /polls/5
    path("<int:pk>/the_best_details/", views.DetailView.as_view(), name="The Detail"),
    # example: /polls/5/results
    path("<int:pk>/results/", views.ResultView.as_view(), name="The Results"),
    # example: /polls/5/vote
    path("<int:question_id>/vote/", views.vote, name="voting")
]