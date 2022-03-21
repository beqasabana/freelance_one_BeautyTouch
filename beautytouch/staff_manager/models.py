from django.db import models
from django.core.exceptions import ObjectDoesNotExist
import bcrypt


# Create your models here.

class EmployeeManager(models.Manager):
    def validate_login(self, user_input):
        try:
            emp = Employee.objects.get(user_name=user_input['user_name'])
        except ObjectDoesNotExist:
            return 0
            #user does not exist
        if bcrypt.checkpw(user_input['password'].encode(), emp.password.encode()):
            return emp
        else:
            # password did not match
            return 0

class Employee(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=35)
    user_name = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    manager = models.BooleanField(default=False)
    objects = EmployeeManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"First Name: {self.first_name}\nLast Name: {self.last_name}\nUser Name: {self.user_name}\nEmail: {self.email}\nPassword: {self.password}\nManager: {self.manager}"

    def user_name_generator(self):
        self.user_name = f"{self.first_name}_{self.last_name}"

    def make_manager(self):
        self.manager = True
        self.objects.save()