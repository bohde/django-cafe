from django.template import Template
from django.test import TestCase

from cafe import settings
import os
import time

class CoffeeTest(TestCase):
    def path(self, *fs):
        return os.path.join(settings.MEDIA_ROOT, *fs)

    def write(self, f, content):
        with open(self.path(f), 'w') as out:
            out.write(content)
    
    def assertFileEquals(self, f, content):
        self.assertEqual(content,
                         ''.join(open(self.path(f))))

    def test_one_file(self):
        OUT = """(function() {\n  console.log('Hello, world!');\n}).call(this);\n"""
        t = Template("""{% load coffee %}{% coffee hello.coffee %}""")
        output = t.render({})
        self.assertFileEquals(output, OUT)
        os.remove(self.path(output))
        
    def test_alter_file(self):
        self.write('test.coffee', "console.log 'test'\n")
        OUT = """(function() {\n  console.log('test');\n}).call(this);\n"""
        t = Template("""{% load coffee %}{% coffee test.coffee %}""")
        first = t.render({})
        self.assertFileEquals(first, OUT)

        time.sleep(1)
        
        self.write('test.coffee', "console.log 'test2'\n")
        OUT = """(function() {\n  console.log('test2');\n}).call(this);\n"""
        t = Template("""{% load coffee %}{% coffee test.coffee %}""")
        second = t.render({})
        self.assertFileEquals(second, OUT)

        os.remove(self.path(first))
        os.remove(self.path(second))
        os.remove(self.path('test.coffee'))

    def test_two_files(self):
        OUT = """(function() {\n  console.log('Hello, world!');\n  console.log('goodbye!');\n}).call(this);\n"""
        t = Template("""{% load coffee %}{% coffee hello.coffee goodbye.coffee %}""")
        output = t.render({})
        self.assertFileEquals(output, OUT)
        os.remove(self.path(output))
        
    
