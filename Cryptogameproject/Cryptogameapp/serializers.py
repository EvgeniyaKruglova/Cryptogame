from rest_framework import serializers
from .models import Award, Creator,TaskCard, Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id',
                  'user',
                  'bio',
                  'email',
                  'profile_pic',
                  'twitter_username',
                  'level',
                  'Twitter', 'Discord', 'Telegram',
                  'Binance', 'metaMask', 'TrustWallet','Phantom'
                  ]
class AwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Award
        fields = ['id', 'nft', 'token_award', 'experience']

class CreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creator
        fields = ['id', 'creator']
class TaskCardSerializer(serializers.ModelSerializer):
    award = AwardSerializer()
    creator = CreatorSerializer()

    class Meta:
        model = TaskCard
        fields = ['id','creator','title','definition','award','level', 'category', 'type','start','last_date','website', 'status','progress']
