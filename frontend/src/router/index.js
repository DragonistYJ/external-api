import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        redirect: '/menu'
    }, {
        path: '/menu',
        name: 'Menu',
        component: () => import('../views/Menu')
    }, {
        path: '/domain',
        name: 'Domain',
        component: () => import('../views/Domain')
    }, {
        path: '/ip',
        name: 'IP',
        component: () => import('../views/Ip')
    }, {
        path: '/url',
        name: 'URL',
        component: () => import('../views/URL')
    }
]

const router = new VueRouter({
    routes
})

export default router
