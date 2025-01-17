from django.db import models

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

    def __str__(self):
        return self.name

class Item(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    is_sales = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.name