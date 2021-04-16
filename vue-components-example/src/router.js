import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Contact from './views/Contact.vue'

Vue.use(Router)

export default new Router({
  mode:'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      component: {
        render (c) { return c('router-view') }
      },
      children: [
        {
          path: '/',
          name: 'home',
          component: Home
        },
        {
          path: 'avtomobili_v_nalichii',
          name: 'avtomobili_v_nalichii',
          // route level code-splitting
          // this generates a separate chunk (about.[hash].js) for this route
          // which is lazy-loaded when the route is visited.
          component: () => import(/* webpackChunkName: "about" */ './views/Avtomobili_v_nalichii.vue')
        },
        {
          path: '/contact',
          name: 'contact',
          component: Contact
        },
        {
          path: '/serviceform',
          name: 'serviceform',
          component: () => import(/* webpackChunkName: "about" */ './views/Serviceform.vue')
        },
        {
          path: '/testdriveForm',
          name: 'testdriveForm',
          component: () => import(/* webpackChunkName: "about" */ './views/TestdriveForm.vue')
        },
        {
          path: '/account',
          name: 'account',
          component: () => import(/* webpackChunkName: "about" */ './views/Account.vue')
        }
      ]
    }
  ]
})