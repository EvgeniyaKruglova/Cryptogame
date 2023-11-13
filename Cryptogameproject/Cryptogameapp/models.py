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



class Partner:
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
    author = models.ForeignKey(Partner, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    text = models.TextField()
    file = models.FileField(upload_to='files/study/', null=True, blank=True)
    study_pic = models.ImageField(null=True, upload_to="images/study/")

    def preview(self):
        return self.text[0:123] + '...'


class Award(models.Model):
    nft = models.FileField(upload_to="award/")
    description = models.TextField()


class CategoryTask(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
class TaskCard(models.Model):
    name = models.CharField(max_length=64)
    category = models.ForeignKey(CategoryTask, on_delete=models.CASCADE)
    description = models.TextField()
    website = models.URLField(max_length=250)
    award = models.ForeignKey(Award, on_delete=models.CASCADE)
    creator = models.ForeignKey(Partner,on_delete=models.CASCADE, related_name='creator')
    published = models.DateTimeField(auto_now_add=True, db_index=True)


    def preview(self):
        return self.description[0:123] + '...'

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Tasks'
        verbose_name = 'Task'
        ordering= ['published']


    def __str__(self):
        return f'{self.title}'

    def preview(self):
        return self.description[0:123] + '...'

