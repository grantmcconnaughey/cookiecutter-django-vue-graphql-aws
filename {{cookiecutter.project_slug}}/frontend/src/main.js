import Vue from 'vue'
import store from '@/store'
import router from '@/router'

import { createProvider, onLogin } from '@/apollo'

import Gravatar from 'vue-gravatar'
import VueMeta from 'vue-meta'
import VueGtag from 'vue-gtag'

import Cookies from 'js-cookie'
import { AUTH_TOKEN_COOKIE_NAME } from './constants'

import App from '@/App.vue'
import './registerServiceWorker'

Vue.config.productionTip = false

// https://matteo-gabriele.gitbook.io/vue-gtag/
Vue.use(
  VueGtag,
  {
    config: { id: process.env.VUE_APP_GOOGLE_ANALYTICS }
  },
  router
)

// https://vue-meta.nuxtjs.org/guide/#download-cdn
Vue.use(VueMeta)

Vue.component('v-gravatar', Gravatar)

import { ValidationProvider, ValidationObserver } from 'vee-validate'
Vue.component('validation-provider', ValidationProvider)
Vue.component('validation-observer', ValidationObserver)

// Layouts
import Default from './layouts/Default'
import NoSidebar from './layouts/NoSidebar'
Vue.component('default', Default)
Vue.component('no-sidebar', NoSidebar)

// Sentry
import * as Sentry from '@sentry/browser'
import * as Integrations from '@sentry/integrations'

Sentry.init({
  dsn: process.env.VUE_APP_SENTRY_DSN,
  release: `{{cookiecutter.project_slug}}-frontend@${process.env.npm_package_version}`,
  integrations: [new Integrations.Vue({ Vue, attachProps: true })]
})

// https://vue-apollo.netlify.com/api/apollo-provider.html#constructor
const apolloProvider = createProvider()

new Vue({
  router,
  store,
  apolloProvider,
  render: (h) => h(App),
  async beforeMount() {
    const token = Cookies.get(AUTH_TOKEN_COOKIE_NAME)
    if (token) {
      await onLogin(apolloProvider.defaultClient, token)
      await this.$store.dispatch('login')
    }
  }
}).$mount('#app')
