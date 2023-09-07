document.addEventListener("DOMContentLoaded", function() {
    const domesticWebsiteSelect = document.getElementById("domesticWebsite");
    const internationalWebsiteSelect = document.getElementById("internationalWebsite");
    const additionalInfoDomestic = document.getElementById("additionalInfoDomestic");
    const additionalInfoInternational = document.getElementById("additionalInfoInternational");
    const internationalCategorySelect = document.getElementById("internationalCategory");
    const domesticCategorySelect = document.getElementById("domesticCategory");

    // Define category options for different websites
    const websiteCategoryOptions = {
        website1: ['all', 'merchandise trade', 'national account'],
        website2: ['monetary_and_financial_statistics_data',
                      'balance_of_payment_data',
                      'banks_reports',
                      'mfis_reports',
                      'flcs_reports', 'all'],
        website3: ['Category 5', 'Category 6'] // Add your actual options for Website 3
    };

    // Function to show additional information inputs
    function showAdditionalInfo(additionalInfoElement) {
        additionalInfoElement.style.display = "block";
    }

    // Function to hide additional information inputs
    function hideAdditionalInfo(additionalInfoElement) {
        additionalInfoElement.style.display = "none";
    }

    // Function to update category options based on the selected website
    function updateCategories(selectElement, website) {
        selectElement.innerHTML = '';
        websiteCategoryOptions[website].forEach(category => {
            const option = document.createElement('option');
            option.value = category;
            option.textContent = category;
            selectElement.appendChild(option);
        });
    }
    updateCategories(domesticCategorySelect, domesticWebsiteSelect.value);


    // Event listener for domestic website selection
    domesticWebsiteSelect.addEventListener("change", function() {
        updateCategories(domesticCategorySelect, this.value);
    });
    // Call hideAdditionalInfo to set the default state
    hideAdditionalInfo(additionalInfoInternational);

    // Event listener for international website selection
    internationalWebsiteSelect.addEventListener("change", function() {
        // TODO: Implement event handling for international website selection
        if (this.value === "website2") {
            showAdditionalInfo(additionalInfoInternational);
        } else {
            hideAdditionalInfo(additionalInfoInternational);
        }
    });



});



