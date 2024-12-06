(function($) {
    $(document).ready(function() {
        // Trigger change event when category is selected
        $('#id_category').change(function() {
            var category_id = $(this).val();
            var subcategory_field = $('#id_subcategory');  // Fixed the ID to lowercase "id_subcategory"

            // Clear existing subcategory options
            subcategory_field.empty();
            subcategory_field.append('<option value="">---------</option>'); // Default placeholder

            if (category_id) {
                // Fetch subcategories based on the selected category
                $.ajax({
                    url: '/admin/get_subcategories/',  // Your view to get subcategories
                    data: {
                        'category_id': category_id
                    },
                    success: function(data) {
                        if (data.subcategories.length) {
                            // Add the fetched subcategories to the dropdown
                            data.subcategories.forEach(function(subcategory) {
                                subcategory_field.append('<option value="' + subcategory.id + '">' + subcategory.name + '</option>');
                            });
                        } else {
                            subcategory_field.append('<option value="">No subcategories available</option>');
                        }
                    },
                    error: function(xhr, status, error) {
                        console.error("Error fetching subcategories:", status, error);
                    }
                });
            }
        });
    });
})(django.jQuery);
