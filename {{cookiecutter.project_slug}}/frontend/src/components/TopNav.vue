<template>
  <header>
    {{ cookiecutter.project_name }}
    <button v-if="isLoggedIn" @click="handleLogoutClick">Logout</button>
  </header>
</template>

<script>
export default {
  name: 'TopNav',
  computed: {
    isLoggedIn() {
      return this.$store.state.isLoggedIn
    }
  },
  methods: {
    async handleLogoutClick() {
      await this.$store.dispatch('logout')
      this.$router.push({ name: 'home' })
    }
  }
}
</script>

<style lang="scss" scoped></style>
