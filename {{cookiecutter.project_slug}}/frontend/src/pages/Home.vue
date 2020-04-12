<template>
  <div>
    <section class="main">
      {{ cookiecutter.project_name }}
    </section>
  </div>
</template>

<script>
export default {
  name: 'Home',
  metaInfo: {
    title: '{{ cookiecutter.project_name }}',
    titleTemplate: null
  }
}
</script>

<style lang="scss" scoped>
.main {
  text-align: center;
  font-size: 4rem;
  font-weight: bold;
}
</style>
