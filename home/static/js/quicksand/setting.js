jQuery.noConflict();
jQuery(document).ready(function($){

if (jQuery().quicksand) {

 	// Clone applications to get a second collection
	var $data = $(".portfolio-area").clone();
	
	//NOTE: Only filter on the main portfolio page, not on the subdistrict pages
	$('.portfolio-categ li').click(function(e) {
		$(".filter li").removeClass("active");	
		// Use the last district class as the district to filter by. This means that multiple districts are not supported (yet)
		var filterClass=$(this).attr('class').split(' ').slice(-1)[0];
		
		if (filterClass == 'all') {
			var $filteredData = $data.find('.item-thumbs');
		} else {
			var $filteredData = $data.find('.item-thumbs[data-type=' + filterClass + ']');
		}
		$(".portfolio-area").quicksand($filteredData, {
			duration: 600,
			adjustHeight: 'auto'
		}	
		$(this).addClass("active"); 			
		return false;
	});
	
}//if quicksand

});