<template lang="html">
  <div>
    <app-topnav />

    <main>
      <router-view />
    </main>

    <app-footer />
  </div>
</template>

<script>
import Footer from '@/components/Footer.vue'
import TopNav from '@/components/TopNav.vue'

export default {
  name: 'NoSidebar',
  components: {
    'app-footer': Footer,
    'app-topnav': TopNav
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
