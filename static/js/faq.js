$(function(){
    var x =$("#firstQuestion,#secondQuestion,#thirdQuestion")
    x.hide()
    $("#first_button").click(function(){
        var x =$("#firstQuestion")
        x.toggle()       
    })
    $("#second_button").click(function(){
        var y =$("#secondQuestion")
        y.toggle()       
    })
    $("#third_button").click(function(){
        var y =$("#thirdQuestion")
        y.toggle()       
    })
})
