from django.db import models

class Education(models.Model):
    title = models.CharField(max_length=100)
    from_year = models.IntegerField()
    end_year = models.IntegerField()
    description = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.title



class Experiences(models.Model):
    title = models.CharField(max_length=100)
    from_year = models.IntegerField()
    end_year = models.IntegerField()
    description = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.title


class Services(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class PersonalDetails(models.Model):
    AVAILABILITY = [
        ('available', 'Available'),
        ('not_available', 'Not Available'),
    ]

    dob = models.DateField()
    language = models.CharField(max_length=200)
    expertness = models.TextField()
    availability = models.CharField(max_length=14, choices=AVAILABILITY, default='available')
    short_description = models.TextField()

    def __str__(self):
        return self.availability


class Skills(models.Model):
    title = models.CharField(max_length=100)
    confidence = models.PositiveIntegerField()

    def __str__(self):
        return self.title


class Welcome(models.Model):
    first_name  = models.CharField(max_length=50)
    last_name  = models.CharField(max_length=50)
    image = models.ImageField(upload_to='welcome/')
    description = models.TextField()