from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Demandes, UserApp, Cours


class FormRegister(forms.ModelForm):
    """
    A form for user registration
    ...
    Attributes
    ----------
    password1 : CharField
        password input field
    password2 : CharField
        confirmation password input field
    
    Methods
    -------
    clean()
        Validate password match
    save(commit=True)
        Save the user with the hashed password
    """

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        """
        Meta class for FormRegister
        """
        model = UserApp
        fields = ['first_name', 'last_name', 'email', 'username']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])

        if commit:
            user.save()

        return user



class LoginForm(forms.Form):
    """
    A form for user login
    ...
    Attributes
    ----------
    username : CharField
        username input field
    password : CharField
        password input field
    
    Methods
    -------
    __init__(*args, **kwargs)
        Constructor method for the form
    """

    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



class CoursForm(forms.Form):
    """
    A form for course information
    ...
    Attributes
    ----------
    code : CharField
        course code input field
    titre : CharField
        course title input field
    Programmes : CharField
        course programs input field
    
    Methods
    -------
    __init__(*args, **kwargs)
        Constructor method for the form
    """

    code = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    titre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    Programmes = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
   

class DemandesForm(forms.ModelForm):
    """
    A form for professor's requests
    ...
    Attributes
    ----------
    Meta : class
        Metadata for the form, specifying the model and fields to exclude
    __init__(*args, **kwargs)
        Constructor method for the form
    """

    class Meta:
        """
        Metadata for DemandesForm
        """
        model = Demandes
        exclude = ['remarque', 'num_poste', 'salaire', 'Accord_CF', 'professeur', 'statut_demande']
        required = {'imputation': False, 'suppleant': False, 'confirmation_Pour_cours_optionnel': False, 'cpo': False}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Add the 'form-control' class to all fields to use Bootstrap design
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


