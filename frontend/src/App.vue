<script>
import {RouterLink, RouterView} from 'vue-router'
import { useLSWatcher } from "next-vue-storage-watcher";


export default {
    name: 'app',
    data() {
        return {
            ls: useLSWatcher()
        }
    },
}
</script>

<template>
    <header>
        <nav class="pruhledne">
            <RouterLink to="/">
                <svg class="dot" height="10" width="15">
                    <circle cx="5" cy="5" r="5" fill="white"/>
                </svg>
                Domů
            </RouterLink>
            <RouterLink to="/lekce">
                <svg class="dot" height="10" width="15">
                    <circle cx="5" cy="5" r="5" fill="white"/>
                </svg>
                Lekce
            </RouterLink>
            <RouterLink to="/about">
                <svg class="dot" height="10" width="15">
                    <circle cx="5" cy="5" r="5" fill="white"/>
                </svg>
                O nás
            </RouterLink>
            <RouterLink v-if="ls.getItem('token').value" to="/ucet">
                <svg class="dot" height="10" width="15">
                    <circle cx="5" cy="5" r="5" fill="white"/>
                </svg>
                Můj účet
            </RouterLink>
            <RouterLink v-else to="/login">
                <svg class="dot" height="10" width="15">
                    <circle cx="5" cy="5" r="5" fill="white"/>
                </svg>
                Přihlásit se
            </RouterLink>
        </nav>
    </header>

    <img id="pavouk" src="@/assets/icony/pavouk.png" alt="Pavouk">

    <div id="kontent">
        <RouterView/>
    </div>

</template>

<style scoped>
@import '@/assets/main.css';

#pavouk {
    position: absolute;
    left: 120px;
    width: 100px;
    pointer-events: none;
}

#kontent {
    padding-top: 20px;
    margin-left: var(--sirka-menu);
    height: 100%;
    margin-bottom: 50px;
    text-align: center;
    width: 720px;
    display: flex;
    flex-direction: column;
    align-items: center;
}

nav {
    position: fixed;
    left: 10px;
    top: 10px;
    width: var(--sirka-menu);
    height: calc(100vh - 20px);
    flex-shrink: 0;
    border-radius: 10px;
}

nav a {
    color: var(--bila);
    display: block;
    padding: 15px;
    text-decoration: none;
    cursor: pointer;
}

nav a:hover {
    backdrop-filter: blur(30px);
    -webkit-backdrop-filter: blur(30px);
    background-color: var(--mene-pruhledna);
    border-radius: 8px;
    margin: 5px;
    padding: 10px;
    width: calc(var(--sirka-menu) - 10px);
    transition: background-color 0.2s, backdrop-filter 0.2s;
}

.dot {
    display: none;
}

.router-link-active .dot {
    display: inline-block;
    margin-bottom: 1px;
}

div { /* google button */
    padding: 10px 15px 15px 15px;
}
</style>
