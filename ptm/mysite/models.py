from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth import get_user_model

CHOICES_TYPE = (
    ('Buyer', 'Buyer'),
    ('Agent', 'Agent')
)

choice1 =(('Short Commute to work','Short Commute to work'),
          ('Access to shopping','Access to shopping'),
          ('Vastu Preference','Vastu Preference'),
          ('School Requirements','School Requirements'),
           )


class profileModel(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete= models.CASCADE)
    contactNumber = models.BigIntegerField(blank = True, null=True)
    approve = models.BooleanField(default=True)
    Teacher_or_Parent = models.CharField(max_length=10, blank=True, default='Buyer' ,choices=CHOICES_TYPE)
    occupation=models.CharField(max_length=200,blank=True,null=True)
    #Property Requirements
    Price_Range=models.CharField(max_length=200,blank=True,null=True)
    has_pre_approval=models.CharField(max_length=200,blank=True,null=True)
    property_type=models.CharField(max_length=200,blank=True,null=True)
    beds=models.CharField(max_length=200,blank=True,null=True)
    bath=models.CharField(max_length=200,blank=True,null=True)
    lot_size=models.CharField(max_length=200,blank=True,null=True)
    stories=models.CharField(max_length=200,blank=True,null=True)
    location_preference=models.CharField(max_length=200,blank=True,null=True)
    looking_to_buy_in_how_many_months=models.CharField(max_length=200,blank=True,null=True)
    How_long_have_you_been_house_hunting=models.CharField(max_length=200,blank=True,null=True)
    Life_style = models.CharField(max_length=200,blank=True,null=True,choices=choice1)
    any_other = models.CharField(max_length=200,blank=True,null=True)
    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)


