$(document).ready(function(){
  var typed=new Typed(`#typed`,{
    strings:["Hi, WElcome to my Profile","I am Collins kipkemoi a Full stack web Developer"],
    backSpeed:40,
    typeSpeed:40,
    smartBackspace:true,
  })

    var typed=new Typed(`#code`,{
      strings:["JavaScript","CSS3","HTML5","TypeScript","Java"],
      backSpeed:60,
      typeSpeed:60,
      loop:true
    })

    // $("#slide").click(function(){
    //   $("html,body").animate({scrollTop:$(document).height()},'slow');
    //   return false;
    // })
    $("#next").click(function(){
      $(".about").fadeOut(500);
      $(".about").hide();
      $(".skills").fadeIn(500)
      $(".skills").show();
      $(".hide").show();
    })
    $("#skilled").click(function(){
      $(".about").fadeOut(500);
      $(".about").hide();
      $(".skills").fadeIn(500)
      $(".skills").show();
      $(".hide").show();
    })




})
