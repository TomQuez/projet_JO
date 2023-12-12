from django.test import TestCase
from accounts.models import Shopper,CustomUserManager
from django.contrib.auth import get_user_model,authenticate
from store.models import Ticket
from django.urls import reverse
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
            
            
class ShopperTest(TestCase):
    def setUp(self):
        self.user_data={
            'email':'test@example.fr',
            'password':'TestPassword1234',
            'username':'test',
            }
        
    def test_create_user(self):
        user=Shopper.objects.create_user(**self.user_data)
        self.assertEqual(user.email,self.user_data['email'])
        self.assertTrue(user.check_password(self.user_data['password']))
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertTrue(user.is_active)
        
    def test_tickets_relation(self):
        user=Shopper.objects.create_user(**self.user_data)
        ticket=Ticket.objects.create(ticket_name='test',user=user)
        user.tickets.add(ticket)
        self.assertEqual(user.tickets.count(),1)

        
class SignupViewTest(TestCase):
    def test_signup_view(self):
        data={
            'username':'test',
            'password':'TestPassword1234',
            'firstname':'John',
            'lastname':'Doe',
            'email':'test@example.fr',
        }
        
        response=self.client.post(reverse('signup'),data)
        self.assertRedirects(response,reverse('index'))
        
        user=get_user_model().objects.get(email=data['email'])
        self.assertTrue(user.is_authenticated)
        
class LoginViewTest(TestCase):
    def setUp(self):
        self.user=get_user_model().objects.create_user(username='test',                 password='TestPassword1234',email='test@example.fr',)
        
    def test_login_view_valid_credentials(self):
        data={
            'username':'test@example.fr',
            'password':'TestPassword1234',
            
        }
        response=self.client.post(reverse('login'),data)
        self.assertRedirects(response,reverse('index'))
        user=get_user_model().objects.get(email=data['username'])
        self.assertTrue(user.is_authenticated)
    
    def test_login_view_invalid_credentials(self):
        data={
            'username':'test@example.fr',
            'password':'Wrongp',}
        response=self.client.post(reverse('login'),data)
        self.assertTemplateUsed(response,'accounts/login.html')
        self.assertContains(response,'Les informations de connexion sont incorrectes')
        user=authenticate(username=data['username'],password=data['password'])
        self.assertIsNone(user)
        
class LogoutViewTest(TestCase):
    def setUp(self):
        self.user=get_user_model().objects.create_user( username='test',                 password='TestPassword1234',
        email='test@example.fr',
        )
        
    def test_logout_view(self):
        self.client.login(username=self.user.email,password='TestPassword1234')
        response=self.client.get(reverse('logout'))
        self.assertRedirects(response,reverse('index'))
        self.assertIsNone(self.client.session.get('user'))
                                                       
                                                       
                                                                                                              
                                                       