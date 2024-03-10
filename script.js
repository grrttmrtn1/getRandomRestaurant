
$(document).ready(function(){
    $("#state").on("input", function(){
        if ($("#state").val().length != 2) {
            $("#error").text("Please use a 2 letter abbreviation for state");
        }
        else {
            statesArr = document.getElementById("states").innerHTML.split(',');
            inputState = document.getElementById("state").value;
            if (statesArr.indexOf(inputState.toUpperCase()) == -1) {
                $("#error").text("Hmm that state doesn't seem right");
            }
            else {
                $("#error").text(" ");
            }  
        }
    });
    $("#city").on("input", function(){
        citiesArr = document.getElementById("cities").innerHTML.split(',');
        inputCity= document.getElementById("city").value;
        inputCity = inputCity[0].toUpperCase() + inputCity.slice(1).toLowerCase()
        if (citiesArr.indexOf(inputCity) == -1) {
            $("#error").text("Hmm that city doesn't seem right");
        }
        else {
            $("#error").text(" ");
        }  
    });

    const button = document.getElementById('nextButton');
    button.addEventListener('click', function() {
    let resCookie = (document.cookie).split(`COOKIE_NAME=restaurants`).pop().split('restaurants=')[1] 
    jsonString = resCookie.slice(1, -1);
    jsonString = jsonString.replace(/\\"/g, '"').replace(/\\054/g, ','); 
    let jsonArray = JSON.parse(jsonString) 
    let table = '<table>';
        for (let key in jsonArray) {
        table += `<tr><th>${key}</th><td>${jsonArray[key]}</td></tr>`;
        }
    document.getElementsByClassName('table-hover')[0].innerHTML = "";
    document.getElementsByClassName('table-hover')[0].innerHTML = table;
    button.disabled = true;

    });


});

document.addEventListener('DOMContentLoaded', function() {
    const menuToggle = document.querySelector('.menu-toggle');
    const menu = document.querySelector('.menu');
    
    menuToggle.addEventListener('click', function() {
        menu.classList.toggle('active');
        menuToggle.classList.toggle('active');
    });
    
    // Close the menu when clicking outside of it
    document.addEventListener('click', function(event) {
        if (!menu.contains(event.target) && !menuToggle.contains(event.target)) {
            menu.classList.remove('active');
            menuToggle.classList.remove('active');
        }
    });
});


