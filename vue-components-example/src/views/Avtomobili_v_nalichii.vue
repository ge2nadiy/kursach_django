<template>
  <div>
    <div class="container mx-auto px-8 lg:px-48">
      <div class="flex-column">
        <div class="mt-20">
          <a href="/en/contact">
          <p class="mb-4 text-2xl font-bold">Audi A4</p>
          <img src="@/assets/media/audiA4.jpg" alt="logo">
          </a>
        </div>
        <div class="mt-20">
          <a href="/en/contact">
          <p class="mb-4 text-2xl font-bold">Audi A5</p>
          <img src="@/assets/media/audiA5.jpg" alt="logo">
          </a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import $ from 'jquery'
  export default {
    data() {
      return {
        models: '',
      }
    },
    created() {
      this.loadModel()
    },
    methods: {
      loadModel() {
        $.ajax({
          url: "http://127.0.0.1:8000/api/models/",
          contentType: 'application/vnd.api+json',
          type: "GET",
          success: (response) => {
            this.models = response.data;
            console.log(this.models)
          }
        })
      }
    }
  }
</script>