from django.urls import path, include
from classroom_management.api.views import *
from classroom_management.api.views import RolePOSTSV

from django.urls import path, include
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('staff/modify', StaffCSV, basename='staffmodify')
router.register('staff', StaffSV, basename='staff')

router.register('classroom', ClassroomsSV, basename='classroom')
router.register('sessions', SessionsSV, basename='sessions')

router.register('request/modify', RequestsCSV, basename='requestmodify')
router.register('request', RequestsSV, basename='request')

router.register('activitytype', ActivityTypeSV, basename='activitype')
router.register('permission', PermissionSV, basename='permission')
router.register('subject', SubjectSV, basename='subject')
router.register('role', RolePOSTSV, basename='role')


urlpatterns = [
    path('', ApiOverviewAV.as_view(), name='apiOverview'),
    path('', include(router.urls)),
    path("classroom/<int:pk>/request",
         ClassroomRequests.as_view(), name='review-list'),
    path("analytics/", Analytics.as_view(), name='Analytics'),
    path("mostreq/", MostRequested.as_view(), name='mostreq'),

]
