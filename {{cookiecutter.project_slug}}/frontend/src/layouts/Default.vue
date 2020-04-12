<template lang="html">
  <div id="body">
    <app-topnav />

    <main class="section">
      <div class="columns">
        <div class="column">
          Sidebar nav here
        </div>
        <div class="column">
          <router-view />
        </div>
      </div>
    </main>

    <app-footer />
  </div>
</template>

<script>
import Footer from '@/components/Footer.vue'
import TopNav from '@/components/TopNav.vue'

export default {
  name: 'Default',
  components: {
    'app-footer': Footer,
    'app-topnav': TopNav
  },
  computed: {
    isLoggedIn() {
      return this.$store.state.isLoggedIn
    }
  }
}
</script>

<style lang="scss" scoped>
#body {
  display: flex;
  min-height: 100vh;
  flex-direction: column;
}

main {
  flex: 1;
}
</style>
