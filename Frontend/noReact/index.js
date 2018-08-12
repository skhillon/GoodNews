//Created by Siddharth Khillon, July 2018
var TEST_URL = "localhost:8000/"
var PROD_URL = "goodnews.space/"

var urlParams = new URLSearchParams(window.location.search);

var getJSONWeb = function(url, callback) {
	var request = new XMLHttpRequest();
	request.open('GET', url, true);
	request.responseType = "json";
    request.onload = function () {
        let status = (request.status == 200) ? request.status : null;
        callback(status, request.response);
	}
	request.send();
};


console.log(urlParams.get("category"));

/*
//How to use it example
var JSONtext = getJSONWeb()
function(err, data) {
  if (err !== null) {
    alert('Something went wrong: ' + err);
  } else {
    alert('Your query count: ' + data.query.count);
  }
  console.log(data);
});*/

//Pretend we have the json
//comment line directly below if wanting to use url above
var JSONtext = `[{"title": "U.S. lifts ban on suppliers selling to China's ZTE med", "url": "https://www.reuters.com/article/us-usa-trade-china-zte/us-lifts-ban-on-suppliers-selling-to-chinas-zte-idUSKBN1K32CN", "publisher": "Reuters", "category": "m", "timestamp": 1394470370698}, {"title": "U.S. lifts ban on suppliers selling to China's ZTE bus", "url": "https://www.reuters.com/article/us-usa-trade-china-zte/us-lifts-ban-on-suppliers-selling-to-chinas-zte-idUSKBN1K32CN", "publisher": "Reuters", "category": "b", "timestamp": 1394470370698}]`
var data = JSON.parse(JSONtext);

//Data is parsed
console.log(data);
function loadDataToWebpage(category){
	var noCategory = (category == null);
    console.log(noCategory);
	document.getElementById("mainPageGrid").innerHTML = "";
    for (let i = 0; i < data.length; i++){
		console.log(data[i]);
		console.log(data[i]["category"])
		console.log(category)
		console.log(data[i]["category"] != category)
		if (data[i]["category"] != category && category != null) {
			console.log("continued")
			continue;
		}

		var date = new Date(parseInt(data[i]["timestamp"]));
		console.log(date.customFormat( "#DD#/#MM#/#YYYY# #hh#:#mm#:#ss#"));
		document.getElementById("mainPageGrid").innerHTML += `
					<div class="mdl-card mdl-cell mdl-cell--6col">
		  	  			<div class="mdl-card__title">
						    <h4 class="mdl-card__title-text">${data[i]["title"]}</h4>
						  </div>
						  <div class="mdl-card__supporting-text">
						    ${data[i]["publisher"]} ${date.customFormat( "#DD#/#MM#/#YYYY# #hh#:#mm#:#ss#")}
						  </div>
						  <div class="mdl-card__actions mdl-card--border">
						    <a href="${data[i]["url"]}">
						      Go to article
						    </a>
						  </div>
						  <div class="mdl-card__menu">
						  </div>
		  	  		</div>`;
	}

}



//*** This code is copyright 2002-2016 by Gavin Kistner, !@phrogz.net
//*** It is covered under the license viewable at http://phrogz.net/JS/_ReuseLicense.txt
Date.prototype.customFormat = function(formatString){
	var YYYY,YY,MMMM,MMM,MM,M,DDDD,DDD,DD,D,hhhh,hhh,hh,h,mm,m,ss,s,ampm,AMPM,dMod,th;
	var dateObject = this;
	YY = ((YYYY=dateObject.getFullYear())+"").slice(-2);
	MM = (M=dateObject.getMonth()+1)<10?('0'+M):M;
	MMM = (MMMM=["January","February","March","April","May","June","July","August","September","October","November","December"][M-1]).substring(0,3);
	DD = (D=dateObject.getDate())<10?('0'+D):D;
	DDD = (DDDD=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"][dateObject.getDay()]).substring(0,3);
	th=(D>=10&&D<=20)?'th':((dMod=D%10)==1)?'st':(dMod==2)?'nd':(dMod==3)?'rd':'th';
	formatString = formatString.replace("#YYYY#",YYYY).replace("#YY#",YY).replace("#MMMM#",MMMM).replace("#MMM#",MMM).replace("#MM#",MM).replace("#M#",M).replace("#DDDD#",DDDD).replace("#DDD#",DDD).replace("#DD#",DD).replace("#D#",D).replace("#th#",th);

	h=(hhh=dateObject.getHours());
	if (h==0) h=24;
	if (h>12) h-=12;
	hh = h<10?('0'+h):h;
  hhhh = hhh<10?('0'+hhh):hhh;
	AMPM=(ampm=hhh<12?'am':'pm').toUpperCase();
	mm=(m=dateObject.getMinutes())<10?('0'+m):m;
	ss=(s=dateObject.getSeconds())<10?('0'+s):s;
	return formatString.replace("#hhhh#",hhhh).replace("#hhh#",hhh).replace("#hh#",hh).replace("#h#",h).replace("#mm#",mm).replace("#m#",m).replace("#ss#",ss).replace("#s#",s).replace("#ampm#",ampm).replace("#AMPM#",AMPM);
}

function remove_qs(url) {
    var a = document.createElement('a'); // dummy element
    a.href = url;   // set full url
    a.search = "";  // blank out query string
    return a.href;
}

window.onload = function() {
	loadDataToWebpage(urlParams.get("category"));
}

