from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200)
    pubdate = models.DateTimeField()
    image = models.ImageField(upload_to='images/blog/')
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:200]

    def pubdate_pretty(self):
        return self.pubdate.strftime('%b %e %Y') #https://strftime.org/
# Create a blog models
# Title
#Publication Date
#body
#image

#Add the blog app to the settings

#Create a migrations

#migrate

#add to the Admin
