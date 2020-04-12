import Vue from 'vue'
import VueApollo from 'vue-apollo'
import {
  createApolloClient,
  restartWebsockets
} from 'vue-cli-plugin-apollo/graphql-client'

import Cookies from 'js-cookie'

import { AUTH_TOKEN_COOKIE_NAME } from './constants'

// Install the vue plugin
Vue.use(VueApollo)

// Config
const defaultOptions = {
  httpEndpoint: process.env.VUE_APP_API_URL + '/graphql',
  wsEndpoint: null,
  tokenName: AUTH_TOKEN_COOKIE_NAME,
  persisting: false,
  websocketsOnly: false,
  ssr: false,
  getAuth: (tokenName) => {
    const token = Cookies.get(tokenName)
    if (token) {
      return 'Bearer ' + token
    } else {
      return ''
    }
  }
}

function createClient(options = {}) {
  // Create apollo client
  const { apolloClient, wsClient } = createApolloClient({
    ...defaultOptions,
    ...options
  })

  apolloClient.wsClient = wsClient

  return apolloClient
}

export const apolloClient = createClient()

// Call this in the Vue app file
export function createProvider() {
  // Create vue apollo provider
  const apolloProvider = new VueApollo({
    clients: {
      // For public GraphQL nodes
      noauth: createClient({
        tokenName: null,
        getAuth: (tokenName) => {
          return ''
        }
      })
    },
    defaultClient: apolloClient,
    defaultOptions: {
      $query: {
        loadingKey: 'loading',
        fetchPolicy: 'cache-and-network'
      }
    },
    errorHandler(error) {
      // eslint-disable-next-line no-console
      console.log(
        '%cError',
        'background: red; color: white; padding: 2px 4px; border-radius: 3px; font-weight: bold;',
        error.message
      )
    }
  })

  return apolloProvider
}

// Manually call this when user log in
export async function onLogin(apolloClient, token) {
  if (apolloClient.wsClient) restartWebsockets(apolloClient.wsClient)
  try {
    await apolloClient.resetStore()
  } catch (e) {
    // eslint-disable-next-line no-console
    console.log('%cError on cache reset (login)', 'color: orange;', e.message)
  }
}

// Manually call this when user log out
export async function onLogout(apolloClient) {
  // Remove both local and domain cookies on logout
  Cookies.remove(AUTH_TOKEN_COOKIE_NAME)
  Cookies.remove(AUTH_TOKEN_COOKIE_NAME, {
    domain: process.env.VUE_APP_ROOT_DOMAIN
  })
  if (apolloClient.wsClient) restartWebsockets(apolloClient.wsClient)
  try {
    await apolloClient.clearStore()
  } catch (e) {
    // eslint-disable-next-line no-console
    console.log('%cError on cache reset (logout)', 'color: orange;', e.message)
  }
}
