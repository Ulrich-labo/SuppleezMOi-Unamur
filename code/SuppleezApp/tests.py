from django.test import SimpleTestCase, TestCase, RequestFactory
from django.urls import reverse
from .models import UserApp,Demandes,Cours,ArchiveDemandeTraite,ArchiveDemandeSupprime,ImputationSalaire
from .forms import FormRegister,LoginForm,DemandesForm,CoursForm


################ models test ###################################
class UserAppTest(TestCase):
    def test_user_creation(self):
        """Test if a user is created successfully."""

        self.user = UserApp.objects.create_user(username='testuser', password='testpassword', first_name='Testf', last_name='Testl', email='test@gmail.com')
        self.assertTrue(UserApp.objects.filter(username='testuser', first_name='Testf', last_name='Testl', email='test@gmail.com').exists())


class CoursModelTest(TestCase):
    def setUp(self):
        # Create a test cours
        self.cours = Cours(code="INFOB", titre="Test Titre", Programmes="Test Programmes")
    
    def test_cours_representation(self):
        """Test if the string representation of Cours is correct."""
        self.assertEqual(str(self.cours), "INFOB Test Titre")

class ImputationSalaireModelTest(TestCase):
    def test_Imputation_representation(self):
        """Test if the string representation of ImputationSalaire is correct."""
       
        imputation = ImputationSalaire(imputation="Test Imputation")
        self.assertEqual(str(imputation), "Test Imputation")

class DemandesModelTest(TestCase):
    def setUp(self):
        # Create necessary objects for testing

        self.user = UserApp.objects.create_user(username='testuser', password='testpassword', first_name='Testf', last_name='Testl', email='test@gmail.com')
        self.cours = Cours.objects.create(code="INFOB", titre="Test Titre", Programmes="Test Programmes")
        self.imputation = ImputationSalaire.objects.create(imputation="Test Imputation")

    def test_demandes_representation(self):
        """Test if the string representation of Demandes is correct."""

        demande = Demandes(
            professeur=self.user,
            cours=self.cours,
            cours_optionnel="Oui",
            confirmation_Pour_cours_optionnel="Oui",
            suppleant="Test Suppleant",
            Motif="Test Motif",
            imputation=self.imputation,
            cpo="Test CPO",
            Accord_suppleant="Oui",
            remarque="Test Remarque",
            num_poste="Test Num Poste",
            salaire=233,
            Accord_CF="Oui",
            date_soumission="2024-02-22",
            statut_demande="En cours de traitement"
        )
        self.assertEqual(str(demande), "INFOB Test Titre")

class ArchiveDemandeTraiteModelTest(TestCase):
    def setUp(self):
        # Create necessary objects for testing
        
        self.user = UserApp.objects.create_user(username='testuser', password='testpassword', first_name='Testf', last_name='Testl', email='test@gmail.com')
        self.cours = Cours.objects.create(code="INFOB", titre="Test Titre", Programmes="Test Programmes")
        self.imputation = ImputationSalaire.objects.create(imputation="Test Imputation")

    def test_ArchiveTraite_representation(self):
        """Test if the string representation of ArchiveDemandeTraite is correct."""
        
        archive_demande = ArchiveDemandeTraite(
            professeur=self.user,
            cours=self.cours,
            cours_optionnel="Oui",
            confirmation_Pour_cours_optionnel="Oui",
            suppleant="Test Suppleant",
            Motif="Test Motif",
            imputation=self.imputation,
            cpo="Test CPO",
            Accord_suppleant="Oui",
            remarque="Test Remarque",
            num_poste="Test Num Poste",
            salaire=233,
            Accord_CF="Oui",
            date_soumission="2024-02-22",
            statut_demande="Approuvé"
        )
        self.assertEqual(str(archive_demande), "INFOB Test Titre")

