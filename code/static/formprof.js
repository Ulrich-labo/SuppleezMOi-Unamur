


// Handling the click event for the "Contact Administration" link
document.getElementById("contactAdministration").addEventListener("click", function() {
    // Redirecting to the specified email address with a subject
    window.location.href = "mailto:demandesuppleance@gmail.com?subject=Contact%20l'administration";
});


// jQuery document ready function
jQuery(document).ready(function ()  {

    // Handling the change event for the 'Cours Optionnel' dropdown
    $('#id_cours_optionnel').change(function () {
        var coursValue = $(this).val();

            if (coursValue === 'Oui') {
                
                // Asking for confirmation if the selected value is 'Oui'
                var confirmation = confirm("Ce cours étant optionnelle il sera organisé uniquement s'il y a au moins un étudiant qui a choisi ce cours. Confirmez vous votre choix concernant le cours ?");
            
                if (confirmation) {
                    // If the user clicks OK, setting the value to 'Oui'
                    $('#id_confirmation_Pour_cours_optionnel').val('Oui');
                } else {
                    // If the user clicks Cancel, setting the value to 'Non'
                    $('#id_confirmation_Pour_cours_optionnel').val('Non');
                }
            } else {
                // Resetting the confirmation field if the course is not optional
                $('#id_confirmation_Pour_cours_optionnel').val('Non');
            }
        
    });
    
    


    

     // Handling the change event for the 'Accord_suppleant' dropdown
    $('#id_Accord_suppleant').change(function () {
        var value = $(this).val();
        if (value === 'Oui') {
            // Displaying a confirmation if the value is 'Oui'
            var confirmation = confirm("Veuillez transmettre le mail d’accord du suppléant au secrétariat ; il devra être joint à la demande au CA.");
        } 
    });


    // Handling the change event for the 'imputation' dropdown
    $('#id_imputation').change(function () {
        var imputationSalaire = $(this).val();
    
        // Selecting the common container including the 'cpo' field and its label
        var container = $('#id_cpo').closest('.mb-3');
    
         // Showing or hiding based on the value of 'imputationSalaire'
            if (imputationSalaire === '2') {
                container.show();  // Showing the container (which includes the field and the label)
                $('#id_cpo').val('Veuillez remplire');
            }
            else {
                container.hide();  // Hiding the container (which includes the field and the label)
                $('#id_cpo').val('None');
            }
    });

    
    



    // Handling the form submission
    $('form').submit(function (event) {
        // Retrieving the value of the 'Accord_suppleant' field
        var accordSuppleantValue = $('#id_Accord_suppleant').val();
        var imputationSalaire = $('#id_imputation').val();
        var Value = $('#id_suppleant').val();
        var coursValue = $('#id_cours_optionnel').val();

 
        if (accordSuppleantValue === '') {
            // Alerting if no valid option is selected for the 'Accord_suppleant' field
            alert("Veuillez sélectionner une option valide pour l'accord du suppléant avant de soumettre le formulaire.");
            event.preventDefault();
        }

        if (imputationSalaire === '') {
            // Alerting if no valid option is selected for the 'imputation' field
            alert("Veuillez sélectionner une option valide pour l'imputation de salaire avant de soumettre le formulaire.");
            event.preventDefault();
        }

            // Handling the change event for the 'Proposition de suppléant' 
        if (Value === '') {
            // Alerting if no valid option is selected for the 'Proposition de suppléant' field
            alert("Veuillez sélectionner une option valide pour le champs Proposition de suppléant avant de soumettre le formulaire.");

        }

        if (coursValue === '') {
            // Alerting if no valid option is selected for the 'Cours Optionnel' field
            alert("Veuillez sélectionner une option valide pour le champs cours optionnel avant de soumettre le formulaire.");
        }
  
    });
  
});

// Another jQuery document ready function for form validation
jQuery(document).ready(function () {
    // Handling the form submission
    $('form').submit(function (event) {
        // Resetting styles
        $('.form-control').removeClass('is-invalid');
        $('.error-message').remove();

        // Checking if the form is valid
        if (!isFormValid()) {
            event.preventDefault();
        }
    });

    // Function to check the validity of the form
    function isFormValid() {
        var isValid = true;

        // Checking each required field
        $('.form-control[required]').each(function () {
            // Checking if the field is empty
            if ($(this).val() === '') {
                // Adding the 'is-invalid' class to outline in red
                $(this).addClass('is-invalid');

                // Adding an error message next to the field
                $(this).after('<div class="error-message">Ce champ est obligatoire.</div>');

                isValid = false;
            }
        });

        return isValid;
    }
});


