<template>
  <div class="section">
    <div class="has-text-centered">
      <img src="/img/svg/404.svg" class="not-found-image" />

      <p class="is-size-4 u-my3">
        404 - Page not found
      </p>

      <div class="u-my3">
        <a href="/" class="button is-primary is-size-5">
          Go to home page
        </a>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'PageNotFound'
}
</script>

<style lang="scss" scoped>
.has-text-centered {
  text-align: center;
}

.not-found-image {
  max-height: 20rem;
}
</style>
