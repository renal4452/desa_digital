from django.urls import path
from . import views

urlpatterns = [
    # Dashboard
    path('', views.dashboard, name="dashboard"),

    # Data warga
    path('warga/', views.warga_list, name="warga_list"),
    path('warga/add/', views.warga_add, name="warga_add"),
    path('warga/edit/<int:id>/', views.warga_edit, name="warga_edit"),

    # Portal Surat
    path('surat/', views.ajukan_surat, name="ajukan_surat"),
    path('surat/status/', views.surat_status, name="surat_status"),

    # Tracking pengajuan surat publik
    path('tracking/', views.tracking, name="tracking"),

    # Profil desa
    path('profil/', views.profil, name="profil"),

    # Admin Surat
    path('admin-surat/', views.surat_admin, name="surat_admin"),
    path('admin-surat/ubah/<int:id>/', views.ubah_status, name="ubah_status"),
]
