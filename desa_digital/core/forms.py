from django import forms
from .models import Warga

class WargaForm(forms.ModelForm):
    class Meta:
        model = Warga
        fields = "__all__"
from .models import PengajuanSurat

class SuratForm(forms.ModelForm):
    class Meta:
        model = PengajuanSurat
        fields = ['nama', 'nik', 'jenis', 'keterangan', 'file_pendukung']

