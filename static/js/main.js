$(document).ready(function(){
  $("#test").click(function(){
    alert("success")
  })
  $("#clickSearch").click(function(){
    $("#search").fadeIn(2000)
    $("#search").show()
  })
  $("#copy").click(function(){
    $("#copy").hide()
    
    $("#paste").show()
  })
  // $("#paste").click(function(){
  //   $("#copy").hide()
  // })
})
