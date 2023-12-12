from django.test import TestCase
from .models import Offer,Blog_article,Order,Cart,Ticket
from django.urls import reverse 
from accounts.models import Shopper

# Create your tests here.
class OfferModelTest(TestCase):
    def setUp(self):
        self.offer=Offer.objects.create(name='test',slug='test',price=10.0,stock=10,description='test',sales_number=0)
        
    def test_offer_model_fields(self):
        self.assertEqual(self.offer.name,'test')
        self.assertEqual(self.offer.slug,'test')   
        self.assertEqual(self.offer.price,10.0)
        self.assertEqual(self.offer.stock,10)
        self.assertEqual(self.offer.description,'test')
        self.assertEqual(self.offer.sales_number,0)
        
    def test_offer_get_absolute_url(self):
        expected_url=reverse('offers')
        self.assertEqual(self.offer.get_absolute_url(),expected_url)
        
        
class BlogArticleTest(TestCase):
    def setUp(self):
        self.article=Blog_article.objects.create(title='test',description='test')
        
    def test_blog_article_model_fields(self):
        self.assertEqual(self.article.title,'test')
        self.assertEqual(self.article.description,'test')
        
class OrderTest(TestCase):
    def setUp(self):
        self.offer=Offer.objects.create(name='test',slug='test',price=10.0,stock=10,description='test',sales_number=0)
        self.user=Shopper.objects.create_user(username='testUser',password='Password1234',email='test@exmple.fr',)
        self.order=Order.objects.create(user=self.user,offer=self.offer,quantity=1)
        
    def test_order_model_fields(self):
        self.assertEqual(self.order.user,self.user)
        self.assertEqual(self.order.offer,self.offer)
        self.assertEqual(self.order.quantity,1)
        self.assertFalse(self.order.ordered)
        

class CartTest(TestCase):
    def setUp(self):
       
        self.user=Shopper.objects.create_user(username='testUser',password='Password1234',email='test@example.fr',)
        self.cart=Cart.objects.create(user=self.user)
        
    def test_cart_model_fields(self):
        self.assertEqual(self.cart.user,self.user)
       
class TicketTest(TestCase):
    def setUp(self):
        self.user=Shopper.objects.create_user(username='testUser',password='Password1234',email='test@example.fr',)
        self.ticket=Ticket.objects.create(user=self.user)
    
    def test_ticket_model_fields(self):
        self.assertEqual(self.ticket.user,self.user)
        
class IndexViewTest(TestCase):
    
        
    def test_index_view(self):
        response=self.client.get(reverse('index'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'store/index.html')
        
class OffersViewTest(TestCase):
    def setUp(self):
        self.offer=Offer.objects.create(name='test',slug='test',price=10.0,stock=10,description='test',sales_number=0)
        
    def test_offers_view(self):
        response=self.client.get(reverse('offers'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'store/offers.html')
        self.assertIn('offers',response.context)
        
class CheckoutViewTest(TestCase):
    def setUp(self):
        self.user=Shopper.objects.create_user(username='testUser',password='Password1234',email='test@example.fr',)
        self.offer=Offer.objects.create(name='test',slug='test',price=10.0,stock=10,description='test',sales_number=0)
        self.order=Order.objects.create(user=self.user,offer=self.offer,quantity=1)
        self.cart=Cart.objects.create(user=self.user)
        
        self.ticket=Ticket.objects.create(user=self.user)
        
    def test_checkout_view(self):
        self.client.login(username='test@example.fr',password='Password1234')
        
        response=self.client.get(reverse('checkout'))
        
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'store/checkout.html')
        self.assertTrue(Ticket.objects.filter(user=self.user).exists())
        self.assertTrue(Order.objects.filter(user=self.user).exists())
        self.assertFalse(Cart.objects.filter(user=self.user).exists())
        
        
class DeleteCartViewTest(TestCase):
    def setUp(self):
        self.user=Shopper.objects.create_user(username='testUser',password='Password1234',email='test@example.fr',)
        self.cart=Cart.objects.create(user=self.user)
        
    def test_delete_cart_view(self):
        self.client.login(username='test@example.fr', password='Password1234')
        response=self.client.get(reverse('delete-cart'))
        self.assertFalse(Cart.objects.filter(user=self.user).exists())
        
class OrdersPaidViewTest(TestCase):
    def setUp(self):
        self.user=Shopper.objects.create_user(username='testUser',password='Password1234',email='test@example.fr',)
        self.ticket=Ticket.objects.create(user=self.user)

    def test_orders_paid_view(self):
        self.client.login(username='test@example.fr',password='Password1234')
        response=self.client.get(reverse('orders-paid'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'store/orders_paid.html')
        self.assertTrue(Ticket.objects.filter(user=self.user).exists())