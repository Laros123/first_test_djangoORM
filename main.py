import django_setup

from lesson_add.models import Genre, Game

# Genre(name='2D').save()
genre = Genre.objects.get(id=3)
genre2 = Genre.objects.get(id=2)

game = Game(name='Stardev Programming', year_of_release='2019-02-01', rating=9.0898)
game.save()
game.genres.set([genre, genre2])


