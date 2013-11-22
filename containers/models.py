from django.db import models

# Create your models here.


from django.db import models

# Create your models here.
class Container(models.Model):
      name=models.CharField(max_length=255)
      serial_Number=models.CharField(max_length=255)
      container_Status=models.CharField(max_length=255)
      location=models.CharField(max_length=255);
      last_Inspection_Date=models.DateField();
      next_Inspection_Date=models.DateField();
      date_Rented=models.DateField()
      category=models.ForeignKey("Category")
      


      def __unicode__(self):
      	 return self.name+ " " +self.serial_Number


class Category(models.Model):
	category_name=models.CharField(max_length=80)
	size=models.IntegerField()
	description=models.TextField()

	def __unicode__(self):
		return self.category_name
