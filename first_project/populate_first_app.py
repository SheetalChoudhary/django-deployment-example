import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()

##Faker script:
import random
from faker import Faker
from first_app.models import AccessRecore, Topic, Webpage

fakegen = Faker()
topics = ['Search','Social','News','Game','Marketing']

def add_topic():
    t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
    t.save()
    return t

def populate(N=10):
    for entry in range(N):

        #get topic
        top = add_topic()

        #add entries for that topic
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        #Create the new webpage emtry
        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        #create the new entry for AccessRecord
        accrec = AccessRecore.objects.get_or_create(name=webpg, date=fake_date)[0]

        webpg.save()
        accrec.save()

if __name__ == '__main__':
    print('Populating data starting..')
    populate(20)
    print('Population data complted!')
