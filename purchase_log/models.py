from django.db import models
from django.db.models import Q

class PurchaseLog(models.Model):
    id = models.AutoField(primary_key=True)
    item_id = models.ForeignKey('purchase_log.Item', on_delete=models.CASCADE)  # 文字列で参照
    user_id = models.ForeignKey('purchase_log.User', on_delete=models.CASCADE)  # 文字列で参照
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    student_id = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_banned = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Item(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    unit_cost = models.IntegerField(default=0)
    is_sales = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    stock = models.IntegerField(default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['price'],
                condition=Q(is_sales=True),
                name='unique_price_when_is_sales_true'
            )
        ]

    def __str__(self):
        return self.name
