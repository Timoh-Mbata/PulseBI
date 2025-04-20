import { createApp } from 'vue';
import App from './App.vue';
import router from './routes/route'; 
import { createHead } from '@vueuse/head';
const app = createApp(App);
const head = createHead()
app.use(router).use(head);
app.mount('#app');
