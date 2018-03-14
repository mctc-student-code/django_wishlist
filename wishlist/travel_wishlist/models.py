from django.db import models

# Create your models here.
# Essentially a place to store data in the database, with columns and rows
class Place(models.Model):
    name = models.CharField(max_length=200)
    visited = models.BooleanField(default=False)
    #default visited is set to false as this is a wishlist and only
    #after a place is visited will the value be true
    def __str__(self):
        return '%s visited? %s' % (self.name, self.visited)
