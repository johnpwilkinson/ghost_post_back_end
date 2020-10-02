from rest_framework import serializers
from back_end.models import Posts

class PostSerializer(serializers.ModelSerializer):
    # manufacturer = serializers.StringRelatedField()
    # color = serializers.StringRelatedField()
    # shoe_type = serializers.StringRelatedField()

    class Meta:
        model= Posts
        fields = [
            'id',
            'post_content',
            'boast_or_roast',
            'submission_time',
            'votes'
        ]