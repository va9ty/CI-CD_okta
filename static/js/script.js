
function getinfo() {
	var ua_report_event = document.getElementById("user_analysis_report");
	console.log(ua_report_event)
	ua_report_event.style.display="inline-block";
}


function download()
{
	var d = document.getElementById("downloading");
	d.value= "Downloading ... ";
	
	var i = document.getElementById("icn");
	icn.style.display="none";
	var t = document.getElementById("loading");
	t.style.display="inline"; 
}
console.log("HEREEE",getinfo())
console.log("the", download())


