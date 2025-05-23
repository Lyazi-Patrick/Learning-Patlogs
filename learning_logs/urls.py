"""Defines URL patterns for learning_logs."""
from django.urls import path
from . import views #the dot tells py to import the views.py module from the same folder as the current Urls.py module
app_name = 'learning_logs'
urlpatterns = [
    #Home Page
    path('',views.index, name='index'),
    #Page that shows all topics
    path('topics/',views.topics, name='topics'),
    path('topics/<int:topic_id>/',views.topic, name='topic'),#Detail page for a single topic
    #Page for adding a new Topic
    path('new_topic/', views.new_topic, name='new_topic'),
    #Page for adding a new entry
    path('new_entry/<int:topic_id>/',views.new_entry,name='new_entry'),
    #Page for editing an entry.
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]
