from rest_framework import serializers
from .models import Book, Author

class BookNamesSerializer(serializers.Serializer):

    book_id = serializers.IntegerField(read_only=True)
    book_name = serializers.CharField(max_length=120, source='name')
    price = serializers.FloatField()
    available_amount = serializers.IntegerField()
    author = serializers.CharField(source='author.full_name')

    def create(self, validated_data):
        author_name = validated_data.pop('author')  # Извлекаем имя автора из данных
        first_name, last_name = Author.objects.get_or_create(full_name=author_name)  # Получаем или создаем автора по его имени
        validated_data['first_name'] = author
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.book_name = validated_data.get('book_name', instance.book_name)
        instance.price = validated_data.get('price', instance.price)
        instance.available_amount = validated_data.get('available_amount', instance.available_amount)
        instance.author_name = validated_data.get('author_name', instance.author_name)
        instance.save()
        return instance

    def to_representation(self, instance: Book):
        return {
            "book_id": instance.id,
            "book_name": instance.name,
            "price": instance.price,
            "available_amount": instance.available_amount,
            "author_name": instance.author.full_name,
        }
    