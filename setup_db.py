import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ca298exam.settings')
django.setup()

from examapp.models import Genre, Platform

genres_list = [
    "Action",
    "Adventure",
    "Shooter"
]

for genre in genres_list:
    existing_genre = genre.objects.filter(genre=genre).first()
    if not existing_genre:
        new_genre = genre(genre=genre)
        new_genre.save()
        print(f"genre {genre} added successfully.")
    else:
        print(f"genre {genre} already exists.")
