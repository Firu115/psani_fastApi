<script>
import router from "@/router";
import axios from "axios";
import {useLSWatcher} from "next-vue-storage-watcher";

export default {
    name: "ucet",
    data() {
        return {
            info: "",
            ls: useLSWatcher()
        }
    },
    methods: {
        odhlasit() {
            this.ls.setItem('token', "")
            router.push("/")
        }
    },
    mounted() {
        axios
            .get('api/ja', {
                headers: {
                    Authorization: 'Bearer ' + this.ls.getItem('token').value
                }
            })
            .then(response => {
                this.info = response.data
            })
            .catch(function (e) { //nebudeš tam chodit nemas ucet more
                router.push("/")
            })
    }
}
</script>

<template>
    <h1>{{ info.jmeno }}</h1>
    <h2>{{ info.email }}</h2>
    <h2>Dokonceno: {{ info.dokonceno }}%</h2>
    <h2>Rychlost: {{ info.prumerna_rychlost }}%</h2>
    <h2>Přesnost: {{ info.prumerna_presnost }}%</h2>

    <button @click="odhlasit">Odhlásit</button>
</template>

<style scoped>

</style>