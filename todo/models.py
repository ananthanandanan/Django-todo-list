from django.db import models

# Create your models here.

class Todo(models.Model):
    
    """Model definition for Todo."""
    add_date = models.DateTimeField()
    text = models.CharField(max_length=150)
    

    # TODO: Define fields here

    class Meta:
        """Meta definition for Todo."""

        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'

    def __str__(self):
        """Unicode representation of Todo."""
        return self.text
