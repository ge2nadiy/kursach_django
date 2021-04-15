<template>
  <div class="normal-case tracking-normal">
    <a href="/#login" @click.prevent="show" class="text-copy-primary uppercase hover:text-gray-600">Login</a>
    <modal name="modal-login" @opened="opened" :adaptive="true" :height="440" :width="400">
      <div class="px-10 py-8">
        <h2 class="mb-4 uppercase tracking-wide text-xl">Login</h2>
        <form @submit="login">
          <div class="form-group mb-4">
            <label for="username" class="block font-normal uppercase tracking-wide text-xs mb-1">Логин</label>
            <input v-model="username" type="text" id="username" name="username" class="border px-4 py-2 w-full rounded bg-gray-200" ref="username" @keydown.shift.tab.prevent="">
          </div>
          <div class="form-group mb-4">
            <label for="password" class="block font-normal uppercase tracking-wide text-xs mb-1">Password</label>
            <input v-model="password" type="password" id="password" name="password" class="border px-4 py-2 w-full rounded bg-gray-200">
          </div>
          <div class="form-group mb-8">
            <label class="text-sm font-normal"><input type="checkbox" name="remember" class="mr-2">Keep me signed in</label>
          </div>
          <div class="form-group mb-4">
            <button type="submit" class="bg-blue-500 hover:bg-blue-700 text-white px-4 py-2 rounded w-full">Login</button>
          </div>
        </form>
        <div class="text-sm font-normal text-center">
          <p>Don't have an account? <a href="#" class="text-blue-600 hover:text-blue-800" @click.prevent="showRegister" @keydown.tab.exact.prevent="">Register</a></p>
        </div>
      </div>
    </modal>
  </div>
</template>

<script>
  import $ from 'jquery'

export default {
  data() {
   return {
     username: "",
     password: ""
   };
 },
  methods: {
    show() {
      this.$modal.show('modal-login')
    },
    login: function (event) {
      event.preventDefault();
      console.log(this.username, this.password);
      $.ajax({
        url: "http://127.0.0.1:8000/auth/token/login/",
        type: "POST",
        data: {
          username: this.username,
          password: this.password
        },
        success: (response) => {
          console.log(response.data.attributes.auth_token)
          localStorage.setItem('auth_token', response.data.attributes.auth_token);
        },
        error: (response) => {
          if (response.status === 400) {
            alert('Логин или пароль не верны')
          }
        }
      })
    },
 /***    this.axios
              .post(`http://127.0.0.1:8000/auth/token/login/`, {
                headers: {'Content-type': 'application-json'},
                'username': this.username, 'password': this.password
              })
              .then(response => {
                console.log(response.data.attributes.auth_token);
                this.setLogined(response.data.attributes.auth_token);
                this.$router.push("/contact");
              })
              .catch(err => {
                console.error(err)
              })
    },
    setLogined(token) {
      localStorage.setItem('token', token);
      console.log(token);
    },***/
    showRegister() {
      this.$modal.show('modal-register')
      this.$modal.hide('modal-login')
    },
    opened() {
      this.$refs.email.focus()
    },
    hide() {
      this.$modal.hide('modal-login')
    }
  }
}
</script>

