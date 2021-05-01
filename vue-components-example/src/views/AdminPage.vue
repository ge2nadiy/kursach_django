<template>
  <div>
    <h2 class="mb-4 mt-4 uppercase tracking-wide text-2xl flex justify-center">Аккаунт Админа</h2>


    <div v-for="date in inquiry" :key="date.id" class="ml-4">

      <div v-if="date.attributes.date_inquiry === null" class=" mb-4 flex flex-row bg-gradient-to-br from-green-400 to-blue-400">
        <h1 class="mb-4 ml-4 mt-2 uppercase tracking-wide text-xl">Заявки на покупку</h1>
        <div class=" flex-column">
       <div class="ml-4" >Пользователь: {{date.attributes.user.username }} </div>
        <div class="ml-4">Email: {{date.attributes.user.email}}</div>
        <div class="ml-4">FirstName: {{date.attributes.user.first_name}}</div>
        <div class="ml-4">LastName: {{date.attributes.user.last_name}}</div>
        <div class="ml-4">Phone: {{date.attributes.user.phone}}</div>
        <div class="ml-4">ID: {{date.attributes.user.id}}</div>
        <div class="ml-4">modelID: {{date.attributes.model.id}}</div>
        <div class="ml-4">SALESID: {{date.id}}</div>
        </div>
        <div >
          <div class="ml-2">Марка: {{date.attributes.model.marka.marka }}  </div>
          <div class="ml-2">Модель: {{date.attributes.model.model }}  </div>
          <div class="ml-2">Тип кузова: {{date.attributes.model.body_type }}  </div>
          <div class="ml-2">Мощность: {{date.attributes.model.power }}  </div>
          <div class="ml-2">Цена: {{date.attributes.model.price }}  </div>
        </div>
<div class="flex-row">
         <div class="ml-4">
           <button @click="buy_car(date.attributes.user.id, date.attributes.model.id, date.id)" type="submit" class="bg-green-500 hover:bg-green-700 text-white px-4 py-2 rounded w-full">Принять</button>
         </div>
        <div class="ml-4">
          <button @click="cancel_buy(date.id)" type="submit" class="bg-red-500 hover:bg-red-700 text-white px-4 py-2 rounded w-full">Отклонить</button>
        </div>
</div>
      </div>
      <div v-else class="bg-gradient-to-br from-yellow-400 to-orange-500 mb-4" >
        <div class="flex flex-column mb-4 mt-2 uppercase tracking-wide text-xl ">Заявка на тест-драйв</div>
        <div class="flex flex-row">
          <div class=" flex-column">
            <div class="uppercase tracking-wide text-xl ml-4 mb-4 flex justify-center">Данные пользователя</div>
            <div class="ml-4" >Пользователь: {{date.attributes.user.username }} </div>
            <div class="ml-4" >id: {{date.attributes.user.id }} </div>
            <div class="ml-4">Email: {{date.attributes.user.email}}</div>
            <div class="ml-4">FirstName: {{date.attributes.user.first_name}}</div>
            <div class="ml-4">LastName: {{date.attributes.user.last_name}}</div>
            <div class="ml-4">Phone: {{date.attributes.user.phone}}</div>
          </div>
          <div >
            <div class="uppercase tracking-wide text-xl ml-4 mb-4 flex justify-center">Данные автомобиля</div>
            <div class="ml-2">Марка: {{date.attributes.model.marka.marka }}  </div>
            <div class="ml-2">Модель: {{date.attributes.model.model }}  </div>
            <div class="ml-2">Тип кузова: {{date.attributes.model.body_type }}  </div>
            <div class="ml-2">Мощность: {{date.attributes.model.power }}  </div>
            <div class="ml-2">Цена: {{date.attributes.model.price }}  </div>
            <div class="ml-2">Дата: {{date.attributes.date_inquiry }}  </div>
          </div>
          <div class="flex-row">
        <div class="ml-4">
          <button @click="test_drive(date.attributes.user.id, date.attributes.model.id, date.id, date.attributes.date_inquiry)" type="submit" class="bg-green-500 hover:bg-green-700 text-white px-4 py-2 rounded w-full">Принять</button>
        </div>
        <div class="ml-4">
          <button @click="cancel_test_drive(date.id)" type="submit" class="bg-red-500 hover:bg-red-700 text-white px-4 py-2 rounded w-full">Отклонить</button>
        </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import $ from 'jquery'
  export default {
    name: 'AdminPage',
    data() {
      return {
        inquiry: [],
        buy: {
          user: null,
          model: null
        },
        testDrive: {
          user: null,
          model: null,
          date_inquiry: null
        },
      }
    },
    created() {
      this.loadInquiry()
    },
    methods: {
      loadInquiry() {
        $.ajax({
          url: "http://127.0.0.1:8000/api/inquiry/",
          contentType: 'application/vnd.api+json',
          type: "GET",
          success: (response) => {
            this.inquiry = response.data;
            console.log(this.inquiry)
          }
        })
      },
      buy_car(id_user, id_model, id_inquiry){
        this.buy.user = id_user;
        this.buy.model = id_model;
        $.ajax({
          url: "http://127.0.0.1:8000/api/sold-car/new/",
          type: "POST",
          data: this.buy,
          success: (response) => {
            console.log("SUCCESS",response)
          },
          error: (response) => {
            if (response.status === 400) {
              alert('Что-то нетак'+ this.model)
            }
          }
        }),
        $.ajax({
          url: "http://127.0.0.1:8000/api/inquiry/" + id_inquiry,
          type: "DELETE",
          success: (response) => {
            console.log("SUCCESS",response)
          },
          error: (response) => {
            if (response.status === 400) {
              alert('Что-то нетак')
            }
          }
        })
      },
      cancel_buy(id_inquiry){
        $.ajax({
          url: "http://127.0.0.1:8000/api/inquiry/" + id_inquiry,
          type: "DELETE",
          success: (response) => {
            console.log("SUCCESS",response)
          },
          error: (response) => {
            if (response.status === 400) {
              alert('Что-то нетак')
            }
          }
        })
      },
      test_drive(id_user, id_model, id_inquiry, data_inquiry){
        this.testDrive.user = id_user;
        this.testDrive.model = id_model;
        this.testDrive.date_inquiry = data_inquiry;
        $.ajax({
          url: "http://127.0.0.1:8000/api/test-drive/new/",
          type: "POST",
          data: this.testDrive,
          success: (response) => {
            console.log("SUCCESS",response)
          },
          error: (response) => {
            if (response.status === 400) {
              alert('Что-то нетак'+ this.testDrive)
            }
          }
        }),
        $.ajax({
          url: "http://127.0.0.1:8000/api/inquiry/" + id_inquiry,
          type: "DELETE",
          success: (response) => {
            console.log("SUCCESS",response)
          },
          error: (response) => {
            if (response.status === 400) {
              alert('Что-то нетак')
            }
          }
        })
      },
      cancel_test_drive(id_inquiry){
        $.ajax({
          url: "http://127.0.0.1:8000/api/inquiry/" + id_inquiry,
          type: "DELETE",
          success: (response) => {
            console.log("SUCCESS",response)
          },
          error: (response) => {
            if (response.status === 400) {
              alert('Что-то нетак')
            }
          }
        })
      },
      show() {
        this.$modal.show('modal')
        // this.$modal.hide('modal')
      },
      hide(){
        this.$modal.hide('modal');
      },
      show_auto() {
        this.$modal.show('modal-auto')
      }
    }
  }
</script>

<style scoped>

</style>