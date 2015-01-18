from django.contrib.gis.db import models

ANIMAL_CHOICES = (
	('DEER','Deer'),
	('RACC','Raccoon'),
	('RAB','Rabbit'),
	('SCAT','Scat')
)

# Create your models here.
#create separate model for each animal type?
class Animal(models.Model):
	
	animal_type = models.CharField(max_length=12,choices=ANIMAL_CHOICES)
	num_animal = models.SmallIntegerField(default=1)
	submission_date = models.DateTimeField(auto_now_add=True)
	sighting_date = models.DateTimeField()
	additional_info = models.TextField(null=True,blank=True,max_length=300)

	#geodjango fields
	points = models.PointField()
	objects = models.GeoManager()

	#return string representation of model
	def __unicode__(self):
		return self.animal_type# Create your models here.
