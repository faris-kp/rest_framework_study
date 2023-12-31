import random
from django.db import models
from django.conf import settings
from django.db.models.query import QuerySet
from django.db.models import Q

User = settings.AUTH_USER_MODEL #auth user
TAG_MODEL_VALUES =  ['electronics','cars','boats','movies','camera']

class ProductQuerySet(models.QuerySet):
    def is_public(self):
        return self.filter(public =True)
    
    def search(self,query,user=None):
        lookup = Q(title__icontains=query) | Q(content__icontains=query)
        qs = self.is_public().filter(lookup)
        if user is not None:
            qs2 =self.filter(user=user).filter(lookup)
            qs = (qs | qs2).distinct()
        return qs
            
        
    
    
class ProductManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return ProductQuerySet(self.model,using=self._db)
    
    def search(self, query, user=None):
        return self.get_queryset().search(query,user=user)
# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User, default=1,null=True ,on_delete=models.SET_NULL)
    title = models.CharField(max_length=50)
    content = models.TextField(null=True,blank=True)
    price = models.DecimalField(max_digits=15,decimal_places=2, default=99.99)
    public = models.BooleanField(default=True )
    
    def is_public(self) -> bool:
        return self.public
    
    def get_tags_list(self):
        return [random.choice(TAG_MODEL_VALUES)]
    objects =  ProductManager()
    
    
    @property
    def sale_price(self):
        return "%.2f" %(float(self.price) * 0.8)
    
    def get_discount(self):
        return "122"
    