(function(){
  "use strict";
  var body=document.body;
  var industry=body.dataset.industry||"unknown";
  var pageUrl=window.location.href;
  var bookingUrl="https://calendar.app.google/qwZB5sgoY74tPssA6";
  var params=new URLSearchParams(window.location.search);
  var attribution={industry:industry,page_url:pageUrl,utm_source:params.get("utm_source")||"",utm_medium:params.get("utm_medium")||"",utm_campaign:params.get("utm_campaign")||""};
  window.refrdaiLandingAttribution=attribution;

  function track(name,detail){
    var payload=Object.assign({event:name,industry:industry,page_path:window.location.pathname},detail||{});
    if(Array.isArray(window.dataLayer)){window.dataLayer.push(payload);}
    window.dispatchEvent(new CustomEvent("refrdai:funnel",{detail:payload}));
  }

  track("industry_page_view");
  document.querySelectorAll('[data-track="primary-cta"]').forEach(function(link){
    link.addEventListener("click",function(){track("industry_primary_cta_click");});
  });

  function revealBooking(){
    var panel=document.querySelector("[data-booking-panel]");
    if(!panel||panel.classList.contains("is-visible")){return;}
    panel.classList.add("is-visible");
    panel.removeAttribute("aria-hidden");
    track("industry_calendar_shown");
    panel.scrollIntoView({behavior:window.matchMedia("(prefers-reduced-motion: reduce)").matches?"auto":"smooth",block:"start"});
  }

  window.addEventListener("message",function(event){
    if(!event.data||event.data.type!=="hsFormCallback"){return;}
    if(event.data.eventName==="onFormSubmitted"){
      track("industry_form_submitted");
      revealBooking();
    }
  });

  document.querySelectorAll("[data-booking-link]").forEach(function(link){
    link.href=bookingUrl;
    link.addEventListener("click",function(){track("industry_booking_link_click");});
  });
})();
