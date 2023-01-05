from django import forms

from resumes.models import Resume


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ["sector","position","content","personal_image","personal_cv"]

    def clean(self):
        sector = self.cleaned_data.get("sector")
        position = self.cleaned_data.get("position")
        content = self.cleaned_data.get("content")
        personal_image = self.cleaned_data.get("personal_image")
        personal_cv = self.cleaned_data.get("personal_cv")
         
 
        print(content)

        if (len(str(content)) >= 750):
            print("test")
            raise forms.ValidationError("Ön yazı karakter sayısı 700'den büyük olamaz")

        else:        
            values = {              
                "sector":sector,
                "position":position,
                "content":content,
                "personal_image":personal_image,
                "personal_cv":personal_cv,
            }

            return values