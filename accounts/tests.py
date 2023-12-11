from django.test import TestCase
from accounts.models import Shopper,CustomUserManager
from django.contrib.auth import get_user_model

# Create your tests here.
class CustomUserManagerTest(TestCase):
    def setUp(self):
        self.user_manager=get_user_model().objects
        
    def test_create_user(self):
        email='test@example.com'
        password='TestPassword1234'
        user=self.user_manager.create_user(email=email,password=password)
        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertTrue(user.is_active)
       
    def test_create_user_invalid_email(self):
        with self.assertRaises(ValueError):
            self.user_manager.create_user(email='',password='TestPassword1234')