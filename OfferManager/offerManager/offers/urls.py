from rest_framework import routers
from .api import OffersViewset

router = routers.DefaultRouter()
router.register('api/offers', OffersViewset, 'offers') 

urlpatterns = router.urls