# Create your models here.
from django.db import models
from django.urls import reverse

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

# model 3
class Toy(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('toy-detail', kwargs={'pk': self.id})
    
# model1
class Cat(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    
    # this when you try it in the shell it will only show the name
    def __str__(self):
        return self.name
    
    # Define a method to get the URL for this particular cat instance
    def get_absolute_url(self):
        # Use the 'reverse' function to dynamically find the URL for viewing this cat's details
        return reverse('cat-detail', kwargs={'cat_id': self.id})
    
    
# model 2
class Feeding(models.Model):
    date = models.DateField('Feeding date') #this will just change the lable
    meal = models.CharField(
        max_length=1,
        # add the 'choices' field option
        choices=MEALS,
        # set the default value for meal to be 'B'
        default=MEALS[0][0]
    )
    
    # Create a cat_id column for each feeding in the database
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)
    
    def __str__(self):
        # Nice method for obtaining the friendly value of a Field.choice, the get disply insted of B it shows breakfast
        return f"{self.get_meal_display()} on {self.date}"
    
    # Define the default order of feedings
    class Meta:
        ordering = ['-date']  # This line makes the newest feedings appear first

