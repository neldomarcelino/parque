from django.test import TestCase

# Create your tests here.
from .models import Specie
from django.utils import timezone
import datetime


class SpecieModelTests(TestCase):

    def test_was_recently_published(self):
        """
        was_published_recently() return False for questions whose pub is in the future
        :return: None
        """
        time = timezone.now() + datetime.timedelta(days=1)
        specie = Specie(datacriacao=time)
        self.assertIs(specie.was_published_recently(), False, "Specie does not exist")
