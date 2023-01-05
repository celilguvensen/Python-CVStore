from django.db import models
 
 
# Create your models here.
# from phone_field import PhoneField
 
# from django.contrib.auth.models import User
 


from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

CITY_CHOICES = (
('ADANA','ADANA'),
('ADIYAMAN','ADIYAMAN'),
('AFYONKARAHİSAR','AFYONKARAHİSAR'),
('AĞRI','AĞRI'),
('AMASYA','AMASYA'),
('ANKARA','ANKARA'),
('ANTALYA','ANTALYA'),
('ARTVİN','ARTVİN'),
('AYDIN','AYDIN'),
('BALIKESİR','BALIKESİR'),
('BİLECİK','BİLECİK'),
('BİNGÖL','BİNGÖL'),
('BİTLİS','BİTLİS'),
('BOLU','BOLU'),
('BURDUR','BURDUR'),
('BURSA','BURSA'),
('ÇANAKKALE','ÇANAKKALE'),
('ÇANKIRI','ÇANKIRI'),
('ÇORUM','ÇORUM'),
('DENİZLİ','DENİZLİ'),
('DİYARBAKIR','DİYARBAKIR'),
('EDİRNE','EDİRNE'),
('ELAZIĞ','ELAZIĞ'),
('ERZİNCAN','ERZİNCAN'),
('ERZURUM','ERZURUM'),
('ESKİŞEHİR','ESKİŞEHİR'),
('GAZİANTEP','GAZİANTEP'),
('GİRESUN','GİRESUN'),
('GÜMÜŞHANE','GÜMÜŞHANE'),
('HAKKARİ','HAKKARİ'),
('HATAY','HATAY'),
('ISPARTA','ISPARTA'),
('MERSİN','MERSİN'),
('İSTANBUL','İSTANBUL'),
('İZMİR','İZMİR'),
('KARS','KARS'),
('KASTAMONU','KASTAMONU'),
('KAYSERİ','KAYSERİ'),
('KIRKLARELİ','KIRKLARELİ'),
('KIRŞEHİR','KIRŞEHİR'),
('KOCAELİ','KOCAELİ'),
('KONYA','KONYA'),
('KÜTAHYA','KÜTAHYA'),
('MALATYA','MALATYA'),
('MANİSA','MANİSA'),
('KAHRAMANMARAŞ','KAHRAMANMARAŞ'),
('MARDİN','MARDİN'),
('MUĞLA','MUĞLA'),
('MUŞ','MUŞ'),
('NEVŞEHİR','NEVŞEHİR'),
('NİĞDE','NİĞDE'),
('ORDU','ORDU'),
('RİZE','RİZE'),
('SAKARYA','SAKARYA'),
('SAMSUN','SAMSUN'),
('SİİRT','SİİRT'),
('SİNOP','SİNOP'),
('SİVAS','SİVAS'),
('TEKİRDAĞ','TEKİRDAĞ'),
('TOKAT','TOKAT'),
('TRABZON','TRABZON'),
('TUNCELİ','TUNCELİ'),
('ŞANLIURFA','ŞANLIURFA'),
('UŞAK','UŞAK'),
('VAN','VAN'),
('YOZGAT','YOZGAT'),
('ZONGULDAK','ZONGULDAK'),
('AKSARAY','AKSARAY'),
('BAYBURT','BAYBURT'),
('KARAMAN','KARAMAN'),
('KIRIKKALE','KIRIKKALE'),
('BATMAN','BATMAN'),
('ŞIRNAK','ŞIRNAK'),
('BARTIN','BARTIN'),
('ARDAHAN','ARDAHAN'),
('IĞDIR','IĞDIR'),
('YALOVA','YALOVA'),
('KARABÜK','KARABÜK'),
('KİLİS','KİLİS'),
('OSMANİYE','OSMANİYE'),
('DÜZCE','DÜZCE'),
)


class Profile(models.Model):
    author = models.ForeignKey("auth.User",on_delete=models.CASCADE, related_name='User')
    city = models.CharField(max_length=200,choices=CITY_CHOICES,blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    phone = models.CharField(max_length=15,blank=True, null=True)
    address = RichTextField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    add_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.add_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.author)

    class Meta:  
        ordering = ['-created_date']

