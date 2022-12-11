<script>
import {inject} from "vue";
import {useLSWatcher} from "next-vue-storage-watcher";

export default {
    name: "blokCviceni",
    props: {
        cviceni: String
    },
    data() {
        return {
            ls: useLSWatcher(),
        }
    },
    methods: {
        prihlaste_se(){
            alert('Nejprve se prosím přihlašte')
        }
    },
    computed: {
        formatovany_pismena() {
            let vratit = "";
            for (let i = 0; i < this.cviceni.length; i++) {
                vratit += i < this.cviceni.length-1 ? this.cviceni.at(i) + ", " : this.cviceni.at(i);
            }
            return vratit;
        }
    }
}
</script>

<template>
    <div class="cviceniBlok">
        <h3>
            <router-link v-if="this.ls.getItem('token').value" :to="'/cvic/' + cviceni">Lekce: {{ formatovany_pismena }}</router-link>
            <a v-else @click="prihlaste_se">Lekce: {{ formatovany_pismena }}</a>
        </h3>
    </div>
</template>

<style scoped>
.cviceniBlok {
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
}
.cviceniBlok a {
    text-decoration: none;
    color: var(--bila);
    font-size: 1em;
    cursor: pointer;
}
</style>
