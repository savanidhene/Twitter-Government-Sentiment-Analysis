function initial() {
    document.getElementById("line1").className = "showLine1";
    document.getElementById("line2").className = "hideLine2";
    document.getElementById("line3").className = "hideLine3";

}

window.onscroll = function() {
    ShowNextPart()
};

function ShowNextPart() {
    if ((document.body.scrollTop > 200 && document.body.scrollTop < 700) || (document.documentElement.scrollTop > 200 && document.documentElement.scrollTop < 700)) {
        document.getElementById('line2').className = "showLine2";
        document.getElementById("line1").className = "hideLine1";
        document.getElementById("line3").className = "hideLine3";
    } else if (document.body.scrollTop > 700 || document.documentElement.scrollTop > 700) {
        document.getElementById("line3").className = "showLine3";
        document.getElementById("line1").className = "hideLine1";
        document.getElementById("line2").className = "hideLine2";
    } else {
        document.getElementById("line1").className = "showLine1";
        document.getElementById("line2").className = "hideLine2";
        document.getElementById("line3").className = "hideLine3";
    }
    // if (document.body.scrollTop > 1000 || document.documentElement.scrollTop > 1000) {
    //     document.getElementById("line3", "line1").className = "showLine3";
    //     document.getElementById("line1").className = "hideLine1";
    // }
    //  else {
    //     document.getElementById("line3").className = "";
    // }
}