class ArchiveDemandeSupprimeModelTest(TestCase):
    def setUp(self):
        # Create necessary objects for testing
        
        self.user = UserApp.objects.create_user(username='testuser', password='testpassword', first_name='Testf', last_name='Testl', email='test@gmail.com')
        self.cours = Cours.objects.create(code="INFOB", titre="Test Titre", Programmes="Test Programmes")
        self.imputation = ImputationSalaire.objects.create(imputation="Test Imputation")

    def test_ArchiveSupprime_representation(self):
        """Test if the string representation of ArchiveDemandeSupprime is correct."""
        
        archive_demande = ArchiveDemandeSupprime(
            professeur=self.user,
            cours=self.cours,
            cours_optionnel="Oui",
            confirmation_Pour_cours_optionnel="Oui",
            suppleant="Test Suppleant",
            Motif="Test Motif",
            imputation=self.imputation,
            cpo="Test CPO",
            Accord_suppleant="Oui",
            remarque="Test Remarque",
            num_poste="Test Num Poste",
            salaire=233,
            Accord_CF="Oui",
            date_soumission="2024-02-22",
            statut_demande="Refusé"
        )
        self.assertEqual(str(archive_demande), "INFOB Test Titre")



################  View test ############################
class HomeProfViewTest(SimpleTestCase):
    def test_home_page_loads_properly(self):
        """The home page loads properly"""
        
        response = self.client.get('https://suppleezmoi.unamurcs.be')
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        """ check if the template has the correct name"""  
        
        response = self.client.get(reverse("home-page"))
        self.assertTemplateUsed(response, "home.html")

    
    def test_url_available_by_name(self):
        """ the home page loads properly when the url name is used"""  
       
        response = self.client.get(reverse("home-page"))
        self.assertEqual(response.status_code, 200)

    
    def test_url_exists_at_correct_location(self):
        """check if the home page urls is at the correct location"""
        
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)



