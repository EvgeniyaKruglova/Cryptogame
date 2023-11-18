from django.contrib.auth.admin import User
from django.db import models
from django.utils import timezone
from django_celery_beat.models import PeriodicTask

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    email = models.EmailField(max_length=300, unique=True)
    profile_pic = models.ImageField(default='default.jpg', upload_to="media/images/profile/")

    def __str__(self):
        return f'{self.user.username} '

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class Award(models.Model):
    nft = models.FileField(upload_to="media/award/")
    description = models.TextField()

class Creator(models.Model):
    creator = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.creator_user)



#     return self.name
class TaskCard(models.Model):
    # name = models.OneToOneField(
    #     PeriodicTask,
    #     to_field='name',
    #     on_delete=models.PROTECT
    # )
    card_task = models.OneToOneField(PeriodicTask,on_delete=models.CASCADE,related_name='card_task', null=True)
    LEVEL = [
        ('NW', 'Новичок'),
        ('MD', 'Срединий'),
        ('AD', 'Продвинутый')
    ]

    level = models.CharField(max_length=300, choices=LEVEL, default='NW')

    TYPE = [
        ('ON', 'Onchain'),
        ('OF', 'Ofchain')
    ]
    type = models.CharField(max_length=300, choices=TYPE, default='ON')
    # start_time = models.OneToOneField(
    #     PeriodicTask,
    #     to_field='start_time',
    #     verbose_name='Начало события',
    #     related_name = 'begining_time',
    #     on_delete=models.PROTECT)
    last_date = models.DateTimeField( default=timezone.now)
    # description = models.TextField()
    taskpic = models.ImageField(null=True, upload_to="media/images/tasks/")
    website = models.URLField(max_length=250, null= True, blank= True)
    award = models.ForeignKey(Award, on_delete=models.CASCADE)
    creator = models.ForeignKey(Creator,on_delete=models.CASCADE)
    # published = models.DateTimeField(auto_now_add=True, db_index=True)
    STATUS = [
        ('ED', 'Ежедневные'),
        ('EW', 'Еженедельные'),
        ('EM', 'Ежемесячные'),
        ('ONE', 'Один раз'),
    ]
    status = models.CharField(max_length=300, choices=STATUS, default='ED')

    # def preview(self):
    #     return self.description[0:123] + '...'
    #
    # def __str__(self):
    #     return self.name

    class Meta:
        verbose_name_plural = 'Tasks'
        verbose_name = 'Task'
        # ordering = ['start_time']



    # def __str__(self):
    #     return f'{self.title}'
    #
    # def preview(self):
    #     return self.description[0:123] + '...'


class Partner(models.Model):
    name = models.CharField(max_length=64)
    profile_pic = models.ImageField(default='default.jpg', upload_to="media/images/profile_partner/")
    task = models.ForeignKey(TaskCard, related_name='task', on_delete=models.CASCADE)
    email = models.EmailField(max_length=300, unique=True)

    def __str__(self):
        return f'{self.name} '


class StudyCard(models.Model):
    author = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    text = models.TextField()
    file = models.FileField(upload_to='files/study/', null=True, blank=True)
    study_pic = models.ImageField(null=True, upload_to="media/images/study/")

    def preview(self):
        return self.text[0:123] + '...'
