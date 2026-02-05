from django.contrib import messages
from .models import Warga, PengajuanSurat, ProfilDesa, UMKM
from .forms import WargaForm, SuratForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required


from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    # hanya perangkat desa
    return render(request,"dashboard.html",{
        "warga": Warga.objects.count(),
        "surat": PengajuanSurat.objects.count(),
        "pending": PengajuanSurat.objects.filter(status="diajukan").count()
    })

@login_required
def warga_edit(request, id):
    warga = get_object_or_404(Warga, id=id)
    form = WargaForm(request.POST or None, instance=warga)
    if form.is_valid():
        form.save()
        messages.success(request, f"Data warga {warga.nama} berhasil diperbarui.")
        return redirect("warga_list")
    return render(request, "warga_form.html", {"form": form, "warga": warga})

@login_required
def warga_list(request):
    data = Warga.objects.all()
    return render(request,"warga.html",{"data":data})

def warga_add(request):
    form = WargaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request,"warga_form.html",{"form":form})

def profil(request):
    return render(request,"profil.html",{
        "desa": ProfilDesa.objects.first(),
        "umkm": UMKM.objects.all()
    })

def ajukan_surat(request):
    form = SuratForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save()
        from django.contrib import messages
        messages.success(request, f"Pengajuan berhasil. Kode: {obj.kode}")
    return render(request,"surat.html",{"form":form})

def surat_status(request):
    data = PengajuanSurat.objects.all().order_by('-dibuat')
    return render(request,"surat_status.html",{"data":data})

def ajukan_surat(request):
    form = SuratForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save()
        messages.success(request, f"Pengajuan berhasil. Kode: {obj.kode}")
    return render(request,"surat.html",{"form":form})

def tracking(request):
    data = None
    kode = request.GET.get("kode")
    if kode:
        data = PengajuanSurat.objects.filter(kode=kode).first()
    return render(request,"tracking.html",{"data":data})

@login_required
def surat_admin(request):
    status_filter = request.GET.get("status")
    if status_filter:
        data = PengajuanSurat.objects.filter(status=status_filter).order_by("-dibuat")
    else:
        data = PengajuanSurat.objects.all().order_by("-dibuat")
    
    return render(request, "surat_admin.html", {"data": data, "status_filter": status_filter})

@login_required
def ubah_status(request, id):
    surat = get_object_or_404(PengajuanSurat, id=id)

    if request.method == "POST":
        new_status = request.POST.get("status")
        if new_status:
            surat.status = new_status

            # Upload file surat final jika selesai
            if new_status == "selesai" and "file_surat_jadi" in request.FILES:
                surat.file_surat_jadi = request.FILES["file_surat_jadi"]

            surat.save()
            messages.success(request, f"Status surat {surat.nama} diubah ke {surat.get_status_display()}")
    return redirect("surat_admin")

