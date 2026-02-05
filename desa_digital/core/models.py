from django.db import models
from django.contrib.auth.models import User
import uuid

class Profile(models.Model):
    ROLE = [
        ('kepala','Kepala Desa'),
        ('sekretaris','Sekretaris'),
        ('kaur','Kaur'),
    ]
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    role = models.CharField(max_length=20,choices=ROLE)

class Warga(models.Model):
    nik = models.CharField(max_length=20, unique=True)
    nama = models.CharField(max_length=100)
    alamat = models.TextField()

class PengajuanSurat(models.Model):
    JENIS = [
        ('domisili','Surat Domisili'),
        ('usaha','Surat Usaha'),
        ('tidak_mampu','Surat Tidak Mampu'),
        ('kelahiran','Surat Kelahiran'),
        ('kematian','Surat Kematian'),
    ]

    STATUS = [
        ('diajukan','Diajukan'),
        ('diproses','Diproses'),
        ('selesai','Selesai'),
        ('ditolak','Ditolak'),
    ]

    kode = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    nama = models.CharField(max_length=100)
    nik = models.CharField(max_length=20)
    jenis = models.CharField(max_length=50, choices=JENIS)
    keterangan = models.TextField(blank=True)
    file_pendukung = models.FileField(upload_to="berkas/", null=True, blank=True)
    file_surat_jadi = models.FileField(upload_to="surat_jadi/", null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS, default='diajukan')
    dibuat = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.kode:
            self.kode = str(uuid.uuid4()).split('-')[0].upper()  # contoh: '3F5A7C1B'
        super().save(*args, **kwargs)
    
class ProfilDesa(models.Model):
    nama = models.CharField(max_length=100)
    jumlah_penduduk = models.IntegerField(default=0)
    deskripsi = models.TextField(blank=True, null=True)
    lokasi = models.CharField(max_length=200, blank=True, null=True)
    potensi_wisata = models.TextField(blank=True, null=True)
    galeri_foto = models.ImageField(upload_to='desa_galeri/', blank=True, null=True)

    def __str__(self):
        return self.nama

class UMKM(models.Model):
    nama = models.CharField(max_length=100)
    kategori = models.CharField(max_length=50, blank=True, null=True)
    deskripsi = models.TextField(blank=True, null=True)
    kontak = models.CharField(max_length=50, blank=True, null=True)
    foto = models.ImageField(upload_to='umkm/', blank=True, null=True)

    def __str__(self):
        return self.nama

