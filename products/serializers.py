from rest_framework import serializers

from products.models import Product


# Create your serializers here.

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "title", "price", "manufacturer", "expiration_date", "addition_date", "barcode", "amount", "info"]

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data['title']
        instance.price = validated_data['price']
        instance.manufacturer = validated_data['manufacturer']
        instance.expiration_date = validated_data['expiration_date']
        instance.addition_date = validated_data['addition_date']
        instance.barcode = validated_data['barcode']
        instance.amount = validated_data['amount']
        instance.info = validated_data['info']

        instance.save()
        return instance
