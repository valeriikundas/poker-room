import 'bootstrap/dist/css/bootstrap.css';
import BootstrapVue from 'bootstrap-vue';
import Vue from 'vue'
import App from './App.vue'
import VueResource from 'vue-resource'
import router from './router';

Vue.use(BootstrapVue);
Vue.use(VueResource);

Vue.http.options.root = "http://localhost:5000/";

Vue.config.productionTip = false;


new Vue({
  router, render: h => h(App),
}).$mount('#app')
