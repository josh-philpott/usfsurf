$(document).ready(function() {
	//credit: Spencer Hawkins - www.spencerhawkins.com
	$(".tile-cover").mouseenter(hideCoverImg).mouseleave(showCoverImg);
	$(".tile").click(get_event);
});

function hideCoverImg() {
	$(this).animate({'opacity':.2},{queue: false});
}

function showCoverImg() {
	$(this).animate({'opacity':1},{queue: false});
}

function get_event(){
	Dajaxice.events.sayhello(my_callback, {'event_id': $(this).attr('id')});
}

function my_callback(data){

$(".event-image").replaceWith('')

if(data){
	$(".right-column h2").replaceWith ('<h2>' + data.name + '</h2>');
	$(".right-column p").replaceWith ('<p>' + data.description + '</p>');
	if(data.event_img3 != ""){
		$(".right-column p").after('<div class="event-image" ><img id="event-img3" src=' + data.event_img3 + '></div>');
	}
	if(data.event_img2 != ""){
		$(".right-column p").after('<div class="event-image" ><img id="event-img3" src=' + data.event_img2 + '></div>');
	}
	if(data.event_img1 != ""){
		$(".right-column p").after('<div class="event-image" ><img id="event-img1" src=' + data.event_img1 + '></div>');
	}

}else{
	$(".right-column p").replaceWith ('<p> There has been a problem. Please contact the webmaster.</p>');
}


}