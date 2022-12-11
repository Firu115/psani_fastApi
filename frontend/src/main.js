import { createApp } from 'vue'
import App from '@/App.vue'
import router from '@/router'
import { createPinia } from 'pinia'

import '@/assets/main.css'

import GoogleSignInPlugin from "vue3-google-signin"
import { createWatcher }from 'next-vue-storage-watcher';

export const lsWatcher = createWatcher({
    prefix:"ls_"
})

const pinia = createPinia()
const app = createApp(App)

app.provide('API_URL','http://127.0.0.1:8000/')

app.use(GoogleSignInPlugin, {
  clientId: '873874261202-aekjikhkkkfnmbdo68crs8l8e252b7rf.apps.googleusercontent.com',
});

import axios from "axios";
axios.defaults.baseURL = "http://127.0.0.1:8000/";

app.use(pinia)
app.use(router)
app.use(lsWatcher)

app.mount('#app')