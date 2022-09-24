from pyexpat import model
from django.db import models

class poll(models.Model):
    #here we define the fields for the model of the poll app
    question = models.CharField(max_length=100) #this is the question of the poll
    #this is the options to answer the poll
    option_one = models.CharField(max_length=50)
    option_two = models.CharField(max_length=50)
    option_three = models.CharField(max_length=50)
    #here we define the fields that count the votes for each option
    option_one_count = models.IntegerField(default=0)
    option_two_count = models.IntegerField(default=0)
    option_three_count = models.IntegerField(default=0)


    def __str__(self):
        return self.question
