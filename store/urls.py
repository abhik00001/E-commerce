from django.urls import  path
from store import views

urlpatterns = [
    path('', views.store, name="store"),
    # path('main/', views.main, name="main"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('signup_page/', views.signup_page, name="signup_page"),
	path('login_page/', views.login_page, name="login_page"),

	path('signup', views.signup,),
	path('addItem/', views.addItem,),
	path('log/', views.log,),
	path('logout_this/', views.logout_this,),
	# path('get/<int:id>', views.get_data, name="checkout"),

]
