import Vue from 'vue';
import Router from 'vue-router';
import Lobby from './components/Lobby.vue';

Vue.use(Router);

export default new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/',
            component: Lobby,
        },
        {
            path: '/game',
            component: () => import('./components/Game.vue')
        },
    ],
});