from django.conf.urls import url
from codefundo import views
app_name = "codefundo"

urlpatterns = [
    #url(r'^$', views.front_page, name='front_page'),

    url(r'^main_page/', views.main_page, name='main_page'),
    url(r'^user_logout/', views.user_logout, name='user_logout'),
    url(r'^main_log_page/', views.main_log_page, name='main_log_page'),

    url(r'^admin_login/', views.admin_login, name='admin_login'),
    
    url(r'^user_login/', views.user_login, name='user_login'),
    url(r'^user_signup/', views.user_signup, name='user_signup'),
    url(r'^registered',views.registered, name='registered'),
    url(r'^aboutus',views.aboutus, name='aboutus'),
    url(r'^alreadyreg',views.alreadyreg, name='alreadyreg'),
    url(r'^afterlogsign',views.afterlogsign, name='afterlogsign'),
    url(r'^thanku',views.thanku,name='thanku')

  






   
   
   
]
