import Vue from 'vue'
import VueRouter from 'vue-router'

import { AUTH_TOKEN_COOKIE_NAME } from './constants'

import Cookies from 'js-cookie'

import PageNotFound from '@/pages/PageNotFound.vue'
import Home from '@/pages/Home.vue'

const routes = [
  {
    path: '*',
    component: PageNotFound,
    name: 'not-found',
    meta: { layout: 'no-sidebar' }
  },
  { path: '/', component: Home, name: 'home', meta: { layout: 'no-sidebar' } }
]

Vue.use(VueRouter)
const router = new VueRouter({
  scrollBehavior(to, from, savedPosition) {
    return { x: 0, y: 0 }
  },
  mode: 'history',
  routes
})

router.beforeEach((to, from, next) => {
  // redirect to login page if not logged in and trying to access a restricted page
  const publicPages = ['/']
  const isPublicPage = publicPages.includes(to.path)
  const authRequired = !isPublicPage
  const loggedIn = Cookies.get(AUTH_TOKEN_COOKIE_NAME)

  if (authRequired && !loggedIn) {
    return next('/')
  }

  next()
})

export default router
