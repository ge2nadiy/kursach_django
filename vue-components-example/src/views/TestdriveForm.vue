<template>
  <div class="container flex flex-row">
    <div class="px-20 py-8">
      <h2 class="mb-4 uppercase tracking-wide text-xl">Запись на тест-драйв</h2>
      <form @submit="testdrive">
        <div class="form-group mb-4">
        <select v-model="model"   class="border px-4 py-2 w-full rounded bg-gray-200">
          <option disabled selected>Выбрать авто</option>
          <option v-for="currency in auto" :value="currency.id" :key="currency.id">{{currency.attributes.marka.marka}} {{currency.attributes.model}}</option>
        </select>
        </div>
        <div class="form-group mb-4">
        <input v-model="date" type="date" class="border px-4 py-2 w-full rounded bg-gray-200"/>
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
import $ from "jquery";
export default {
  name: "TestdriveForm",
  data() {
    return {
      auto: '',
      date: '',
      user: '',
      model:''
    }
  },
  created() {
    $.ajaxSetup({
      headers: {'Authorization': 'Token ' + localStorage.getItem('auth_token')}
    });
    this.loadModel();
    this.loadUser();

  },
  methods: {
    loadModel() {
      console.log("modeli")
      $.ajax({
        url: "http://127.0.0.1:8000/api/models/",
        contentType: 'application/vnd.api+json',
        type: "GET",
        success: (response) => {
          this.auto = response.data;
          console.log(this.auto)
        }
      })
    },


    loadUser() {
      console.log("user")
      $.ajax({
        url: "http://127.0.0.1:8000/auth/users/me/",
        contentType: 'application/vnd.api+json',
        type: "GET",
        success: (response) => {
          this.user = response.data;
          console.log(response.data);
          console.log(this.user.id)
        }
      })
    },
    testdrive: function (event) {
      event.preventDefault();
      console.log(this.auto, this.date);
      $.ajax({
        url: "http://127.0.0.1:8000/api/inquiry/new/",
        type: "POST",
        data: {
          user: this.user.id,
          model: this.model,
          date_inquiry: this.date
        },
        success: (response) => {
          console.log("SUCCESS")
          alert('Спасибо, мы ответим вам на почту')
        },
        error: (response) => {
          if (response.status === 400) {
            alert('Что-то не так'+ this.model)
          }
        }
      })
    }
  }
}
</script>

<style scoped>
</style>