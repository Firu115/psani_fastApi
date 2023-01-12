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
            ls: useLSWatcher(),
            spatnej_uzivatel: false,
            spatny_heslo: false,
        }
    },
    methods: {
        login(e) {
            e.preventDefault(); //aby se nerefreshla stranka

            if (!this.heslo) { //pokud uzivatel nic nenapsal
                this.spatny_heslo = true
            }
            if (!this.jmeno_nebo_email) {
                this.spatnej_uzivatel = true
            }
            if (this.spatnej_uzivatel || this.spatny_heslo) return //nezkoušet ani

            axios
                .post('api/prihlaseni', {
                    "jmeno_nebo_email": this.jmeno_nebo_email,
                    "heslo": this.heslo
                })
                .then(response => {
                    this.info = response
                    if (this.info.data.access_token) {
                        this.ls.setItem("token", this.info.data.access_token)
                        router.push("/ucet")
                    } else {
                        if (this.info.data.error === "Špatný uživatel") this.spatnej_uzivatel = true
                        else if (this.info.data.error === "Špatné heslo") this.spatny_heslo = true
                    }
                })

        },
        zmenaUziv() { // pokud zacnu znova psat tak zrusim znaceni spatnyho inputu
            this.spatnej_uzivatel = false
        },
        zmenaHeslo() {
            this.spatny_heslo = false
        }
    }
}
</script>

<template>
    <h2>Přihlášení</h2>
    <form class="pruhledne">
        <h3 class="nadpis">Uživatelské jméno / email:</h3>
        <input :class="{spatnej_input: spatnej_uzivatel}" :oninput="this.zmenaUziv" type="text"
               v-model="jmeno_nebo_email" placeholder="Např: Pepa z depa / pepa@zdepa.cz">
        <h3 class="nadpis">Heslo:</h3>
        <input :class="{spatnej_input: spatny_heslo}" :oninput="this.zmenaHeslo" type="password" v-model="heslo"
               placeholder='Rozhodně ne "Pepa123"'>
        <button class="pruhledne" @click="login">Přihlásit</button>

    </form>
    <p>Nemáte ještě účet?
        <router-link to="/register">Registrace</router-link>
    </p>

</template>

<style scoped>
@import "@/assets/loginRegisterForma.css";
</style>
