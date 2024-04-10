from django.db import models
import string
import random
def generate_unique_code():
    length = 6
    while True:
        code = ''.join(random.choice(string.ascii_uppercase,k=length))
        if not Room.objects.filter(code=code).count() == 0:
            break
    return code

# Create your models here.


class Room(models.Model):
    code = models.CharField(max_length=100,unique=True,default="")
    host=models.CharField(max_length=50,unique=True)
    guest_can_pause=models.BooleanField(default=False,null=False)
    votes_to_skip=models.IntegerField(default=1,null=False)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.code
    
    