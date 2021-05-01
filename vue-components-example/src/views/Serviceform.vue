<template>
  <div class="flex justify-center">
      <div class="px-20 py-8">
        <h2 class="mb-4 uppercase tracking-wide text-xl">Запись на сервис</h2>
        <form @submit="serviceform">
          <div class="form-group mb-4">
            <label class="block font-normal uppercase tracking-wide text-xs mb-1">Марка</label>
            <input v-model="marka" class="border px-4 py-2 w-full rounded bg-red-200" @keydown.shift.tab.prevent="">
          </div>
          <div class="form-group mb-4">
            <label class="block font-normal uppercase tracking-wide text-xs mb-1">Модель</label>
            <input v-model="model" class="border px-4 py-2 w-full rounded bg-red-700" ref="lastname" @keydown.shift.tab.prevent="">
          </div>
          <div class="form-group mb-4">
            <label class="block font-normal uppercase tracking-wide text-xs mb-1">Год выпуска</label>
            <input v-model="year_of_issue" class="border px-4 py-2 w-full rounded bg-red-200" ref="email" @keydown.shift.tab.prevent="">
          </div>
          <div class="form-group mb-4">
            <input v-model="date" type="date" class="border hover:bg-red-200 px-4 py-2 w-full rounded bg-red-100"/>
          </div>
          <div class="form-group mb-4">
            <label class="block font-normal uppercase tracking-wide text-xs mb-1">Описание</label>
            <textarea v-model="description" class="border hover:bg-red-200 px-4 py-2 w-full rounded bg-red-100"></textarea>
          </div>
          <div class="form-group mb-4">
            <button type="submit" class="bg-red-500 hover:bg-red-700 text-white px-4 py-2 rounded w-full">Отправить</button>
          </div>
        </form>
      </div>
  </div>
</template>

<script>
import $ from "jquery";

export default {
  name: "Serviceform",
  data() {
    return {
      marka: '',
      model: '',
      year_of_issue: '',
      date: '',
      description: '',
      user: ''

    }
  },
  created() {
    $.ajaxSetup({
      headers: {'Authorization': 'Token ' + localStorage.getItem('auth_token')}
    });
    this.loadUser();

  },


  methods: {
    serviceform: function (event) {
      event.preventDefault();
      $.ajax({
        url: "http://127.0.0.1:8000/api/service/new/",
        type: "POST",
        data: {
          user: this.user.id,
          model: this.model,
          marka: this.marka,
          years: this.year_of_issue ,
          description: this.description,
          date_service: this.date
        },
        success: (response) => {
          console.log("SUCCESS")
          alert('Вы записались на сервис')
        },
        error: (response) => {
          if (response.status === 400) {
            alert('Что-то не так')
          }
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




  }
}
</script>

<style scoped>

</style>