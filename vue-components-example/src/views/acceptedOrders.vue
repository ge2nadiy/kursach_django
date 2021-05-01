<template>
<div>
  <h2 class="mb-4 uppercase tracking-wide text-3xl flex justify-center">Подтвержденные заказы</h2>
  <h3 class="mb-4 uppercase tracking-wide text-2xl">Заявки на тест-драйв</h3>
  <div v-for="test in testDrive" class="ml-10 ">
    <template v-if="test.attributes.user.id == user.id">
    <p>Дата Тест-драйва: {{test.attributes.date_inquiry}}</p>
    <p>Авто: {{test.attributes.model.marka.marka}} {{test.attributes.model.model}} </p>
      <div class="mb-4 w-7/12 shadow-2xl bg-white rounded-lg h-18">
        <img :src="test.attributes.model.logo" alt="logo">
      </div>
  </template>
  </div>
  <h3 class="mb-4 uppercase tracking-wide text-2xl">Подтвержденные заявки на покупку</h3>
  <div v-for="sold in soldCar" class="ml-10 ">
    <template v-if="sold.attributes.user.id == user.id">
      <p>Авто: {{sold.attributes.model.marka.marka}} {{sold.attributes.model.model}} </p>
      <div class="mb-4 w-7/12 shadow-2xl bg-white rounded-lg h-18">
        <img :src="sold.attributes.model.logo" alt="logo">
      </div>
    </template>
  </div>
</div>
</template>

<script>
import $ from "jquery";

export default {
  name: "acceptedOrders",
  data(){
    return{
      user:'',
      testDrive:[],
      soldCar:[]
    }
  },
  created(){
    this.loadUser();
    this.loadTestDrive();
    this.loadSoldCars();
  },
  methods:{
    loadUser() {
      $.ajax({
        url: "http://127.0.0.1:8000/auth/users/me/",
        contentType: 'application/vnd.api+json',
        headers: {'Authorization': 'Token ' + localStorage.getItem('auth_token')},
        type: "GET",
        success: (response) => {
          this.user = response.data;
          console.log(response.data,"USER")
        }
      })
    },
    loadTestDrive() {
      $.ajax({
        url: "http://127.0.0.1:8000/api/test-drive/",
        contentType: 'application/vnd.api+json',
        headers: {'Authorization': 'Token ' + localStorage.getItem('auth_token')},
        type: "GET",
        success: (response) => {
          this.testDrive = response.data;
          console.log(response.data,"TESTDRIVE")
        }
      })
    },
    loadSoldCars() {
      $.ajax({
        url: "http://127.0.0.1:8000/api/sold-car/",
        contentType: 'application/vnd.api+json',
        headers: {'Authorization': 'Token ' + localStorage.getItem('auth_token')},
        type: "GET",
        success: (response) => {
          this.soldCar = response.data;
          console.log(response.data,"SoldCar")
        }
      })
    }
  }
}
</script>

<style scoped>

</style>