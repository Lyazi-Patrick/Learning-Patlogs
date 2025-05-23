from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    """A topic the user is learning About."""
    text = models.CharField(max_length=200)#attr CharField is made up of characters or texts
    date_added = models.DateTimeField(auto_now_add=True)#sets date to current time 
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):#returns a string stored in the text attribute
        """Return a string representation of the model."""
        return self.text

class Entry(models.Model):
    """Something specific learned about a topic."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)#cascading delete, topic is a ForeignKey instance
    text = models.TextField()#text(attribute) is an instance of TextField
    date_added = models.DateTimeField(auto_now_add=True)#presents entries in order they were created

    class Meta:#holds information for managing the model
        verbose_name_plural = 'entries'#without this django would refer to multiple entries as Entrys
    
    def __str__(self):
        """Return a string representayion of the model."""
        return f"{self.text[:50]}..."#django will display just the first 50characters of text, ...means ellipsis

