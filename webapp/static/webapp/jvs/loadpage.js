console.log("loadpage.js")
var before_loadtime = new Date().getTime();
window.onload = Pageloadtime;
    function Pageloadtime() {  
        var aftr_loadtime = new Date().getTime();  
        pgloadtime = (aftr_loadtime - before_loadtime) / 1000;
        let loadTime = document.getElementById("loadtime");
        console.log("@")
        console.log(loadTime)
        document.getElementById("loadtime").innerHTML = "<font color='black'><b>" + pgloadtime + "</b></font> seconds";  
    }