<template>
    <div id="klavesnice" class="pruhledne">
        <div class="radek" v-for="radek in schema">
            <div v-for="tlacitko in radek"
                 :class="{tlacitko: tlacitko.length <= 2, delsiTlacitko: tlacitko.length > 2, oznaceneTlacitko: oznacene(tlacitko)}">
                {{ tlacPismeno(0, tlacitko) }} <br> {{ tlacPismeno(1, tlacitko) }}
            </div>
        </div>
    </div>
</template>

<script>
import {h, toRef} from "vue";

export default {
    name: "Klavesnice",
    props: ["counter", "text"],
    data() {
        return {
            schema: [
                ["°;", "1+", "2ě", "3š", "4č", "5ř", "6ž", "7ý", "8á", "9í", "0é", "%=", "ˇ´", "Backspace"],
                ["TAB", "Q", "W", "E", "R", "T", "Z", "U", "I", "O", "P", "/ú", "()", "'¨"],
                ["CapsLock", "A", "S", "D", "F", "G", "H", "J", "K", "L", '"ů', "!§", "Enter"],
                ["Shift", "Y", "X", "C", "V", "B", "N", "M", "?,", ":.", "_-", "Shift"],
                ["Ctrl", "", "", "Alt", "SPACE", "AltGr", "", ""]
            ], delkaKlaves: {"Backspace": 1}
        }
    },
    setup(props) { // nevim jak to funguje ale zustane tak reaktivni
        const counter = toRef(props, 'counter')
        return {counter}
    },
    watch: {
        counter() {

        }
    },
    methods: {
        tlacPismeno(cislo, tlacitko) {
            if (tlacitko.length === 2) return tlacitko.at(cislo)
            else if (tlacitko.length === 1 && cislo === 0) return tlacitko.at(0)
            else if (tlacitko.length >= 2 && cislo === 0) return tlacitko
        },

        oznacene(tlacitko) {
            //console.log(this.text[this.counter])
            if (this.text[this.counter] === tlacitko.toLowerCase()) return true
        }
    }
}
</script>

<style scoped>
.oznaceneTlacitko {
    background-color: #FFFFFF;
}
.tlacitko {
    width: 40px;
    height: 40px;
    background-color: rgba(203, 203, 203, 0.25);
    border-radius: 5px;
    display: flex;
    justify-content: center;
    align-items: center;
}

.delsiTlacitko {
    width: 90px;
    height: 40px;
    background-color: rgba(203, 203, 203, 0.25);
    border-radius: 5px;
    display: flex;
    justify-content: center;
    align-items: center;
}

#klavesnice {
    display: flex;
    flex-direction: column;
    gap: 5px;
    background-color: var(--pruhledna);
    padding: 10px;
    border-radius: 10px;
    font-size: 0.8em;
    line-height: 1.3em;
    width: 650px;
    margin-top: 50px;
}

.radek {
    display: flex;
    gap: 5px;
}

</style>