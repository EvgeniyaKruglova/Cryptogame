from rest_framework import serializers
from .models import Award, Creator,TaskCard


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
        fields = ['id','creator','name','description','award','level', 'category', 'type','start_date','last_date','website', 'status','progress']
