<template>
  <div>
    <b-col align-h="center" class="auto-list" @click="goAuto">One of three columns</b-col>
    <br>

    <b-col align-h="center" class="auto-list" @click="goAuto">One of three columns</b-col>
    <br>

    <b-col align-h="center" class="auto-list" @click="goAuto">One of three columns</b-col>
  </div>
</template>

<script>
  export default {
      name: 'Home',
      methods: {
          goAuto() {
              this.$router.push({name: "login"})
          }
      }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .auto-list {
    box-shadow: 1px 4px 5px #848182;
  }
</style>

