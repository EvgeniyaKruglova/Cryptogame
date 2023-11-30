from django.contrib.auth.admin import User
from django.db import models
from django.utils import timezone
from django_celery_beat.models import PeriodicTask

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    email = models.EmailField(max_length=300, unique=True)
    profile_pic = models.ImageField(default='default.jpg', upload_to="media/images/profile/")
    twitter_username = models.CharField(max_length=64,blank=True, null=True)
    level = models.IntegerField(default=1)
    Twitter = models.URLField(blank=True, null=True)
    Discord = models.URLField(blank=True, null=True)
    Telegram = models.URLField(blank=True, null=True)
    Binance = models.CharField(max_length=64,blank=True, null=True)
    metaMask = models.CharField(max_length=64,blank=True, null=True)
    TrustWallet = models.CharField(max_length=64,blank=True, null=True)
    Phantom = models.CharField(max_length=64,blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} '

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class Award(models.Model):
    nft = models.FileField(null=True, blank=True,upload_to="media/award/")
    token_award = models.FileField(null=True, blank=True,upload_to="media/token_awards/")
    experience = models.IntegerField(null=True, blank=True)



# class Creator(models.Model):
#     creator = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return str(self.creator)



class TaskCard(models.Model):
    title = models.CharField(max_length=64,null=True)
    definition = models.TextField(null=True, blank=False)
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
    CATEGORY= [
        ('LK', 'Поставить лайк'),
        ('QR', 'Поиск соответствия')
    ]
    category = models.CharField(max_length=300, choices=CATEGORY, default='LK')
    type = models.CharField(max_length=300, choices=TYPE, default='ON')
    # start_time = models.OneToOneField(
    #     PeriodicTask,
    #     to_field='start_time',
    #     verbose_name='Начало события',
    #     related_name = 'begining_time',
    #     on_delete=models.PROTECT)
    start= models.DateTimeField( default=timezone.now,null= True, verbose_name= "start_date")
    last_date = models.DateTimeField( default=timezone.now)
    taskpic = models.ImageField(null=True, upload_to="media/images/tasks/")
    website = models.URLField(max_length=250, null= True, blank= True)
    award = models.ForeignKey(Award, on_delete=models.CASCADE)
    creator = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    published = models.DateTimeField(auto_now_add=True,null=True)
    STATUS = [
        ('ED', 'Ежедневные'),
        ('EW', 'Еженедельные'),
        ('EM', 'Ежемесячные'),
        ('ONE', 'Один раз'),
    ]
    status = models.CharField(max_length=300, choices=STATUS, default='ED')
    SOCIAL_NETWORK = [
        ('TW','Twitter'),
        ('TG','Telegram'),
        ('DC','Discord'),
    ]
    social_network = models.CharField(max_length=300, choices=SOCIAL_NETWORK, default='TW')
    PROGRESS = [
        ('AC', 'Аctive'),
        ('CM', 'Completed'),

    ]
    progress = models.CharField(max_length=300, choices=PROGRESS, default='AC')

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
    name = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='default.jpg', upload_to="media/images/profile_partner/")
    email = models.EmailField(max_length=300, unique=True)
    short_description = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f'{self.name} '


class StudyCard(models.Model):
    author = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    text = models.TextField()
    file = models.FileField(upload_to='files/study/', null=True, blank=True)
    study_pic = models.ImageField(null=True, upload_to="media/images/study/")

    def preview(self):
        return self.text[0:123] + '...'

