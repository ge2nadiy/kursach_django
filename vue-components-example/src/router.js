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
        },
        {
          path: '/adminpage',
          name: 'adminpage',
          component: () => import(/* webpackChunkName: "about" */ './views/AdminPage.vue')
        },
        {
          path: '/admincar',
          name: 'admincar',
          component: () => import(/* webpackChunkName: "about" */ './views/AdminCar.vue')
        },
        {
          path: '/car/:id',
          name: 'car',
          props:true,
          component: () => import(/* webpackChunkName: "about" */ './views/Car.vue')
        }
        ,
        {
          path: '/3dTour',
          name: '3dTour',
          props:true,
          component: () => import(/* webpackChunkName: "about" */ './views/3dTour.vue')
        },
        {
          path: '/buyform',
          name: 'buyform',
          component: () => import(/* webpackChunkName: "about" */ './views/BuyCar.vue')
        },
        {
          path: '/userorders',
          name: 'userorders',
          component: () => import(/* webpackChunkName: "about" */ './views/UserOrders.vue')
        },
        {
          path: '/acceptedOrders',
          name: 'acceptedOrders',
          component: () => import(/* webpackChunkName: "about" */ './views/acceptedOrders.vue')
        }
      ]
    }
  ]
})