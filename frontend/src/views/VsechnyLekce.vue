<script>
import axios from 'axios';
import BlokLekce from "@/components/BlokLekce.vue";
import {inject} from "vue";
import {useLSWatcher} from "next-vue-storage-watcher";
import router from "@/router";

export default {
    name: "VsechnyLekce",
    data() {
        return {
            info: {},
            ls: useLSWatcher(),
        }
    },
    components: {
        BlokLekce
    },
    mounted() {
        axios
            .get('api/lekce', {
                headers: {
                    Authorization: 'Bearer ' + this.ls.getItem('token').value
                }
            })
            .then(response => {
                this.info = response.data
            })
    },
}
</script>

<template>
    <div id="lekce">
        <BlokLekce v-for="(pismena, cislo) in info.lekce" :pismena="pismena" :cislo="cislo"
                   :je_dokonceno="info.dokoncene.includes(parseInt(cislo))"/>
    </div>

</template>

<style scoped>
#lekce {
    display: flex;
    flex-direction: column;
    gap: 20px;
    text-align: left;
    height: 3000%;
}
</style>