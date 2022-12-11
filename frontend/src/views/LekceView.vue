<script>
import axios from 'axios';
import BlokCviceni from "@/components/BlokCviceni.vue";
import {inject} from "vue";

export default {
    name: "lekce",
    data() {
        return {
            info: "",
        }
    },
    components: {
        BlokCviceni
    },
    mounted() {
        axios
            .get('lekce/')
            .then(response => (this.info = response))
    },
}
</script>

<template>
    <div id="lekce">
        <BlokCviceni v-for="(pismena) in info.data" :cviceni="pismena"/>
    </div>
</template>

<style scoped>
#lekce {
    display: flex;
    flex-direction: column;
    gap: 20px;
    text-align: left;
}
</style>