export function klik(event) {
    kliknuti++;

    if (!timer_start) {
        zacatek = new Date().getTime();
        timer_start = true;
        cas.innerHTML = Math.floor(((new Date().getTime() - zacatek) % (1000 * 60)) / 1000) + " s";
        setInterval(function () {
            cas.innerHTML = Math.floor(((new Date().getTime() - zacatek) % (1000 * 60)) / 1000) + " s";
        }, 1000);
    }

    const element = document.getElementById("p" + ukazatel);

    if (event.key == element.innerHTML || (event.key == " " && element.innerHTML == "&nbsp;")) {
        if (ukazatel == delkaTextu-1) {
            document.removeEventListener('keydown', klik);
            document.getElementById("p" + ukazatel).classList.remove("podtrzenePismeno");
            var scripts = document.getElementsByTagName('script');
            cas = Math.floor(((new Date().getTime() - zacatek) % (1000 * 60)) / 1000);
            window.location.href = "/update/" + scripts[scripts.length - 2].getAttribute("pismena") + "/" + cas + "/" + preklepy + "/" + (((delkaTextu - preklepy) / delkaTextu * 100).toFixed(1)).toString() + "/" + (kliknuti / (cas / 60)).toFixed(1).toString();
        };
        if (element.classList.contains("spatnePismeno")) {
            element.classList.remove("spatnePismeno");
            element.classList.add("opravenePismeno");
            element.classList.remove("podtrzenePismeno")
            ukazatel++;
            document.getElementById("p" + ukazatel).classList.add("podtrzenePismeno");
        } else {
            element.classList.remove("podtrzenePismeno");
            ukazatel++;
            document.getElementById("p" + ukazatel).classList.add("podtrzenePismeno");
        }

        if (typ == "pohadka") {
            if (element.getBoundingClientRect().y < document.getElementById("p" + ukazatel).getBoundingClientRect().y) {
            scroll_y += vyskaPismena;
            //scroll(0, scroll_y);
            scroll({
                top: scroll_y,
                behavior: 'smooth'
            });
            } else {
                scroll({
                    top: scroll_y,
                    behavior: 'smooth'
                });
            }
        }

    } else if (event.shiftKey) {

    } else {
        element.classList.add("spatnePismeno");
        preklepy++;
    };
}

function caps(event) {
    if (event.getModifierState('CapsLock')) {
        document.getElementById("CapsLock").innerHTML = "Caps lock je zapnutý!"
    } else {
        document.getElementById("CapsLock").innerHTML = ""
    }
}

let kontejner = document.getElementById("textKontejner")
let ukazatel = 0;
let delkaTextu = document.getElementById("text").getAttribute("data-length");

let timer_start = false;
let cas = document.getElementById("cas");

let preklepy = 0;
let kliknuti = 0;
var zacatek;

var vyskaPismena = document.getElementById("p0").clientHeight;

var scroll_y = 0;
var typ = document.getElementById("text").getAttribute("typ");

document.addEventListener('keydown', klik);
document.addEventListener('keydown', caps);
window.addEventListener('keyup', caps)

window.addEventListener('keydown', (e) => {
    if (e.keyCode === 32 && e.target === document.body) {
      e.preventDefault();
    }
});



/*(function () { //refresh když jde zpět
    window.onpageshow = function (event) {
        if (event.persisted) {
            window.location.reload();
        }
    };
})(); */