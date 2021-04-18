<template>
  <div class="container flex flex-row">
    <div class="px-20 py-8">
      <h2 class="mb-4 uppercase tracking-wide text-xl">Аккаунт</h2>
      <form @submit.prevent="setUser">
        <div class="form-group mb-4">
          <label for="username" class="block font-normal uppercase tracking-wide text-xs mb-1">Username</label>
          <input type="text" v-model="form.username" id="username" name="username" class="border px-4 py-2 w-full rounded bg-gray-200" ref="username" @keydown.shift.tab.prevent="">
        </div>
        <div class="form-group mb-4">
          <label for="first_name" class="block font-normal uppercase tracking-wide text-xs mb-1">First Name</label>
          <input type="text" v-model="form.first_name" id="first_name" name="first_name" class="border px-4 py-2 w-full rounded bg-gray-200" ref="first_name" @keydown.shift.tab.prevent="">
        </div>
        <div class="form-group mb-4">
          <label for="last_name" class="block font-normal uppercase tracking-wide text-xs mb-1">Last Name</label>
          <input type="text" v-model="form.last_name" id="last_name" name="last_name" class="border px-4 py-2 w-full rounded bg-gray-200" ref="last_name" @keydown.shift.tab.prevent="">
        </div>
        <div class="form-group mb-4">
          <label for="email" class="block font-normal uppercase tracking-wide text-xs mb-1">Email</label>
          <input type="email" v-model="form.email" id="email" name="email" class="border px-4 py-2 w-full rounded bg-gray-200" ref="email" @keydown.shift.tab.prevent="">
        </div>
        <div class="form-group mb-4">
          <label for="phone" class="block font-normal uppercase tracking-wide text-xs mb-1">Phone</label>
          <input type="text" v-model="form.phone" id="phone" name="phone" class="border px-4 py-2 w-full rounded bg-gray-200" ref="phone" @keydown.shift.tab.prevent="">
        </div>
        <div class="form-group mb-4">
          <button type="submit" class="bg-blue-500 hover:bg-blue-700 text-white px-4 py-2 rounded w-full">Изменить</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
  import $ from 'jquery'
  export default {
  name: "Account",
    data() {
      return {
        form: {
          username: '',
          first_name: '',
          last_name: '',
          email: '',
          phone: ''
        },
      }
    },
    created() {
      $.ajaxSetup({
        headers: {'Authorization': 'Token ' + localStorage.getItem('auth_token')}
      });
      this.loadUser()
    },
    methods: {
      loadUser() {
        $.ajax({
          url: "http://127.0.0.1:8000/auth/users/me/",
          contentType: 'application/vnd.api+json',
          type: "GET",
          success: (response) => {
            this.form = response.data;
            console.log(this.form)
            console.log(this.form.id)
          }
        })
      },
      setUser() {
        console.log(this.form);
         $.ajax({
            url: "http://127.0.0.1:8000/api/3/",
            contentType: 'application/vnd.api+json',
            type: "PUT",
            data: {
              username: this.form.username,
              first_name: this.form.first_name,
              last_name: this.form.last_name,
              email: this.form.email,
              phone: this.form.phone
            },
            success: (response) => {
              console.log('Данные обновились')
            },
            error: (response) => {
              console.log(error())
            }
         })
      }
    }
  }
</script>

<style scoped>

</style>