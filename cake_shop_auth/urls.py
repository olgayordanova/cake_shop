from django.urls import path

from cake_shop_auth import views

urlpatterns = (
    path('sign-up/', views.SignUpView.as_view(), name='sign up'),
    path('sign-in/', views.SignInView.as_view(), name='sign in'),
    path('sign-out/', views.sign_out, name='sign out'),
)
# path('sign-up/', views.sign_up, name='sign up'),
# path('sign-in/', views.sign_in, name='sign in'),