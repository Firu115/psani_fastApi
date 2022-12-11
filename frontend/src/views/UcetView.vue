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
            .get('/ja', {
                headers: {
                    Authorization: 'Bearer ' + this.ls.getItem('token').value
                }
            })
            .then(response => {
                this.info = response.data
            })
    }
}
</script>

<template>
    <h1>{{ this.info.jmeno }}</h1>
    <h2>{{ this.info.email }}</h2>
    <button @click="odhlasit">Odhlásit</button>
</template>

<style scoped>

</style>