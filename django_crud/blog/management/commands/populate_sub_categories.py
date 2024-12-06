from typing import Any
from blog.models import Subcategory, Category
from django.core.management.base import BaseCommand
import random

class Command(BaseCommand):
    help = "This command help to insert sub category data"

    def handle(self, *args: Any, **options: Any):
        
        #Delete existing data
        Subcategory.objects.all().delete()

        categories = Category.objects.all()
        subcategories = ['Cricket', 'Football','Vollyball', 'AI', 'MachineLearning', 'Programming', 'Physics', 'Chemistry', 'Sandart','Painting', 'Veg','Nonveg']

        for Subcategory_name in subcategories:
            category = random.choice(categories)
            Subcategory.objects.create(name=Subcategory_name, category=category)

        self.stdout.write(self.style.SUCCESS("Subcategories inserted successfully!"))