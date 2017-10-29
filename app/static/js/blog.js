
jQuery(document).ready(function($){

	//Responsive navigation animation

	jQuery("#burgernav").click(function(){

    jQuery(this).toggleClass("is-active");
    jQuery('body').toggleClass('with--sidebar');

	});

    jQuery('#site-cache').click(function(e){
      jQuery("#burgernav").toggleClass("is-active");
      jQuery('body').removeClass('with--sidebar');
    });

	//create the slider
	jQuery('.cd-testimonials-wrapper').flexslider({
		selector: ".cd-testimonials > li",
		animation: "slide",
		controlNav: true,
		slideshow: false,
		smoothHeight: true,
		start: function(){
			jQuery('.cd-testimonials').children('li').css({
				'opacity': 1,
				'position': 'relative'
			});
		}
	});

	//Video Controls

	//Handle to controls
	var playicon = jQuery(".playpause");
	var video = jQuery(".video");
	var volume = jQuery(".volume");

	//when video is played
	video.on('play', function () {
    // do something
    playicon.hide();
	});

	//when video is paused or ends
	video.on('pause ended', function () {
		playicon.show();
	});

	//when video is clicked at any point on the screen like youtube video
	video.click(function(){

		//Check if video is in the paused state
		if(video[0].paused == true){

			video[0].play();

		}

		//if video is in the play state
		else{
			video[0].pause();
		}

	});

 	//On volume click
 	volume.click(function(){

 		jQuery(this).toggleClass("muted");
 		var bool = video.prop("muted");
 		video.prop("muted",!bool);
 	});

});

jQuery(window).load(function(){
	jQuery(".load-overlay").fadeOut('slow', function(){
		jQuery(this).remove();
	});
	var searchinputhandle = jQuery(".search-input");
	var searchbutton = jQuery(".searchbtn");
	jQuery('#lifegrid').NewWaterfall({
		width: 310,
		delay: 60,
		repeatShow: false
	});
	searchbutton.click(function(e){
		e.stopPropagation();
		searchinputhandle.toggleClass("stretch");
	});

	jQuery('.paging a').addClass('paging-button com-btn');
	var inputVal = jQuery('.search-input').val();
		inputVal = jQuery.trim(inputVal).length;
	if( inputVal !== 0){
		jQuery('.life-search input.searchbox-submit').css('z-index','800');
		//$('.searchbox-icon').css('display','none');
	} else {
		jQuery('.search-input').val('');
		jQuery('.life-search input.searchbox-submit').css('z-index','');
		//$('.searchbox-icon').css('display','block');
	}

});
	function buttonUp()
	{
		var inputVal = jQuery('.life-search .search-input').val();
		//alert(inputVal);
		inputVal = jQuery.trim(inputVal).length;
		if( inputVal !== 0)
		{
			jQuery('.life-search input.searchbox-submit').css('z-index','800');
			jQuery('.searchbtn').css('display','none');
		} else
		{
		jQuery('.life-search .search-input').val('');
		jQuery('.life-search input.searchbox-submit').css('z-index','');
		jQuery('.searchbtn').css('display','block');
		}
	}
jQuery(document).ready(function()
{
	jQuery(".top-btn").click(function()
	{
		jQuery(".maintopnav").slideToggle();
	});
	jQuery(".menuIcon").click(function()
	{
		jQuery(".menuIcon").toggleClass("active");
	});
	jQuery(document.body).click( function()
	{
		jQuery(".searchbtn").removeClass("stretch");
		jQuery(".profile-menu").removeClass("profile-slide");
		//alert("hello");
	});
	jQuery(".mobile-profile .user-profile").click(function(e)
	{
		e.stopPropagation();
		jQuery(".profile-menu").toggleClass("profile-slide");
	});
	jQuery(document).ready(function() {
		jQuery('.fb-share').click(function(e) {
			e.preventDefault();
			window.open(jQuery(this).attr('href'), 'fbShareWindow', 'height=450, width=550, top=' + (jQuery(window).height() / 2 - 275) + ', left=' + (jQuery(window).width() / 2 - 225) + ', toolbar=0, location=0, menubar=0, directories=0, scrollbars=0');
			return false;
		});
	});

});

jQuery(document).ready(function() {
	jQuery(".topnav").accordion({
		accordion:false,
		speed: 500,
		closedSign: '+',
		openedSign: '-'
	});
});
jQuery(window).bind("pageshow", function() { jQuery('.life-search input.searchbox-submit').css('z-index',''); });








(function($)
{
	$.fn.NewWaterfall = function(options)
	{

		var defaults = {
			width: 360,
			delay: 60,
			repeatShow: false
		};
		var config = $.extend({},defaults, options);
		var ul = this;

		var show = function(li)
		{
			if ($(window).scrollTop() + $(window).height() > $(li).offset().top)
			{
				$(li).addClass('show');
			}
			else if ($(window).scrollTop() + $(window).height() < $(li).offset().top)
			{
				if (config.repeatShow)
				{
					$(li).removeClass('show');
				}
			}
		}
		var refresh = function()
		{
			if(ul.length <= 0)
			{
				return;
			}

			ul.css({
				"position": "relative"
			});


			var lis = $(ul).children("li");

			if(lis.length <= 0)
			{
				return;
			}

			var ul_width = $(ul).width();
			var ul_column = parseInt(ul_width / config.width);

			if (lis.length < ul_column)
			{
				ul_column = lis.length;
			}

			var li_left = (ul_width - ul_column * config.width) / 2;

			if (ul_column > 0)
			{

				lis.css({
					"position": "absolute",
					"width": config.width
				});


				var maxHeight = 0;
				var list = []
				var nlist = []


				for (var i = 0; i < lis.length; i++)
				{
					list.push({
						"index": i,
						"bottom": 0,
						"height": $(lis[i]).height(),
					});
				}


				for (var i = 0; i < ul_column; i++)
				{
					nlist.push([]);
				}


				for (var i = 0; i < lis.length; i++)
				{
					if (i < ul_column)
					{
						list[i]["bottom"] = list[i]["height"];
						nlist[i].push(list[i]);
					}
					else
					{
						var b = 0;
						var l = 0;
						for (var j = 0; j < ul_column; j++)
						{
							var jh = nlist[j][nlist[j].length - 1]["bottom"] + list[i]["height"];
							if (b == 0 || jh < b)
							{
								b = jh;
								l = j;
							}
						}
						list[i]["bottom"] = b;
						nlist[l].push(list[i]);
					}
				}


				for (var i = 0; i < nlist.length; i++)
				{
					for (var j = 0; j < nlist[i].length; j++)
					{
						$(lis[nlist[i][j]["index"]]).css({
							"left": i * config.width + li_left,
							"top": nlist[i][j]["bottom"] - nlist[i][j]["height"]
						});
					}
				}


				for (var i = 0; i < nlist.length; i++)
				{
					var h = nlist[i][nlist[i].length -1]["bottom"];
					if (maxHeight < h)
					{
						maxHeight = h;
					}
				}
				$(ul).css("height",maxHeight);
			}
			else
			{
				lis.attr("style","");
				ul.attr("style","");
			}


			for (var i = 0; i < lis.length; i++)
			{
				show(lis[i]);
			}
		}


		refresh();
		setInterval(refresh,config.delay);
	}
})(jQuery);
