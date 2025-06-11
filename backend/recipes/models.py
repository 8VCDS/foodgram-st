from django.db import models
from django.conf import settings

class Ingredient(models.Model):
    name = models.CharField(max_length=200, unique=True)
    measurement_unit = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name} ({self.measurement_unit})'


class Recipe(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='recipes'
    )
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='recipes/images/')
    description = models.TextField()
    ingredients = models.ManyToManyField(
        Ingredient,
        through='RecipeIngredient',
        related_name='recipes'
    )
    cooking_time = models.PositiveIntegerField()  # в минутах

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.FloatField()

    class Meta:
        unique_together = ('recipe', 'ingredient')

    def __str__(self):
        return f'{self.amount} {self.ingredient.measurement_unit} {self.ingredient.name} в {self.recipe.name}'