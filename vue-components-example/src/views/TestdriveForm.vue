<template>
  <div class="container flex flex-row">
    <div class="px-20 py-8">
      <h2 class="mb-4 uppercase tracking-wide text-xl">Запись на тест-драйв</h2>
<<<<<<< HEAD
      <form action="#" method="post">
        <div class="form-group mb-4">
        <select class="border px-4 py-2 w-full rounded bg-gray-200">
=======
      <form @submit="testdrive">
        <div class="form-group mb-4">
        <select v-model="model" class="border px-4 py-2 w-full rounded bg-gray-200">
>>>>>>> 2eb59d554e7cfd740cf8bad9d45c07e79167c6ca
          <option>Audi A4</option>
          <option>Audi A3</option>
          <option>Audi A8</option>
        </select>
        </div>
        <div class="form-group mb-4">
<<<<<<< HEAD
        <input type="date" class="border px-4 py-2 w-full rounded bg-gray-200"/>
=======
        <input v-model="date" type="date" class="border px-4 py-2 w-full rounded bg-gray-200"/>
>>>>>>> 2eb59d554e7cfd740cf8bad9d45c07e79167c6ca
        </div>
        <div class="form-group mb-4">
          <button type="submit" class="bg-blue-500 hover:bg-blue-700 text-white px-4 py-2 rounded w-full">Отправить</button>
        </div>
      </form>
    </div>
    <div class="mb-5 ml-10">
      <img src="@/assets/media/test.jpg" alt="logo" class="w-200">
    </div>
  </div>
</template>

<script>
<<<<<<< HEAD
export default {
  name: "TestdriveForm"
=======
import $ from "jquery";

export default {
  name: "TestdriveForm",
  data() {
    return {
      auto: '',
      date: ''
    }
  },
  methods: {
    testdrive: function (event) {
      event.preventDefault();
      console.log(this.auto, this.date);
      $.ajax({
        url: "http://127.0.0.1:8000/api/inquiry/new/",
        type: "POST",
        data: {
          user: 1,
          model: 1,
          date_inquiry: this.date
        },
        success: (response) => {
          console.log("SUCCESS")
        },
        error: (response) => {
          if (response.status === 400) {
            alert('Что-то нетак')
          }
        }
      })
    }
  }
>>>>>>> 2eb59d554e7cfd740cf8bad9d45c07e79167c6ca
}
</script>

<style scoped>

</style>