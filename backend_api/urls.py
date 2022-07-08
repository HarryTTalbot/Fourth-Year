""" URL patterns for the backend API. """

from django.conf import settings
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework import routers

from .views import delete_expired

from backend_api.api_views.attendance.views import LessonViewSet, LongTermAbsenceViewSet
from backend_api.api_views.classes.views import ClassViewSet
from backend_api.api_views.inventory.views import BulkItemViewSet, WorksheetViewSet, LendableItemViewSet, ItemLoanViewSet
from backend_api.api_views.staff.views import StaffViewSet
from backend_api.api_views.students.views import StudentViewSet, ContactViewSet
from backend_api.api_views.subjects.views import SubjectViewSet
from backend_api.api_views.data_import.views import ImportViewSet, ExportViewSet
from backend_api.api_views.reporting.views import RecordSheetViewSet
from backend_api.api_views.authentication.views import UserViewSet
from backend_api.api_views.centre_details.views import CenterDetailsViewSet

#from .authentication import views as AuthenticationViews

# Router maps viewsets to urls
router = routers.DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'classes', ClassViewSet)
router.register(r'contacts', ContactViewSet)
router.register(r'staff', StaffViewSet)
router.register(r'lesson', LessonViewSet)
router.register(r'long-term-absence', LongTermAbsenceViewSet)
router.register(r'subject', SubjectViewSet)
router.register(r'bulk-item', BulkItemViewSet)
router.register(r'worksheet', WorksheetViewSet)
router.register(r'lendable-item', LendableItemViewSet)
router.register(r'item-loan', ItemLoanViewSet)
router.register(r'export', ExportViewSet, basename='export')
router.register(r'import', ImportViewSet, basename='import')
router.register(r'record-sheet', RecordSheetViewSet,
                basename='record-sheet')
router.register(r'authentication', UserViewSet,
                basename='authentication')
router.register(r'center-details', CenterDetailsViewSet,
                basename='center-details')

urlpatterns = [
    path('', include(router.urls)),
    path('delete_expired', delete_expired, name='deleted_expired')
]

#urlpatterns += [path('authenticate', AuthenticationViews.is_logged_in_view)]

if settings.DEBUG:
    urlpatterns += [  # OpenAPI Schema
        path('openapi/', SpectacularAPIView.as_view(), name='openapi-schema'),

        # Swagger View for API Schema
        path('swagger-ui/', SpectacularSwaggerView.as_view(
            url_name='openapi-schema'
        ), name='swagger-ui'),

        # Redoc View for API Schema
        path('redoc/', SpectacularRedocView.as_view(
            url_name='openapi-schema'
        ), name='redoc'),
    ]

# Use Django REST Framework's views for HTTP 400/500
handler400 = 'rest_framework.exceptions.bad_request'
handler500 = 'rest_framework.exceptions.server_error'
