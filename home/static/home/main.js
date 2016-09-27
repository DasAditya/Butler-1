
var RestaurantListPage = {
	init: function() {
		this.$container = $('.resto-container');
		this.bindEvents();
	},


	bindEvents: function() {
		$('.btn-favorite', this.$container).on('click', function(e) {
			e.preventDefault();

			var self = $(this);
			var url = $(this).attr('href');
			$.getJSON(url, function(result) {
				if (result.success) {
					$('.glyphicon-bookmark', self).toggleClass('active');
				}
			});

			return false;
		});
	}
};

$(document).ready(function() {
	RestaurantListPage.init();
});