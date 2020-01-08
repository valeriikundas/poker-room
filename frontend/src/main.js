import 'bootstrap/dist/css/bootstrap.css';
import BootstrapVue from 'bootstrap-vue';
import Vue from 'vue'
import App from './App.vue'
import router from './router';
import axios from 'axios';

Vue.use(BootstrapVue);

Vue.config.productionTip = false;

const API_URL = process.env.API_URL || 'http://localhost:5000'

export default axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': "application/json",
    'Authorization': 'Token'
  }
})



new Vue({
  router, render: h => h(App), axios
}).$mount('#app')
