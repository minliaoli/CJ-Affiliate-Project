from rest_framework import routers
from .api import OffersViewset#, ProductsViewset
from . import views

router = routers.DefaultRouter()
router.register('api/offers', OffersViewset, 'offers') 
#router.register('api/products', ProductsViewset, 'products')

urlpatterns = router.urls