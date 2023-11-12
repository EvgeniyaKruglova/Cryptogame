from django.db import models
from django.contrib.auth.admin import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    email = models.EmailField(max_length=300, unique=True)
    profile_pic = models.ImageField(default='default.jpg', upload_to="images/profile/")

    def __str__(self):
        return f'{self.user.username} '

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)



class ProfilePartner:
    name = title = models.CharField(max_length=64)
    bio = models.TextField(null=True, blank=True)
    profile_pic = models.ImageField(default='default.jpg', upload_to="images/profile_partner/")
    inn_field = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(10)
        ]
    )

    def __str__(self):
        return f'{self.name} '


class StudyCard(models.Model):
    author = models.ForeignKey(ProfilePartner, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    text = models.TextField()
    file = models.FileField(upload_to='files/study/', null=True, blank=True)
    study_pic = models.ImageField(null=True, upload_to="images/study/")

    def preview(self):
        return self.text[0:123] + '...'


class Award(models.Model):
    nft = models.FileField(upload_to="award/")
    description = models.TextField()


class TaskCard(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    website = models.URLField(max_length=250)
    award = models.ForeignKey(Award, on_delete=models.CASCADE)
    published = models.DateTimeField(auto_now_add=True, db_index=True)
    def preview(self):
        return self.description[0:123] + '...'


    class Meta:
        verbose_name_plural = 'Tasks'
        verbose_name = 'Объявление'
        ordering= ['published']


    def __str__(self):
        return f'{self.title}'

    def preview(self):
        return self.description[0:123] + '...'

