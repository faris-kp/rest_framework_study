from rest_framework import serializers
from rest_framework.reverse import reverse
from product.models import Product
from . import validators



class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field = 'pk' 
        )
    title = serializers.CharField(validators = [validators.validate_title_no_hello,validators.unique_product_title])
    # name = serializers.CharField(source = 'title',read_only = True)
    
    # email = serializers.EmailField(write_only = True)
    class Meta:
        model = Product
        fields = [
            # 'user',
            'url',
            'edit_url',
            'pk',
            # 'name',
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',
        ]
    
    def  validate_title(self, value):
        request = self.context.get('request')
        user = request.user
        qs = Product.objects.filter(user=user ,title__iexact = value)
        if qs.exists():
            raise serializers.ValidationError(f"{value} is already a product name")
        return value
    # def create(self, validated_data):
    #     email  = validated_data.pop('email')
    #     obj = super().create(validated_data)
    #     print(email, obj)
    #     return obj 
    
    # def update(self, instance, validated_data):
    #     email = validated_data.pop('email')
    #     instance.title = validated_data.pop('title')
    #     return super().update(instance,validated_data)
    
    def get_edit_url(self,obj):
        
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-edit",kwargs={"pk":obj.pk},request=request)
        # return f"/api/product/{obj.id}/"
    def get_my_discount(self,obj):
        if not hasattr(obj,'id'):
            return None
        if not isinstance(obj,Product):
            return None
        return obj.get_discount()