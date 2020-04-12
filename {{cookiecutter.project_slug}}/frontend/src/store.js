import Cookies from 'js-cookie'
import Vue from 'vue'
import Vuex from 'vuex'

import { apolloClient, onLogout } from '@/apollo'
import { AUTH_TOKEN_COOKIE_NAME } from '@/constants'

import logout from '@/graphql/mutations/logout.gql'

Vue.use(Vuex)

const store = new Vuex.Store({
  strict: true,
  state: {
    isLoggedIn: !!Cookies.get(AUTH_TOKEN_COOKIE_NAME),
    profile: null
  },
  mutations: {
    login(state) {
      state.isLoggedIn = true
    },
    logout(state) {
      state.isLoggedIn = false
    }
  },
  actions: {
    async login(context) {
      context.commit('login')
    },
    async logout(context) {
      await apolloClient.mutate({ mutation: logout })
      await onLogout(apolloClient)
      context.commit('logout')
    }
  }
})

export default store
