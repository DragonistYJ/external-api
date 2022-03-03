import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import axios from 'axios'

let axiosInstance = axios.create({
    baseURL: process.env.NODE_ENV === 'production' ? "http://localhost:5000" : "/backend",
    timeout: 60000
});


Vue.prototype.$axios = axiosInstance;
Vue.config.productionTip = false
Vue.use(ElementUI);


new Vue({
    router,
    store,
    render: h => h(App)
}).$mount('#app')
