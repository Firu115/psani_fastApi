<script>
import axios from "axios";
import {inject} from "vue";
import router from "@/router";
import {useLSWatcher} from "next-vue-storage-watcher";

export default {
    name: "login",
    data() {
        return {
            jmeno_nebo_email: this.jmeno_nebo_email,
            heslo: this.heslo,
            info: "",
            ls: useLSWatcher()
        }
    },
    methods: {
        login(e) {
            e.preventDefault(); //aby se nerefreshla stranka

            axios
                .post('/prihlaseni', {
                    "jmeno_nebo_email": this.jmeno_nebo_email,
                    "heslo": this.heslo
                })
                .then(response => {
                    this.info = response
                    if (this.info.data.access_token) {
                        this.ls.setItem("token",this.info.data.access_token)
                        //localStorage.setItem("token", this.info.data.access_token)
                    } else {
                        console.log(this.info.data.access_token)
                    }
                    router.push("/ucet")
                })
        }
    }
}
</script>

<template>
    <h2>Přihlášení</h2>
    <form class="pruhledne">
        <h3 class="nadpis">Uživatelské jméno / email:</h3>
        <input type="text" v-model="jmeno_nebo_email" placeholder="Např: Pepa z depa / pepa@zdepa.cz">
        <h3 class="nadpis">Heslo:</h3>
        <input type="password" v-model="heslo" placeholder='Rozhodně ne "Pepa123"'>
        <button class="pruhledne" @click="login">Přihlásit</button>

    </form>
    <p>Nemáte ještě účet?
        <router-link to="/register">Registrace</router-link>
    </p>

</template>

<style scoped>
@import "@/assets/loginRegisterForma.css";
</style>
