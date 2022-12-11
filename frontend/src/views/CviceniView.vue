<script>
import blokCviceni from "@/components/BlokCviceni.vue";
import axios from "axios";
import {useLSWatcher} from "next-vue-storage-watcher";

export default {
    name: "cviceni",
    data() {
        return {
            info: {},
            cas: 10,
            pismena: this.$route.params.pismena,
            ls: useLSWatcher()
        }
    },
    mounted() {
        axios
            .get('cvic/' + this.pismena, {
                headers: {
                    Authorization: 'Bearer ' + this.ls.getItem('token').value
                }
            })
            .then(response => (this.info = response.data));
    },
    methods: {
        plus() {
            this.pismena += "k"
        }
    }
}
</script>

<template>
    <h1>Lekce: {{ pismena }}</h1>

    <div v-if="!info.error">

        <div id="cviceniNabidka">
            <h2 id="cas">Čas</h2>
            <h2 id="CapsLock"></h2>
        </div>

        <div id="ramecek">
            <div id="text">
                <div class="slova" v-for="(slovo, i) in info.text">
                    <div v-for="(pismeno, j) in slovo">
                        <p class="pismena" :id="'p' + (i * slovo.length + j)">{{(pismeno !== ' ' ? pismeno : "&nbsp") }}</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <p v-else>{{info.error}}</p>
</template>

<style>
#text {
    display: flex;
    flex-wrap: wrap;
    line-height: normal;
}

.slova {
    display: flex;
    flex-wrap: nowrap;
}

.pismena {
    border-radius: 3px;
    display: inline-flex;
    font-family: Menlo, Monaco, Consolas, Courier New, monospace;
    font-size: 25px;
    line-height: 1.5;
    text-decoration: none;
    padding-left: 2px;
}

#ramecek {
    border-radius: 10px;
    padding: 10px;
    width: 650px;
    height: 200px;

    background-color: var(--pruhledna);
    backdrop-filter: blur(15px);
    -webkit-backdrop-filter: blur(15px);
}

.podtrzenePismeno {
    border-bottom: 3px solid var(--bila);
    border-radius: 0px;
}

.spatnePismeno {
    background-color: red;
    border-radius: 3px 3px 0px 0px;
}

.opravenePismeno {
    background-color: gray;
}
</style>
