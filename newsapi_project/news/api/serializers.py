from rest_framework import serializers
from news.models import Article
from datetime import datetime
from django.utils. timesince import timesince

# Using a Serializer
# class ArticleSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     author = serializers.CharField()
#     title = serializers.CharField()
#     description = serializers.CharField()
#     body = serializers.CharField()
#     location = serializers.CharField()
#     publication_date = serializers.DateField()
#     active = serializers.BooleanField()
#     created_at = serializers.DateTimeField(read_only=True)
#     updated_at = serializers.DateTimeField(read_only=True)
#
#     def create(self, validated_data):
#         print(validated_data)
#         return Article.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.author = validated_data.get('author', instance.author)
#         instance.title = validated_data.get('title', instance.title)
#         instance.description = validated_data.get('description', instance.description)
#         instance.body = validated_data.get('body', instance.body)
#         instance.location = validated_data.get('location', instance.location)
#         instance.publication_date = validated_data.get('publication_date', instance.publication_date)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
#
#     # Custom validator (object-level, which give access to multiple fields in object)
#     def validate(self, data):
#         """ check that description and title are different """
#         if data['title'] == data['description']:
#             raise serializers.ValidationError('Title and description must be different.')
#         else:
#             return data
#
#     # Custom validator for title
#     def validate_title(self, value):
#         """ check that length of title is at least 10 characters long"""
#         if len(value) < 10:
#             raise serializers.ValidationError('The title must be at least 10 characters long')
#         else:
#             return value


# Using a ModelSerializer
class ArticleSerializer(serializers.ModelSerializer):

    # Add a new field. Gives the user access to this new field, but doesn't add it to the database.
    time_since_publication = serializers.SerializerMethodField()

    class Meta:
        model = Article
        # fields = '__all__' # serialize all fields
        # fields = ('title', 'desciption', 'body') # serialize only these fields
        exclude = ('id',) # serialize all fields except the id field

    def get_time_since_publication(self, article):
        publication_date = article.publication_date
        now = datetime.now()
        time_delta = timesince(publication_date, now)
        return time_delta

    # Same as validator in ArticleSerializer using just Serializer
    def validate(self, data):
        """ check that description and title are different """
        if data['title'] == data['description']:
            raise serializers.ValidationError('Title and description must be different.')
        else:
            return data

    # Same as validator in ArticleSerializer using just Serializer
    def validate_title(self, value):
        """ check that length of title is at least 10 characters long"""
        if len(value) < 10:
            raise serializers.ValidationError('The title must be at least 10 characters long')
        else:
            return value
