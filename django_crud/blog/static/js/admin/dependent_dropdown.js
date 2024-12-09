(function($) {
    $(document).ready(function() {
        // Function to populate subcategories
        function populateSubcategories(category_id, selected_subcategory) {
            var subcategory_field = $('#id_subcategory');
            
            // Clear previous options and reset the dropdown
            subcategory_field.empty();
            
            // Add placeholder option first
            subcategory_field.append('<option value="">---------</option>');

            if (category_id) {
                // Fetch subcategories based on the selected category
                $.ajax({
                    url: '/admin/get_subcategories/',  // Your view to get subcategories
                    data: {
                        'category_id': category_id
                    },
                    success: function(data) {
                        if (data.subcategories.length) {
                            // Track added subcategories to avoid duplicates
                            var subcategory_ids = new Set();

                            // Loop through the response and add subcategories to the dropdown
                            data.subcategories.forEach(function(subcategory) {
                                if (!subcategory_ids.has(subcategory.id)) {
                                    subcategory_field.append('<option value="' + subcategory.id + '">' + subcategory.name + '</option>');
                                    subcategory_ids.add(subcategory.id); // Ensure uniqueness
                                }
                            });

                            // If there's a selected subcategory, ensure it's pre-selected
                            if (selected_subcategory) {
                                subcategory_field.val(selected_subcategory);
                            }
                        } else {
                            // If no subcategories, show "No subcategories available"
                            subcategory_field.append('<option value="">No subcategories available</option>');
                        }
                    },
                    error: function(xhr, status, error) {
                        console.error("Error fetching subcategories:", status, error);
                    }
                });
            }
        }

        // Trigger change event when category is selected
        $('#id_category').change(function() {
            var category_id = $(this).val();
            var selected_subcategory = $('#id_subcategory').val();  // Get the current selected subcategory
            populateSubcategories(category_id, selected_subcategory);
        });

        // On page load, check if a category is selected or not
        var category_id = $('#id_category').val();
        var selected_subcategory = $('#id_subcategory').val();  // Get the current selected subcategory

        // If a category is selected, populate subcategories, otherwise, show placeholder
        // if (category_id) {
        //     populateSubcategories(category_id, selected_subcategory);
        // } else {
        //     // If no category selected, reset subcategory dropdown and show placeholder
        //     $('#id_subcategory').empty().append('<option value="">---------</option>');
        // }
    });
})(django.jQuery);
