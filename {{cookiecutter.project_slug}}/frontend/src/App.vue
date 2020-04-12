<template lang="html">
  <component :is="layout">
    <router-view />
  </component>
</template>

<script>
import { onLogout } from './apollo'

const defaultLayout = 'default'

export default {
  name: 'App',
  computed: {
    layout() {
      return this.$route.meta.layout || defaultLayout
    }
  },
  metaInfo: {
    // if no subcomponents specify a metaInfo.title, this title will be used
    title: '{{cookiecutter.project_name}}',
    // all titles will be injected into this template
    titleTemplate: '%s | {{cookiecutter.project_name}}'
  }
}
</script>
