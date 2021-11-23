from django import forms
from .models import Tags, Posts
from mptt.forms import TreeNodeChoiceField

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = '__all__'


class NewTagsForm(forms.ModelForm):
    parent = TreeNodeChoiceField(queryset=Tags.objects.all())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['parent'].widget.attrs.update(
            {'class': 'd-none'})
        self.fields['parent'].label = ''
        self.fields['parent'].required = False

    class Meta:
        model = Tags
        fields = ('name', 'parent')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'col-sm-12'}),
        }

    def save(self, *args, **kwargs):
        Tags.objects.rebuild()
        return super(NewTagsForm, self).save(*args, **kwargs)
