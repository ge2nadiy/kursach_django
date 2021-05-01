<template>
<div>
  <h2 class="mb-4 uppercase tracking-wide text-2xl flex justify-center">Заказы на тест-драйв</h2>
  <div v-for="data in orders" class="ml-10 ">
    <template v-if="data.attributes.user.id == user && data.attributes.date_inquiry !== null">
    <p>Дата тест-драйва: {{data.attributes.date_inquiry}}</p>
    <p>Модель: {{data.attributes.model.marka.marka}} {{data.attributes.model.model}}</p>
      <div class="flex flex-column mb-1">
        <div >
          <button @click="cancel_inquiry(date.id)" type="submit" class="bg-red-500 hover:bg-red-700 text-white px-4 py-2 rounded w-full">Отменить</button>
        </div>
      </div>
<div class="mb-4 w-7/12 shadow-2xl bg-white rounded-lg h-18">
  <img :src="data.attributes.model.logo" alt="logo">
</div>
  </template>
    <template v-if="data.attributes.user.id == user && data.attributes.date_inquiry === null ">
      <h2 class="mb-4 uppercase tracking-wide text-2xl flex justify-center">Заказы на покупку</h2>
      <p>Модель: {{data.attributes.model.marka.marka}} {{data.attributes.model.model}}</p>
      <div class="flex flex-column mb-1">
      <div >
        <button @click="cancel_inquiry(data.id)" type="submit" class="bg-red-500 hover:bg-red-700 text-white px-4 py-2 rounded w-full">Отменить</button>
      </div>
      </div>
      <div class="mb-4 w-7/12 ">
        <img :src="data.attributes.model.logo" alt="logo">
      </div>
    </template>
  </div>


</div>
</template>

<script>
import $ from "jquery";

export default {
  name: "UserOrders",

data(){
  return{
    orders:[],
    user:''
  }
},
created(){
  this.loadOrders();
  this.loadUser();
},

methods:{
  loadOrders() {
    $.ajax({
      url: "http://127.0.0.1:8000/api/inquiry/",
      contentType: 'application/vnd.api+json',
      type: "GET",
      success: (response) => {
        this.orders = response.data;
        console.log(this.orders)
      }
    })
  },
  cancel_inquiry(id_inquiry){
    $.ajax({
      url: "http://127.0.0.1:8000/api/inquiry/" + id_inquiry,
      type: "DELETE",
      success: (response) => {
        console.log("SUCCESS",response)
        alert("Ваша заявка удалена");
      },
      error: (response) => {
        if (response.status === 400) {
          alert('Что-то нетак')
        }
      }
    })
},
  loadUser() {
    $.ajax({
      url: "http://127.0.0.1:8000/auth/users/me/",
      contentType: 'application/vnd.api+json',
      headers: {'Authorization': 'Token ' + localStorage.getItem('auth_token')},
      type: "GET",
      success: (response) => {
        this.user = response.data.id;
        console.log(response.data,"USER")
      }
    })
  }
}
}
</script>

<style scoped>

</style>