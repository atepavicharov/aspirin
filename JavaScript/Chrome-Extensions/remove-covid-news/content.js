console.log("Chrome Corona extension is working.");
var listToCheck = [
    "ковид",
    "ковид-19",
    "коронавирус",
    "коронавирос",
    "вирус",
    "вируса",
    "вирос",
    "зараза",
    "заразен",
    "заразена",
    "заразени",
    "заразените",
    "карантина",
    "епидемия",
    "пандемия",
    "симптоми",
    "симптомите",
    "сзо",
    "инфекция",
    "инфекцията",
    "symptoms",
    "covid",
    "covid-19",
    "coronavirus",
    "outbreak",
    "patients",
    "corona",
    "quarantine",
    "epidemy",
    "pandemy",
    "virus",
    "disease",
    "lockdown",
    "stay-home"

];

var arrMaskedElements = [];

function checkContentForMatches(element) {
    var element_lower = element.innerHTML.toString().toLowerCase();
    for (let i = 0, l = listToCheck.length; i < l; i += 1) {
        if (element_lower.includes(listToCheck[i]))
            return true;
    }
    return false;
}

function refactor(element) {
    element.style['background-color'] = '#000000';
    element.style['color'] = '#000000';
}

function addToMaskedElementsArray(element) {
    if (!arrMaskedElements.includes(element)) {
        arrMaskedElements.push(element);
    }
}

function getMaskedElementsArrayItems() {
    for (let i = 0, l = arrMaskedElements.length; i < l; i += 1) {
        console.log(arrMaskedElements[i]);
    }
}

function maskShit() {

    console.log("maskShit() executed:");

    let titles = document.getElementsByTagName('h1');
    for (let elt of titles) {
        if (checkContentForMatches(elt)) {
            refactor(elt);
            addToMaskedElementsArray(elt);
        }
    }

    let paragraphs = document.getElementsByTagName('p');
    for (let elt of paragraphs) {
        if (checkContentForMatches(elt)) {
            refactor(elt);
            addToMaskedElementsArray(elt);
        }
    }

    let spans = document.getElementsByTagName('span');
    for (let elt of spans) {
        if (checkContentForMatches(elt)) {
            refactor(elt);
            //addToMaskedElementsArray(elt);
        }
    }

    let hrefs = document.getElementsByTagName('a');
    for (let elt of hrefs) {
        if (checkContentForMatches(elt)) {
            refactor(elt);
            addToMaskedElementsArray(elt);
        }
    }
}
;

// Build Stats Banner Body
// inject css/stats_bar.css
var style = document.createElement('link');
style.rel = 'stylesheet';
style.type = 'text/css'  ;
style.href = chrome.extension.getURL('css/stats_bar.css');
(document.head || document.documentElement).appendChild(style);

// inject stats banner
var divStats = document.createElement("div");
divStats.className = "stats_banner";
divStats.innerHTML = "&#x2622;&#xFE0F;<p id=\"match_counter\"></p>";
document.body.appendChild(divStats);

var divDyatlov = document.createElement("div");
divDyatlov.className = "dyatlov_banner";
divDyatlov.innerHTML = "<img class=\"dyatlov_banner\" src=\"" + chrome.extension.getURL('img/dyatlov_test.png') + "\">";
document.body.appendChild(divDyatlov);

// Trigger on page content load
maskShit(); //
document.getElementById("match_counter").innerHTML = arrMaskedElements.length;

window.addEventListener("load", function () {
    maskShit();
    document.getElementById("match_counter").innerHTML = arrMaskedElements.length;
});


// Trigger on Scroll (include throttling)
// https://developer.mozilla.org/en-US/docs/Web/API/Document/scroll_event
let ticking = false;

window.addEventListener('scroll', function () {     // scroll triggers the event
    if (!ticking) {
        window.requestAnimationFrame(function () {  // the only function to update ticking back to false - running asynch with the rest of the if
            maskShit();
            document.getElementById("match_counter").innerHTML = arrMaskedElements.length;
            ticking = false;
        });
        ticking = true;                             // maskShit() has started so ticking will remain true untill maskShit() is completed
    }
});
