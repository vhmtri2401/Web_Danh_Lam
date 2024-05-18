
jQuery(document).ready(function($){

if (jQuery().quicksand) {

 	// Clone applications to get a second collection
	var $data = $(".portfolio").clone();
	
	//NOTE: Only filter on the main portfolio page, not on the subdistrict pages
	$('.filter li').click(function(e) {
		$(".filter li").removeClass("active");	
		// Use the last district class as the district to filter by. This means that multiple districts are not supported (yet)
		var filterClass=$(this).attr('class').split(' ').slice(-1)[0];
		
		if (filterClass == 'all') {
			var $filteredData = $data.find('.item-thumbs');
		} else {
			var $filteredData = $data.find('.item-thumbs[data-type=' + filterClass + ']');
		}
		$(".portfolio").quicksand($filteredData, {
			duration: 600,
			adjustHeight: 'auto'
		}, function () {
		
			// Portfolio fancybox
		$(".fancybox").fancybox({				
				padding : 0,
				beforeShow: function () {
					this.title = $(this.element).attr('title');
					this.title = '<a href="'+ this.location + '">' +'<h4>' + this.title + '</h4>'+ '</a>' + '<p>' + $(this.element).parent().find('img').attr('alt') + '</p>';
				},
				helpers : {
					title : { type: 'inside' },
					location: (type:'inside'),
				}
			});


		});	
		$(this).addClass("active"); 			
		return false;
	});
	
}//if quicksand

});