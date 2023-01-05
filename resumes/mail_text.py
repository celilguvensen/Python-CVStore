
from django.conf import settings
 
from_email=settings.EMAIL_HOST_USER 
subject = "CV Store"


def message(first_name):


    return """Merhabalar {}

            Özgeçmişiniz incelendi. Yakın zamanda posta ya da telefon çağrısı alabilirsiniz.
            Kariyer Hayatınızda başarılar dileriz


            CV Store Kariyer Ekibi
            Saygılarımızla
            ...
            """.format(first_name)


