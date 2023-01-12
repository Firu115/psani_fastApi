<script>
import {inject} from "vue";
import {useLSWatcher} from "next-vue-storage-watcher";
import axios from "axios";

export default {
    name: "Lekce",
    data() {
        return {
            pismena: this.$route["params"].pismena,
            ls: useLSWatcher(),
            info: {}
        }
    },
    methods: {
        prihlaste_se() {
            alert('Nejprve se prosím přihlašte')
        },
        index1(index) {
            return index + 1
        }
    },
    computed: {
        formatovany_pismena() {
            let vratit = "";
            for (let i = 0; i < this.pismena.length; i++) {
                vratit += i < this.pismena.length - 1 ? this.pismena.at(i) + ", " : this.pismena.at(i);
            }
            return vratit;
        },
    },
    mounted() {
        axios
            .get('api/lekce/' + this.pismena, {
                headers: {
                    Authorization: 'Bearer ' + this.ls.getItem('token').value
                }
            })
            .then(response => {
                this.info = response.data
            });
    },
}
</script>

<template>
    <div class="kontejnr" v-if="!info.error">
        <div v-if="info.length !== 0" v-for="(cviceni, index) in info['cviceni']">
            <h2>
                <router-link class="lekceBlok" v-if="cviceni[1]" :to="'/lekce/' + pismena + '/' + index1(index)">
                    <h2>{{ index + 1 }} - {{ formatovany_pismena }}</h2>
                    <img class="fajvkaMensi" v-if="index in info['dokonceno']" src="@/assets/icony/right.svg" alt="Dokonceno!">
                </router-link>
                <router-link v-else class="lekceBlok" :to="'/lekce/' + pismena + '/' + index1(index)">
                    <h2>{{ index + 1 }} - Se slovy</h2>
                    <img class="fajvkaMensi" v-if="index in info['dokonceno']" src="@/assets/icony/right.svg" alt="Dokonceno!">
                </router-link>
            </h2>
        </div>
        <p v-else>Tato lekce zatím nemá žádná cvičení</p>
    </div>
    <p v-else>{{ info.error }}</p>


</template>

<style scoped>
.kontejnr {
    display: flex;
    gap: 15px;
}

.lekceBlok {
    color: var(--bila);
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    padding: 12px 12px 12px 25px;
    text-decoration: none;
    border-radius: 10px;
    min-width: 220px;
    background-color: var(--pruhledna);
    backdrop-filter: blur(15px);
    -webkit-backdrop-filter: blur(15px);
    height: 56px;
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

.lekceBlok a {
    text-decoration: none;
    color: var(--bila);
    cursor: pointer;
}
</style>
