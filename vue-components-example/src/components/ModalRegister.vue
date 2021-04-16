<template>
  <div class="normal-case tracking-normal">
    <a href="/#register" @click.prevent="show" class="text-copy-primary uppercase hover:text-gray-600">Register</a>
    <modal name="modal-register" @opened="opened" :adaptive="true" :height="460" :width="400">
      <div class="px-10 py-8">
        <h2 class="mb-4 uppercase tracking-wide text-xl">Register</h2>
        <form @submit.prevent="register">
          <div class="form-group required mb-4">
            <label for="username" class="block font-normal uppercase tracking-wide text-xs mb-1">Username</label>
            <input type="text" v-model="form.username" id="username" name="username" class="border px-4 py-2 w-full rounded bg-gray-200" ref="username" @keydown.shift.tab.prevent="">
          </div>
          <div class="form-group required mb-4">
            <label for="first_name" class="block font-normal uppercase tracking-wide text-xs mb-1">First Name</label>
            <input type="text" v-model="form.first_name" id="first_name" name="first_name" class="border px-4 py-2 w-full rounded bg-gray-200" ref="first_name" @keydown.shift.tab.prevent="">
          </div>
          <div class="form-group required mb-4">
            <label for="last_name" class="block font-normal uppercase tracking-wide text-xs mb-1">Last Name</label>
            <input type="text" v-model="form.last_name" id="last_name" name="last_name" class="border px-4 py-2 w-full rounded bg-gray-200" ref="last_name" @keydown.shift.tab.prevent="">
          </div>
          <div class="form-group required mb-4">
            <label for="email" class="block font-normal uppercase tracking-wide text-xs mb-1">Email</label>
            <input type="email" v-model="form.email" id="email" name="email" class="border px-4 py-2 w-full rounded bg-gray-200" ref="email" @keydown.shift.tab.prevent="">
          </div>
          <div class="form-group required mb-4">
            <label for="phone" class="block font-normal uppercase tracking-wide text-xs mb-1">Phone</label>
            <input type="text" v-model="form.phone" id="phone" placeholder="+375(33)123-45-67" maxlength="17" name="phone" class="border px-4 py-2 w-full rounded bg-gray-200"
                   ref="phone" @keydown.shift.tab.prevent="">
          </div>
          <div class="form-group required mb-4">
            <label for="password" class="block font-normal uppercase tracking-wide text-xs mb-1">Password</label>
            <input type="password" v-model="form.password" id="password" name="password" class="border px-4 py-2 w-full rounded bg-gray-200">
          </div>
          <div class="form-group required mb-8">
            <label for="confirm_password" class="block font-normal uppercase tracking-wide text-xs mb-1">Confirm Password</label>
            <input type="password" v-model="form.repeatPassword" id="confirm_password" name="confirm_password" class="border px-4 py-2 w-full rounded bg-gray-200">
          </div>
          <div class="form-group mb-4">
            <button type="submit" class="bg-blue-500 hover:bg-blue-700 text-white px-4 py-2 rounded w-full">Register</button>
          </div>
          <p class="mt-2"><small class="text-muted">Все поля отмеченные <span class="text-danger">*</span> обязательны для заполнения</small></p>
        </form>
        <div class="text-sm font-normal text-center">
          <p>Already have an account? <a href="#" class="text-blue-600 hover:text-blue-800" @click.prevent="showLogin" @keydown.tab.exact.prevent="">Login</a></p>
        </div>
      </div>
    </modal>
  </div>
</template>

<script>
  import { required, minLength, sameAs} from 'vuelidate/lib/validators'
  import { IMaskDirective } from 'vue-imask';
  import $ from 'jquery'

export default {
  data() {
 return {
      form: {
        username: "",
        first_name: "",
        last_name: "",
        email: "",
        password: "",
        phone: "",
      },
     repeatPassword: "",
     userPhone: "",
     phoneNumberMask: {
mask: '+{375}(00)000-00-00',
       lazy: true
     },
     err: ''
   };
  },
  validations: {
   username: {
     required
   },
   password: {
     required,
     minLength: minLength(8)
   },
   confirm_password: {
     required,
     sameAs: sameAs('password')
   },
   phone: {
     required
   }
  },
  computed: {
   formValid() {
     return this.$v.$invalid
   }
  },
  methods: {
    show() {
      this.$modal.show('modal-register')
    },
    register: function (event) {
      event.preventDefault();
      console.log(this.form);
      $.ajax({
        url: "http://127.0.0.1:8000/auth/users/",
        type: "POST",
        data: this.form,
        success: (response) => {
          alert('Вы успешно зарегались')
        },
        error: (response) => {
          console.log(error)
          if (response.status === 400) {
            alert('Логин или пароль не верны')
          }
        }
      })
    },
  /***  register: function (event) {
      event.preventDefault();
      console.log(this.form);
      this.axios
              .post(`http://127.0.0.1:8000/auth/users/`,
                { headers: {
                  'Media-type': 'application/vnd.api+json',
                },
                data: this.form
                })
              .then(response => {
                console.log('succeful');
                this.$router.push({name: "home"})
                })
              .catch(error => {
                console.log(error)
              })
    }, ***/
    showLogin() {
      this.$modal.show('modal-login')
      this.$modal.hide('modal-register')
    },
    opened() {
      this.$refs.email.focus()
    },
    hide() {
      this.$modal.hide('modal-register')
    },
    onAccept(e) {
      const maskRef = e.detail
      this.phone = maskRef.value
    },
    onComplete(e) {
      const maskRef = e.detail
      this.userPhone = maskRef.unmaskedValue
    },
    isNumber(e) {
      let regex = /[0-9]/

      if (!regex.test(e.key)) {
        e.returnValue = false;
        if (e.preventDefault) e.preventDefault();
      }
    }
  },
  directives: {
    imask: IMaskDirective
  },
}
</script>

<style>
  .form-group.required:after{
    content: " *";
    color:red;
  }
</style>

