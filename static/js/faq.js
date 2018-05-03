$(function(){
    var x =$("#firstQuestion,#secondQuestion")
    x.hide()

    

    $("#first_button").click(function(){
        var x =$("#firstQuestion")
        x.toggle()       
    })
    $("#second_button").click(function(){
        var y =$("#secondQuestion")
        y.toggle()       
    })
})
