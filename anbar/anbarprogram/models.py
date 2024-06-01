from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Brands(models.Model):
    photo = models.ImageField(upload_to='brand_photos/', blank=True, null=True)
    user_id = models.IntegerField()
    brand = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    

class Clients(models.Model):
    photo = models.ImageField(upload_to='client_photos/', blank=True, null=True)
    user_id = models.IntegerField()
    name = models.CharField(max_length=15)
    surname = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    telephone = models.CharField(max_length=20)
    company = models.CharField(max_length=40)
    

class Departments(models.Model):
    user_id = models.IntegerField()
    department = models.CharField(max_length=20)


class Expense(models.Model):
    user_id = models.IntegerField()
    appointment = models.CharField(max_length=14)
    amount = models.CharField(max_length=15)



class Permissions(models.Model):
    name = models.CharField(max_length=20)
    url = models.CharField(max_length=20)

class Perms(models.Model):
    user_id = models.IntegerField()
    item_id = models.ForeignKey(Permissions, on_delete=models.CASCADE, related_name='permissions')
    item_value = models.BooleanField(default=0)




class Positions(models.Model):
    user_id = models.IntegerField()
    department_id = models.ForeignKey(Departments, on_delete=models.CASCADE, related_name='departments')
    positions = models.CharField(max_length=30)



class Staff(models.Model):
    user_id = models.IntegerField()
    position_id = models.ForeignKey(Positions, on_delete=models.CASCADE, related_name='position')
    photo = models.ImageField(upload_to='staff_photos/', blank=True, null=True)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    telephone = models.CharField(max_length=35)
    salary = models.CharField(max_length=15)
    work = models.DateField()


class Planner(models.Model):
    user_id = models.IntegerField()
    task = models.CharField(max_length=40)
    dtask = models.DateField()
    ttask = models.TimeField()
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='staff')
    accept = models.IntegerField()

    @property
    def remaining_time(self):
        now = timezone.now()
        deadline = datetime.datetime.combine(self.dtask, self.ttask)
        deadline = timezone.make_aware(deadline)  # Делаем deadline осведомленным

        if now >= deadline:
            return 'There is no time left'

        time_difference = deadline - now

        if time_difference.days > 0:
            return f'{time_difference.days} days'
        elif time_difference.seconds >= 3600:
            hours, remainder = divmod(time_difference.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            return f'{hours} hours {minutes} minutes {seconds} seconds'
        elif time_difference.seconds >= 60:
            minutes, seconds = divmod(time_difference.seconds, 60)
            return f'{minutes} minutes {seconds} seconds'
        else:
            return f'{time_difference.seconds} seconds'

class Suppliers(models.Model):
    photo = models.ImageField(upload_to='supplier_photos/', blank=True, null=True)
    user_id = models.IntegerField()
    firm = models.CharField(max_length=25)
    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)
    email = models.CharField(max_length=50)
    telephone = models.CharField(max_length=35)
    address = models.CharField(max_length=50)

class Products(models.Model):
    supplier_id = models.ForeignKey(Suppliers, on_delete=models.CASCADE, related_name='supplier')
    user_id = models.IntegerField()
    brand_id = models.ForeignKey(Brands, on_delete=models.CASCADE, related_name='products')
    photo = models.ImageField(upload_to='product_photos/', blank=True, null=True)
    name = models.CharField(max_length=25)
    purchase = models.FloatField(max_length=20)
    sale = models.FloatField(max_length=20)
    quantity = models.IntegerField()

    @property
    def qazanc(self):
        netice = (self.sale - self.purchase) * self.quantity
        return netice
    



class Orders(models.Model):
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='products')
    user_id = models.IntegerField()
    client_id = models.ForeignKey(Clients, on_delete=models.CASCADE, related_name='clients')
    quantity = models.PositiveIntegerField()
    accept = models.IntegerField()




class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15, blank=True, null=True)
    photo = models.ImageField(upload_to='user_photos/', blank=True, null=True)
    is_blocked = models.BooleanField(default=False)
    
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_user_groups",
        blank=True,
        verbose_name="Groups",
        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
    )
    
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_user_permissions",
        blank=True,
        verbose_name="User permissions",
        help_text="Specific permissions for this user.",
        related_query_name="custom_user_permissions",
    )

    def __str__(self):
        return self.username

class Settings(models.Model):
    photo = models.ImageField(upload_to='settings_photos/', blank=True, null=True)
    title = models.CharField(max_length=100)
    footer = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    address = models.CharField(max_length=50)

class Messages(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    message = models.TextField()
    accept = models.BooleanField()

class Chat(models.Model):
    send = models.ForeignKey(CustomUser,related_name='sent_messages', on_delete=models.CASCADE)
    receive = models.ForeignKey(CustomUser,related_name='received_messages', on_delete=models.CASCADE)
    message = models.TextField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)