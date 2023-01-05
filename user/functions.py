
from django.conf import settings
 
from_email=settings.EMAIL_HOST_USER 
subject = "CV Store"


def message(first_name):


    return """Merhabalar {}

            CV Store Hoşgeldiniz, Profile bilgilerinizi ve Özgeçmişinizi ekleyerek Kariyer Fırsatlarınıza ulaşabilirsiniz
            Kariyer hayatınızda başarılar dileriz
            
            CV Store Kariyer Ekibi
            Saygılarımızla
            ...
            """.format(first_name)


