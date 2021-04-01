<template>
    <div>
      <input v-model="login" type="text" aria-placeholder="Логин">
      <input v-model="password" type="password" aria-placeholder="Пароль">
      <button @click="setLogin">Войти</button>
    </div>
</template>

<script>
  import $ from 'jquery'

    export default {
        name: "Login",
        data() {
            return {
                login: '',
                password: '',
            }
        },
        methods: {
            setLogin() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/auth/jwt/create/',
                    type: "POST",
                    data: {
                        username: this.login,
                        password: this.password
                    },
                    success: (response) => {
                        console.log(response)
                    },
                    error: (response) => {
                        console.log(response)
                    }
                })
            }
        }
    }
</script>

<style scoped>

</style>
