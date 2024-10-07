from django.db import models

# Create your models here.

class Customer_Details(models.Model):
    Customer_Id=models.IntegerField(primary_key=True)
    Customer_Name=models.CharField(max_length=40)
    Customer_Address=models.TextField()
    def __str__(self):
        return self.Customer_Name
    
class Product_Details(models.Model):
    Product_Id=models.IntegerField(primary_key=True)
    Customer_Id=models.ForeignKey(Customer_Details,on_delete=models.CASCADE)
    Product_Name=models.CharField(max_length=200)

    def __str__(self):
        return self.Product_Name
    
    
