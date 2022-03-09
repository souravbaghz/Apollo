# Copyright (c) 2008 Joost Cassee
# Licensed under the terms of the MIT License (see LICENSE.txt)
from django.urls import path

from Work import views

urlpatterns = [
    path("download/<str:filename>", views.GetExpFromServerToAgent, name="Download"),
]
