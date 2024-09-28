from django.shortcuts import render,redirect
from django.views.generic import CreateView,TemplateView
from .forms import FormRegister,LoginForm,DemandesForm,CoursForm
from .models import UserApp,Demandes,Cours,ArchiveDemandeTraite,ArchiveDemandeSupprime
from django.urls import reverse_lazy
from django.template import RequestContext
from django.views import View
from django.contrib import messages
from django.contrib.auth import logout,login,authenticate

class CustomLoginView(View):
    """
    A class handling custom login functionality
    ...
    Attributes
    ----------
    template_name : str
        the HTML template file for the login view
    
    Methods
    -------
    get(self, request, *args, **kwargs)
        Handle GET requests to display the login form
    
    post(self, request, *args, **kwargs)
        Handle POST requests to process login data
    """

    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        # Create an instance of the login form
        form = LoginForm()

        # Prepare context with the form
        context = {'form': form}
        
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        # Create an instance of the login form with POST data
        form = LoginForm(request.POST)
        
        try:
            # Assertion to check if the form is valid
            assert form.is_valid(), "Le formulaire est invalide. Vous avez probablement saisi une valeur invalide pour l'un des champs"

            # Retrieve username and password from the form
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            # Authenticate user
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # Log in the user
                login(request, user)
                
                # Redirect to the home-prof page upon successful login
                return redirect('home-prof')
            else:
                # Add error message to the form in case of invalid username or password
                form.add_error(None, 'Username ou password incorrecte.')

            # Prepare context with the form
            context = {'form': form}
            
            return render(request, self.template_name, context)
        
        except AssertionError as e:

            context = {'error_message': e.args[0]}
            return render(request, 'generic_error.html', context)


class SignUpView(CreateView):
    """
    A class handling user signup functionality
    ...
    Attributes
    ----------
    model : Model
        the UserApp model for user registration
    template_name : str
        the HTML template file for the signup view
    form_class : Form
        the registration form class (FormRegister)
    success_url : str
        the URL to redirect to upon successful signup
    
    Methods
    -------
    No specific methods added
    """

    model = UserApp
    template_name = 'signup.html'
    form_class = FormRegister
    success_url = reverse_lazy('login-prof')

class CoursView(View):
    """
    A class handling course creation functionality
    ...
    Attributes
    ----------
    template_name : str
        the HTML template file for the course creation view
    
    Methods
    -------
    get(self, request)
        Handle GET requests to display the course creation form

    post(self, request)
        Handle POST requests to process course creation data
    """

    template_name = 'encodercours.html'
 
    def get(self, request):

        try:
            # Assertion to check if the user is authenticated
            assert request.user.is_authenticated, "vous n'êtes pas authentifié. Vous devez vous connecter avant de pouvoir accéder à cette page."
            form = CoursForm()
            return render(request, self.template_name, {'form': form})
        
        except AssertionError as e:
            context = {'error_message': e.args[0]}
            return render(request, 'generic_error.html', context)
        
    def post(self, request):

        try:
            # Assertion to check if the user is authenticated
            assert request.user.is_authenticated, "vous n'êtes pas authentifié. Vous devez vous connecter avant de pouvoir accéder à cette page."
            form = CoursForm(request.POST)
            # Assertion to check if the form is valid
            assert form.is_valid(), "Le formulaire est invalide. Vous avez probablement saisi une valeur invalide pour l'un des champs.Ou oubliez de remplir un champ."
            cours = Cours.objects.create(
                code=form.cleaned_data['code'],
                titre=form.cleaned_data['titre'],
                Programmes=form.cleaned_data['Programmes']
            )

            return redirect('form-prof')   
          
        except AssertionError as e:
            context = {'error_message': e.args[0]}
            return render(request, 'generic_error.html', context)
        
class HomeProfView(View):
    """
    A class handling the home page for professors
    ...
    Attributes
    ----------
    template_name : str
        the HTML template file for the professor's home page
    
    Methods
    -------
    get(self, request)
        Handle GET requests to display the professor's home page
    """

    template_name = 'homeprof.html'

    def get(self, request):
        
        try:
            # Assertion to check if the user is authenticated
            assert request.user.is_authenticated, "vous n'êtes pas authentifié. Vous devez vous connecter avant de pouvoir accéder à cette page."
    
            user = request.user
            username = user.first_name

            # Pass the username to the context
            context = {'username': username}

            return render(request, self.template_name, context)
    
        except AssertionError as e:
            context = {'error_message': e.args[0]}
            return render(request, 'generic_error.html', context)


class LogoutView(View):
    """
    A class handling user logout (sign out) functionality
    ...
    Methods
    -------
    get(self, request, *args, **kwargs)
        Handle GET requests to log the user out and redirect to the home page
    """

    def get(self, request, *args, **kwargs):

        try:
            # Assertion to check if the user is authenticated before logging out
            assert request.user.is_authenticated, "Vous n'êtes pas connecté, donc vous ne pouvez pas vous déconnecter"

            logout(request)  # Log out the user
            return redirect('home-page')
        
        except AssertionError as e:
            context = {'error_message': e.args[0]}
            return render(request, 'generic_error.html', context)

