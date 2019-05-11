$(document).ready(function(){
  $("#test").click(function(){
    alert("success")
  })
  $("#clickSearch").click(function(){
    $("#search").fadeIn(2000)
    $("#search").show()
  })
  $("#copy").click(function(){
    alert("done")

    $("#paste").show()
  })
  // $("#paste").click(function(){
  //   $("#copy").hide()
  // })
  $(function () {
$('[data-toggle="popover"]').popover()
})
$('.popover-dismiss').popover({
trigger: 'focus'
})
})
