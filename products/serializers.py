from rest_framework import serializers

from products.models import Product


# Create your serializers here.

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        product = Product.objects.create(**validated_data)
        return product

    def update(self, instance, validated_data):
        instance.title = validated_data['title']
        instance.price = validated_data['price']
        instance.manufacturer = validated_data['manufacturer']
        instance.expiration_date = validated_data['expiration_date']
        instance.barcode = validated_data['barcode']
        instance.amount = validated_data['amount']
        instance.info = validated_data['info']

        instance.save()
        return instance