class FormProfPageView(View):
    """
    A class handling the form submission request for professors
    ...
    Attributes
    ----------
    template_name : str
        the HTML template file for the form submission view
    
    Methods
    -------
    get(self, request)
        Handle GET requests to display the form for submission
    
    post(self, request)
        Handle POST requests to process form submission data
    """
   
    template_name = 'formprof.html'
    
    def get(self, request):
        
        try:
            # Assertion to check if the user is authenticated
            assert request.user.is_authenticated, "vous n'êtes pas authentifié. Vous devez vous connecter avant de pouvoir accéder à cette page."
            
            form = DemandesForm()
            context = {'form': form}
            return render(request, self.template_name, context) 
        
        except AssertionError as e:
            context = {'error_message': e.args[0]}
            return render(request, 'generic_error.html', context)
            

    def post(self, request):
       
        try:
            # Assertion to check if the user is authenticated
            assert request.user.is_authenticated, "Vous n'êtes pas authentifié. Vous devez vous connecter avant de pouvoir accéder à cette page."

            form = DemandesForm(request.POST)
            context = {'form': form}

            # Assertion to check if the form is valid
            assert form.is_valid(), "Le formulaire est invalide. Veuillez vérifier les champs."

            # Retrieve information about the course and submission date from the request
            cours = form.cleaned_data.get('cours')
            year = form.cleaned_data.get('date_soumission').year
            prof = request.user

            # Check if there is already a request for the same course and year
            existing_demande = Demandes.objects.filter(cours=cours, date_soumission__year=year, professeur=prof).first()

            # Assertion to check if no request exists for the same course and year
            assert not existing_demande, f"Une demande portant votre nom comme professeur titulaire pour ce cours existe déjà cette année {year}. Si elle n'a pas été soumise par vous, veuillez contacter l'administration."

            # If no request exists, save the form data
            demande = form.save(commit=False)
            demande.professeur = request.user
            demande.save()
            return redirect('list-demande')

        except AssertionError as e:
            context = {'error_message': e.args[0]}
            return render(request, 'generic_error.html', context)

            


class HomeView(TemplateView):
    """
    A class handling the home page view
    ...
    Attributes
    ----------
    template_name : str
        the HTML template file for the home page
    
    Methods
    -------
    get_context_data(self, **kwargs)
        Provide additional data to the template context during rendering
    """

    template_name = 'home.html'

    def get_context_data(self, **kwargs):
  
        # Call the get_context_data method of the parent class
        # to obtain the existing context.
        context = super().get_context_data(**kwargs)
        
        # Add a 'welcome_message' key to the context with the value of the welcome message.
        context['welcome_message'] = "Bienvenue sur le site de demande de suppléance de l'université de Namur"

      
        # Return the updated context.
        return context

class ListDemandesView(View):
    """
    A class handling the  view for the list of substitution requests in evaluation 
    ...
    Attributes
    ----------
    template_name : str
        the HTML template file for the list of substitution requests view
    
    Methods
    -------
    get(self, request, *args, **kwargs)
        Handle GET requests to display the list of substitution requests
    """

    template_name = 'listeDemande.html'

    def get(self, request, *args, **kwargs):

        try:
   
            # Assertion to check if the user is authenticated
            assert request.user.is_authenticated, "vous n'êtes pas authentifié. Vous devez vous connecter avant de pouvoir accéder à cette page."

            user = request.user
            username = user.first_name

            # Retrieve all requests in evaluation of the current user
            user_demandes = Demandes.objects.filter(professeur=user)

            # Pass the requests to the context
            context = {'user_demandes': user_demandes, 'username': username}

            return render(request, self.template_name, context)
        
        except AssertionError as e:
            context = {'error_message': e.args[0]}
            return render(request, 'generic_error.html', context)

class ListDemandesArchiveView(View):
    """
    A class handling the archived substitution requests page for professors
    ...
    Attributes
    ----------
    template_name : str
        the HTML template file for the archived substitution requests view
    
    Methods
    -------
    get(self, request, *args, **kwargs)
        Handle GET requests to display the archived substitution requests
    """

    template_name = 'archiveprofesseur.html'
    def get(self, request, *args, **kwargs):
        
        try:
            # Assertion to check if the user is authenticated
            assert request.user.is_authenticated, "vous n'êtes pas authentifié. Vous devez vous connecter avant de pouvoir accéder à cette page."

            user = request.user
            username = user.first_name
            
            # Retrieve all deleted and treated requests of the current user
            user_demandes_supprime = ArchiveDemandeSupprime.objects.filter(professeur=user)
            user_demandes_traite = ArchiveDemandeTraite.objects.filter(professeur=user)

            # Pass the archived requests to the context
            context = {'user_demandes_supprime': user_demandes_supprime,'user_demandes_traite':user_demandes_traite,'username':username}

            return render(request, self.template_name,context)
        
        except AssertionError as e:
            context = {'error_message': e.args[0]}
            return render(request, 'generic_error.html', context)
        

#some views for error handling

def csrf_failure(request, reason=""):
    """
   handling CSRF problem display for the user
    """

    context = {'message': "Un problème CSRF a été détecté. Essayez de recharger la page ou contactez l'administrateur si le problème persiste."}
    return render(request,'template_erreur_csrf.html', context)

def erreur_404(request, exception):
    """
    handling Page non found Error display
    """
    return render(request, '404.html')


def erreur_500(request):
    """
    handling Page for internal server Error display
    """
    return render(request, '500.html')