class ListDemandesViewTest(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = UserApp.objects.create_user(username='testuser', password='testpassword', first_name='Testf',last_name='Testl',email = 'test@gmail.com')
    
    def test_template_used(self):
        """Test that the correct template is used by the view"""
        
        self.client.force_login(self.user)
        response = self.client.get(reverse('list-demande'))
        self.assertTemplateUsed(response, 'listeDemande.html')

    def test_view_returns_200_when_authenticated(self):
        """Test that the view returns a 200 status code when the user is authenticated"""
        
        self.client.force_login(self.user)
        response = self.client.get(reverse('list-demande'))
        self.assertEqual(response.status_code, 200)

    def test_user_requests_are_displayed(self):
        """Test that the user's substitution requests are displayed in the template"""
        
        self.client.force_login(self.user)

        # Create a test substitution request for the user
        courstest = Cours.objects.create(code="INFOB",titre="test.titre",Programmes="test.programme")
        
        imputationtest = ImputationSalaire.objects.create(imputation="test.imputation")
        
        Demandes.objects.create(professeur=self.user, cours=courstest, cours_optionnel="Oui",
        confirmation_Pour_cours_optionnel="Oui", suppleant="testsuppleant",
        Motif="test.Motif", imputation=imputationtest, cpo="test.cpo",
        Accord_suppleant="Oui", remarque="test.remarque", num_poste="test.num_poste",
        salaire=233, Accord_CF="Oui", date_soumission="2024-02-22",
        statut_demande="En cours de traitement")
    
        response = self.client.get(reverse('list-demande'))
        
        #check if the informations which are supposed to figure on the page contain appear
        values_to_check = [courstest.code,courstest.titre, "testsuppleant", "test.Motif",imputationtest.imputation,"En cours de traitement","Oui"]

        for value in values_to_check:
            self.assertContains(response, value) 



class ListDemandesArchiveViewTest(TestCase):
    def setUp(self):
        # Set up a test user
        self.user = UserApp.objects.create_user(username='testuser', password='testpassword', first_name='Testf', last_name='Testl', email='test@gmail.com')

    def test_template_used(self):
        """Check if the correct template is used when accessing the archive-prof view."""
        
        self.client.force_login(self.user)
        response = self.client.get(reverse('archive-prof'))
        self.assertTemplateUsed(response, 'archiveprofesseur.html')

    def test_view_returns_200_when_authenticated(self):
        """Check if the archive-prof view returns a status code of 200 when the user is authenticated."""
        
        self.client.force_login(self.user)
        response = self.client.get(reverse('archive-prof'))
        self.assertEqual(response.status_code, 200)

    def test_archived_requests_are_displayed(self):
        """Check if archived requests are displayed correctly on the archive-prof view."""
        
        self.client.force_login(self.user)
        courstest = Cours.objects.create(code="INFOB", titre="test.titre", Programmes="test.programme")
        imputationtest = ImputationSalaire.objects.create(imputation="test.imputation")

        # Create archived demandes for the test user
        ArchiveDemandeSupprime.objects.create(professeur=self.user, cours=courstest, cours_optionnel="Oui",
        confirmation_Pour_cours_optionnel="Oui", suppleant="testsuppleant",Motif="test.Motif", imputation=imputationtest, cpo="test.cpo",
        Accord_suppleant="Oui", remarque="test.remarque", num_poste="test.num_poste",salaire=233, Accord_CF="Oui", date_soumission="2024-02-22",
        statut_demande="En cours de traitement")

        ArchiveDemandeTraite.objects.create(professeur=self.user, cours=courstest, cours_optionnel="Oui",
        confirmation_Pour_cours_optionnel="Oui", suppleant="testsuppleant",
        Motif="test.Motif", imputation=imputationtest, cpo="test.cpo",Accord_suppleant="Oui", remarque="test.remarque", num_poste="test.num_poste",
        salaire=233, Accord_CF="Oui", date_soumission="2024-02-22",
        statut_demande="Traité")

        response = self.client.get(reverse('archive-prof'))

        # Check if the information that is supposed to appear on the page contains the expected values
        values_to_check = [courstest.code,courstest.titre, "testsuppleant", "test.Motif",imputationtest.imputation,"Traité","Était en cours de traitement","Oui"]


        for value in values_to_check:
            self.assertContains(response, value)


class FormProfPageViewTest(TestCase):
    
    def setUp(self):
        # Set up a test user, cours, and imputation
        self.user = UserApp.objects.create_user(username='testuser', password='testpassword', first_name='Testf', last_name='Testl', email='test@gmail.com')
        self.cours = Cours.objects.create(code="INFOB", titre="test.titre", Programmes="test.programme")
        self.imputation = ImputationSalaire.objects.create(imputation="test.imputation")
    
    def test_get_view_authenticated_user(self):
        """Test if the form-prof view is accessible for an authenticated user."""
        
        self.client.force_login(self.user)
        response = self.client.get(reverse('form-prof'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'formprof.html')
    
    def test_get_view_non_authenticated_user(self):
        """Test if the form-prof view is not accessible for an non authenticated user."""
        response = self.client.get(reverse('form-prof'))
        self.assertTemplateUsed(response, 'generic_error.html')
        self.assertContains(response, 'Erreur de Validation')




class CustomLoginViewTest(TestCase):
    def test_get_login_view(self):
        """Test if the login-prof view is accessible via GET."""

        response = self.client.get(reverse('login-prof'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        self.assertTrue(isinstance(response.context['form'], LoginForm))

    def test_post_valid_login_form(self):
        """Test if a user can successfully log in with a valid login form."""

        user = UserApp.objects.create_user(username='testuser', password='testpassword', first_name='Testf', last_name='Testl', email='test@gmail.com')
        self.client.post(reverse('login-prof'), {'username': user.username, 'password': user.password})
        self.assertTrue(user.is_authenticated)

    def test_post_invalid_login_form(self):
        """Test if an invalid login form displays the correct error message."""

        response = self.client.post(reverse('login-prof'), {'username': 'invaliduser', 'password': 'invalidpassword'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        self.assertContains(response, 'Username ou password incorrecte.')

class SignUpViewTest(TestCase):
    def test_get_signup_view(self):
        """Test if the signup-page view is accessible via GET."""
        response = self.client.get(reverse('signup-page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')
        self.assertTrue(isinstance(response.context['form'], FormRegister))

    def test_post_valid_signup_form(self):
        """Test if a user can successfully sign up with a valid signup form."""
        self.client.post(reverse('signup-page'), {'username': 'newuser', 'password1': 'newpassword', 'password2': 'newpassword', 'first_name':'Testf', 'last_name':'Testl', 'email':'test@gmail.com'})
        self.assertTrue(UserApp.objects.filter(username='newuser').exists())

    def test_post_invalid_signup_form(self):
        """Test if an invalid signup form displays the correct error message."""
        response = self.client.post(reverse('signup-page'), {'username': 'newuser', 'password1': 'password', 'password2': 'differentpassword','first_name':'Testf', 'last_name':'Testl', 'email':'test@gmail.com'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')
        self.assertContains(response, 'Passwords do not match.')

class CoursViewTest(TestCase):
    def setUp(self):
        # Set up a test user
        self.user = UserApp.objects.create_user(username='testuser', password='testpassword', first_name='Testf', last_name='Testl', email='test@gmail.com')

    def test_get_cours_view_authenticated(self):
        """Test if the cours-prof view is accessible for an authenticated user."""
       
        self.client.force_login(self.user)
        response = self.client.get(reverse('cours-prof'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'encodercours.html')
        self.assertTrue(isinstance(response.context['form'], CoursForm))

    def test_get_view_non_authenticated_user(self):
        """Test if the cours-prof view  is not accessible for an non authenticated user."""
        response = self.client.get(reverse('cours-prof'))
        self.assertTemplateUsed(response, 'generic_error.html')
        self.assertContains(response, 'Erreur de Validation')

    
    def test_post_valid_cours_form(self):
        """Test if a valid cours form submission redirects and creates a new Cours object."""
        
        self.client.force_login(self.user)
        response = self.client.post(reverse('cours-prof'), {'code': 'INFOB', 'titre': 'Test Title', 'Programmes': 'Test Program'})
        self.assertRedirects(response, reverse('cours-prof'))
        self.assertTrue(Cours.objects.filter(code='INFOB', titre='Test Title', Programmes='Test Program').exists())

    def test_post_invalid_cours_form(self):
        """Test if an invalid cours form submission displays the correct error message."""
        self.client.force_login(self.user)
        response = self.client.post(reverse('cours-prof'), {'code': '', 'titre': '', 'Programmes': ''})
        self.assertTemplateUsed(response, 'generic_error.html')
        self.assertContains(response, 'Erreur de Validation')
    
class HomeProfViewTest(TestCase):
    def setUp(self):
        # Set up a test user
        self.user = UserApp.objects.create_user(username='testuser', password='testpassword', first_name='Testf', last_name='Testl', email='test@gmail.com')

    def test_get_home_prof_view_authenticated(self):
        """Test if the home-prof view is accessible for an authenticated user."""

        self.client.force_login(self.user)
        response = self.client.get(reverse('home-prof'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'homeprof.html')
        self.assertEqual(response.context['username'], 'Testf')
    
    def test_get_view_non_authenticated_user(self):
        """Test if the home-prof view  is not accessible for an non authenticated user."""
        response = self.client.get(reverse('home-prof'))
        self.assertTemplateUsed(response, 'generic_error.html')
        self.assertContains(response, 'Erreur de Validation')


class LogoutViewTest(TestCase):
    def setUp(self):
        # Set up a test user
        self.user = UserApp.objects.create_user(username='testuser', password='testpassword', first_name='Testf', last_name='Testl', email='test@gmail.com')

    def test_logout_authenticated_user(self):
        """Test if logging out an authenticated user redirects to the home page."""

        self.client.force_login(self.user)
        response = self.client.get(reverse('logout'))
        self.assertRedirects(response, reverse('home-page'))
        
    def test_get_view_non_authenticated_user(self):
        """Test if logging out an  non authenticated  is not possible."""
        response = self.client.get(reverse('logout'))
        self.assertTemplateUsed(response, 'generic_error.html')
        self.assertContains(response, 'Erreur de Validation')

