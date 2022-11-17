from django import forms
from .models import Clubs,ClubImage

class Club_Form(forms.ModelForm):
  class Meta:
    model = Clubs
    fields = ["club_name", "breif",]
    labels = {'club_name': "Name", "breif": "A breif about your club",}
 

class ImageForm(forms.ModelForm):  
    type = forms.CharField(label='Name')
    class meta:  
        model=ClubImage
        fields = ["title","photo"]
        
    
        
class ClubForm(forms.Form):
    club_name = forms.CharField(max_length=50, required=True)
    breif = forms.CharField(max_length=300, required=True)
    title = forms.CharField(max_length=20)
    photo = forms.ImageField(required=True)
    print("form made")
    def save(self, commit=True):
      print("running")
      obj, created = Clubs.objects.get_or_create(
            club_name=self.cleaned_data['club_name'],
            breif=self.cleaned_data['breif']
        )
      obj2,created = ClubImage.objects.get_or_create(
          title=self.cleaned_data["title"],
          photo=self.cleaned_data["photo"],
          club=obj
          
        )
      print(self.cleaned_data["photo"])
      obj.save()
      obj2.save()
      return obj,obj2
  
    
