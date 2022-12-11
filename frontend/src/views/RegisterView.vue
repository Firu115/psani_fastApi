<script>
import axios from "axios";
import router from "@/router";

export default {
    name: "register",
    data() {
        return {
            email: this.email,
            heslo: this.heslo,
            jmeno: this.jmeno,
            spatny_jmeno: false,
            spatnej_email: false,
            spatny_heslo: false,
        }
    },
    methods: {
        registr(e) {
            e.preventDefault(); //aby se nerefreshla stranka

            if (this.heslo === undefined) this.spatny_heslo = true
            if (this.email === undefined) this.spatnej_email = true
            if (this.jmeno === undefined) this.spatny_jmeno = true

            if (this.spatnej_email || this.spatny_heslo || this.spatny_jmeno) return;

            axios
                .post('/registrace', {
                    "jmeno": this.jmeno,
                    "email": this.email,
                    "heslo": this.heslo
                })
                .then(response => {
                    this.info = response
                    if (this.info.data.access_token) {
                        localStorage.setItem("token", this.info.data.access_token)
                    } else {
                        console.log(this.info.data.access_token)
                    }
                    this.global.prihlasen = true
                    router.push("/ucet")
                })
        },
        chekuj_udaje(jaky) {
            if (jaky === 'email' && this.email !== undefined) this.spatnej_email = !/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(this.email); //test jestli email
            else if (jaky === 'heslo' && this.heslo !== undefined) this.spatny_heslo = !/^(?=.*[0-9])(?=.*[!@#$%^&*_])[a-zA-Z0-9!@#$%^&*_]{8,20}$/.test(this.heslo) //heslo 8-20 aspon jeden CAPS a *_!
            else if (jaky === 'jmeno' && this.jmeno !== undefined) this.spatny_jmeno = !/^[a-zA-Z0-9!@#$%^&*_ ]{3,25}$/.test(this.jmeno) //jmeno 3-25
        },
        open_info() {
            document.getElementsByClassName('info')[0].id = 'info_show';
        },
        close_info() {
            document.getElementsByClassName('info')[0].id= 'info_out';
        }
    }
}
</script>

<template>
    <h2>Registrace</h2>
    <form class="pruhledne">
        <h3 class="nadpis">Uživatelské jméno:</h3>
        <input :class="{spatnej_input: spatny_jmeno}" :oninput="chekuj_udaje('jmeno')" type="text" v-model="jmeno"
               placeholder="Např: Pepa z depa">
        <h3 class="nadpis">Email:</h3>
        <input :class="{spatnej_input: spatnej_email}" :oninput="chekuj_udaje('email')" type="text" v-model="email"
               placeholder="Např: pepa@zdepa.cz">
        <h3 class="nadpis">Heslo: <img src="@/assets/icony/info.svg" alt="info" @mouseover="open_info" @mouseleave="close_info"></h3>
        <input :class="{spatnej_input: spatny_heslo}" :oninput="chekuj_udaje('heslo')" type="text" v-model="heslo"
               placeholder='Rozhodně ne "Pepa123"'>
        <button class="pruhledne" @click="registr">Registrovat</button>
    </form>
    <div id="info_out" class="info">
        Heslo musí obsahovat:
        <ul>
            <li>Minimálně 8 znaků</li>
            <li>Alespoň jeden speciální znak (!@#$%^&*_)</li>
            <li>Alespoň jedna číslice</li>
        </ul>
    </div>

    <p>Máte už účet?
        <router-link to="/login">Přihlášení</router-link>
    </p>

</template>

<style scoped>
@import "@/assets/loginRegisterForma.css";

</style>
