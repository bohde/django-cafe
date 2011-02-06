from django.template import Template
from django.test import TestCase

class CoffeeTest(TestCase):

    def test_one_file(self):
        t = Template("""{% load cafe %}{% coffee "hello.coffee" %}""")
        output = t.render({})
        self.assertEqual(output, "hello.js")
