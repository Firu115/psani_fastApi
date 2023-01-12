<script>
import {inject} from "vue";
import {useLSWatcher} from "next-vue-storage-watcher";

export default {
    name: "blokLekce",
    props: {
        pismena: String,
        je_dokonceno: Boolean,
        cislo: String
    },
    data() {
        return {
            ls: useLSWatcher(),
        }
    },
    methods: {
        prihlaste_se() {
            alert('Nejprve se prosím přihlašte')
        }
    },
    computed: {
        formatovany_pismena() {
            let vratit = "";
            for (let i = 0; i < this.pismena.length; i++) {
                vratit += i < this.pismena.length - 1 ? this.pismena.at(i) + ", " : this.pismena.at(i);
            }
            return vratit;
        }
    }
}
</script>

<template>
    <router-link class="lekceBlok" v-if="this.ls.getItem('token').value" :to="'/lekce/' + pismena">
        <h2>Lekce: {{ formatovany_pismena }}</h2>
        <img class="fajvka" v-if="je_dokonceno" src="@/assets/icony/right.svg" alt="Dokonceno!">
    </router-link>
    <a v-else class="lekceBlok" @click="prihlaste_se"><h2>Lekce: {{ formatovany_pismena }}</h2></a>
</template>

<style scoped>
.lekceBlok {
    color: var(--bila);
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    padding: 12px 12px 12px 25px;
    text-decoration: none;
    border-radius: 10px;
    min-width: 500px;
    background-color: var(--pruhledna);
    backdrop-filter: blur(15px);
    -webkit-backdrop-filter: blur(15px);
    height: 64px;
    transition-duration: 0.2s;
}

.lekceBlok:hover {
    background-color: var(--mene-pruhledna);
    transition-duration: 0.2s;
}

.lekceBlok h2 {
    align-self: center;
    font-size: 24px;
}
</style>
