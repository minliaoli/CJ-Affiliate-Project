from rest_framework import routers
from .api import OffersViewset
from . import views

router = routers.DefaultRouter()
router.register('api/offers', OffersViewset, 'offers') 
#router.register('/import', views.get_products, 'products')

urlpatterns = router.urls