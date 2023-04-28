
from django.urls import path
from .views import ( MemberSignupView, CreatorSignupView,StaffSignupView,CustomAuthToken,LogoutView,CreatorOnlyView,StaffOnlyView)
# from django.urls import path


urlpatterns = [
    path('signup/member/', MemberSignupView.as_view()),
    path('signup/creator/', CreatorSignupView.as_view()),
    path('signup/staff/', StaffSignupView.as_view()),
    path('login/',CustomAuthToken.as_view(), name='auth-token'),
    path('logout/', LogoutView.as_view(), name='logout-view'),



    path('freelance/dashboard/', CreatorOnlyView.as_view(), name='freelance-dashboard'),
    path('client/dashboard/', StaffOnlyView.as_view(), name='client-dashboard'),
    
]