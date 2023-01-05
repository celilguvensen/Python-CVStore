from django.db import models
from ckeditor.fields import RichTextField
 
# Create your models here.
POSITION_CHOICES = (
    ('Software Engineer','Software Engineer'),
    ('Akademisyen','Akademisyen'),
    ('Tıp Hekimi', 'Tıp Hekimi'),
    ('Diş Hekimi', 'Diş Hekimi'),
    ('Elektrik&Elektronik Mühendisi', 'Elektrik&Elektronik Mühendisi'),
    ('İnşaat Mühdendisi', 'İnşaat Mühdendisi'),
    ('Mimar', 'Mimar'),
    ('Muhasebeci', 'Muhasebeci'),
    ('Program Manager', 'Program Manager'),
    ('Ürün Yönetimi Uzmanı', 'Ürün Yönetimi Uzmanı'),
    ('Elektronik ve Haberleşme Mühendisi', 'Elektronik ve Haberleşme Mühendisi'),
    ('E-Ticaret Uzmanı', 'E-Ticaret Uzmanı'),
    ('Öğretmen', 'Öğretmen'),
    ('Borsa/Finans Uzmanı', 'Borsa/Finans Uzmanı'),
    ('Endüstri Mühendisi','Endüstri Mühendisi'),
    ('İnsan Kaynakları ','İnsan Kaynakları'),
    ('Avukat','Avukat'),
    ('Satış ve Pazarlama Uzmanı','Satış ve Pazarlama Uzmanı'),
    ('Network Security Engineer','Network Security Engineer'),
    ('IT Sistem Yöneticisi','IT Sistem Yöneticisi'),
    ('Diğer','Diğer'),
)

SECTOR_CHOICES = (
    ('Ar-Ge','Ar-Ge'),
    ('Bilişim','Bilişim'),
    ('Bilgi Teknolojileri','Bilgi Teknolojileri'),
    ('Üretim / Endüstriyel Ürünler','Üretim / Endüstriyel Ürünler'),
    ('Elektrik & Elektronik','Elektrik & Elektronik'),
    ('Güvenlik','Güvenlik'),
    ('Enerji','Enerji'),
    ('Gıda','Gıda'),
    ('Kimya','Kimya'),
    ('Maden ve Metal Sanayi','Maden ve Metal Sanayi'),
    ('Mobilya & Aksesuar','Mobilya & Aksesuar'),
    ('Ev Eşyaları','Ev Eşyaları'),
    ('Orman Ürünleri','Orman Ürünleri'),
    ('Ofis / Büro Malzemeleri','Ofis / Büro Malzemeleri'),
    ('Otomotiv','Otomotiv'),
    ('Sağlık','Sağlık'),
    ('Tarım / Ziraat','Tarım / Ziraat'),
    ('Taşımacılık','Taşımacılık'),
    ('Tekstil','Tekstil'),
    ('Telekomünikasyon','Telekomünikasyon'),
    ('Turizm','Turizm'),
    ('Yapı','Yapı'),
    ('Topluluklar','Topluluklar'),
    ('Hizmet','Hizmet'),
    ('Danışmanlık','Danışmanlık'),
    ('Reklam ve Tanıtım','Reklam ve Tanıtım'),
    ('Eğitim','Eğitim'),
    ('Finans - Ekonomi','Finans - Ekonomi'),
    ('Ticaret','Ticaret'),
    ('Denizcilik','Denizcilik'),
    ('Eğlence - Kültür - Sanat','Eğlence - Kültür - Sanat'),
    ('Basım - Yayın','Basım - Yayın'),
    ('Medya','Medya'),
    ('Havacılık','Havacılık'),
    ('Hızlı Tüketim Malları','Hızlı Tüketim Malları'),
    ('Sigortacılık','Sigortacılık',),
    ('Perakende','Perakende',),
    ('İletişim Danışmanlığı','İletişim Danışmanlığı'),
    ('Bilgi Teknolojileri','Bilgi Teknolojileri'),
    ('Dental','Dental'),
    ('Organizasyon','Organizasyon'),
    ('Diğer','Diğer'),
)

class Resume(models.Model):
    author = models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="Aday")
    position = models.CharField(max_length=50,choices=POSITION_CHOICES,verbose_name="Departman")
    sector = models.CharField(max_length=60,choices=SECTOR_CHOICES,verbose_name="Sektör")
    content = RichTextField(verbose_name="Ön Yazı",blank=True,null=True)
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    personal_image = models.FileField(blank=True,null=True,verbose_name="Fotoğraf Ekleyiniz")
    personal_cv = models.FileField(blank=True,null=True,verbose_name="Lütfen CV'nizi ekleyiniz")

    def __str__(self):
        return self.position

    class Meta:
        ordering = ["-created_date"]