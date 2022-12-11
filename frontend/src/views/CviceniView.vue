<script>
import blokCviceni from "@/components/BlokCviceni.vue";
import axios from "axios";
import {useLSWatcher} from "next-vue-storage-watcher";

export default {
    name: "cviceni",
    data() {
        return {
            info: {},
            text: String,
            cas: [0, 0],
            pismena: this.$route["params"].pismena,
            ls: useLSWatcher(),
            counter: 0,     //         0             1                2
            list_textu: {}, // {str pismeno, bool aktivni, bool je/bylo_spatne}
            timer_zacatek: null,
        }
    },
    computed: {
        cas_format() {
            return this.cas[0] === 0 ? this.cas[1] : `${this.cas[0]}:${this.cas[1]}`;
        },
        progress() {
            return Math.floor(((this.counter) / Object.keys(this.list_textu).length) * 100)
        },
        preklepy() {

            let pocet = 0
            for (const [key, value] of Object.entries(this.list_textu)) {
                if (value[2]) pocet++
            }
            return pocet
        }
    },
    mounted() {
        axios
            .get('cvic/' + this.pismena, {
                headers: {
                    Authorization: 'Bearer ' + this.ls.getItem('token').value
                }
            })
            .then(response => {
                this.info = response.data
                let pismenoCount = 0
                for (const slovo in this.info.text) {
                    for (const pismeno in this.info.text[slovo]) {
                        this.list_textu[pismenoCount] = [this.info.text[slovo][pismeno], false, false];
                        pismenoCount++
                    }
                }
                this.list_textu[0][1] = true //prvni pismeno podtrhu
            });
        document.addEventListener("keydown", this.klik);
    },
    unmounted() {
        document.removeEventListener("keydown", this.klik)
    },
    methods: {
        klik(e) {
            if (["Shift"].includes(e.key)) return
            if (!this.timer_zacatek) {
                this.timer_zacatek = new Date().getTime();
                setInterval(() => {
                    this.cas[1]++
                    if (this.cas[1] === 60) {
                        this.cas[1] = 0
                        this.cas[0]++
                    }
                }, 1000);
            }
            if (e.key === this.list_textu[this.counter][0]) {
                if (this.counter === this.list_textu.length - 1) {
                    //presmerovat
                    //window.location.href = "/update/" + cas + "/" + preklepy + "/" + (((delkaTextu - preklepy) / delkaTextu * 100).toFixed(1)).toString() + "/" + (kliknuti / (cas / 60)).toFixed(1).toString();
                }
                this.dalsi()
            } else {
                this.list_textu[this.counter][2] = true
            }
        },
        dalsi() {
            this.list_textu[this.counter][1] = false
            this.counter++
            this.list_textu[this.counter][1] = true
        },
        get_index_pismena(i, j) {
            let index = j
            for (let k = 0; k < i; k++) {
                index += this.info.text[k].length
            }
            return index
        }
    }
}
</script>

<template>
    <h1>Lekce: {{ pismena }}</h1>

    <div v-if="!info.error">

        <div id="cviceniNabidka">
            <h2 id="cas">Čas: {{ cas_format }}s</h2>
            <h2 id="preklepy">Překlepy: {{ preklepy }}</h2>
            <h2 id="CapsLock"></h2>
        </div>
        <div id="pozadi_ramecku">
            <div id="ramecek">
                <div id="text">
                    <div class="slovo" v-for="(slovo, i) in info.text">
                        <div v-for="(pismeno, j) in slovo">
                            <p class="pismeno"
                               :class="{podtrzenePismeno: this.list_textu[get_index_pismena(i,j)][1],
                                    spatnePismeno: this.list_textu[get_index_pismena(i,j)][2] && this.counter <= (get_index_pismena(i,j)),
                                    opravenePismeno: this.list_textu[get_index_pismena(i,j)][2] && this.counter > (get_index_pismena(i,j))}"
                               :id="'p' + (i * slovo.length + j)">{{
                                    (pismeno !== ' ' ? pismeno : "&nbsp")
                                }}</p>
                        </div>
                    </div>
                </div>
            </div>
            <div :style="'width:' + progress + '%; border-bottom-right-radius:' + (progress === 100 ? '10px':'0')"
                 id="progress_bar">Postup:&nbsp{{ progress }}%
            </div>
        </div>
    </div>
    <p v-else>{{ info.error }}</p>
</template>

<style>
#cviceniNabidka {
    margin-bottom: 20px;
}

#text {
    display: flex;
    flex-wrap: wrap;
}

.slovo {
    display: flex;
    flex-wrap: nowrap;
}

.pismeno {
    border-radius: 3px;
    display: inline-flex;
    font-family: Menlo, Monaco, Consolas, Courier New, monospace;
    font-size: 25px;
    line-height: 1.2;
    text-decoration: none;
    padding: 0 1px;
    margin-right: 1px;
    border-bottom: 3px solid rgba(255, 255, 255, 0); /* aby se nedojebala vyska liny když jdu na dalsi radek*/
}

#ramecek {
    padding: 10px 10px 0 10px;
    width: 650px;
    height: 200px;
}

#pozadi_ramecku {
    border-radius: 10px;
    background-color: var(--pruhledna);
    backdrop-filter: blur(15px);
    -webkit-backdrop-filter: blur(15px);
}

#progress_bar {
    height: 20px;
    background-color: rgba(101, 60, 253, 0.5);
    width: 0;
    border-bottom-left-radius: 10px;
    transition: ease 0.5s;
}

.podtrzenePismeno {
    border-bottom: 3px solid var(--bila);
    border-radius: 0;
}

.spatnePismeno {
    background-color: red;
    border-radius: 3px 3px 0px 0px;
}

.opravenePismeno {
    background-color: gray;
}
</style>
