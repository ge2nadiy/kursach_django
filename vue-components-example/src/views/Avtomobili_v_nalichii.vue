<template>
  <div>
    <div class="container mb-8 ml-2 mt-4">
      <form @submit.prevent="getFilter" class="flex flex-row ml-4">
        <div class="mr-2">
          <select v-model="filter.model" class="border px-4 py-2 w-full rounded bg-gray-200">
            <option value="" disabled selected>По модели</option>
            <option value=""></option>
            <option v-for="currency in models" :key="currency.id">{{currency.attributes.model}}</option>
          </select>
        </div>
        <div class="mr-2">
          <select v-model="filter.body_type" class="border px-4 py-2 w-full rounded bg-gray-200">
            <option value="" disabled selected>По типу кузова</option>
            <option value=""></option>
            <option v-for="currency in models" :key="currency.id" >{{currency.attributes.body_type}}</option>
          </select>
        </div>
        <div class="mr-2">
          <input class="border px-4 py-2 w-40 rounded bg-gray-200" v-model="filter.min_price" id="min_price" name="min_price" placeholder="Цена от" type="number">
        </div>
        <div class="mr-2">
          <input class="border px-4 py-2 w-40 rounded bg-gray-200" v-model="filter.max_price" id="max_price" name="max_price" placeholder="Цена до" type="number">
        </div>
        <div class="form-group mb-4">
          <button  type="submit" class="bg-blue-500 hover:bg-blue-700 text-white px-4 py-2 rounded w-full">Показать</button>
        </div>
      </form>
        <div class="form-group mb-4 ml-2 w-1/6">
          <button @click="loadModel" class="bg-red-500 hover:bg-blue-700 text-white px-4 py-2 rounded w-full">Cбросить</button>
        </div>
      <div class="flex justify-center mb-8" v-for="currency in models" :key="currency.id">
        <div class="w-7/12 ">
          <img  :src="currency.attributes.logo" alt="logo">
        </div>
        <router-link :to="{name:'car', params:{id:currency.id}}" class="font-bold text-xl flex items-end">
        <div class="ml-4 mx-auto">
          <p class="mb-4 font-bold">Модель:{{currency.attributes.model}}</p>
          <p class="mb-4 font-bold">Тип кузова: {{currency.attributes.body_type}}</p>
          <p class="mb-4 font-bold">Мощность: {{currency.attributes.power}}</p>
          <p class="mb-4 font-bold">Год выпуска: {{currency.attributes.year_of_issue}}</p>
          <p class="mb-4 font-bold">Цена: {{currency.attributes.price}}</p>
        </div>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
import $ from 'jquery'
export default {
  data() {
    return {
      filt: '',
      filter: {},
      models: [],
    }
  },
  created() {
    this.loadModel()
  },
  methods: {
    loadModel() {
      $.ajax({
        url: "http://127.0.0.1:8000/api/models/",
        contentType: 'application/vnd.api+json',
        type: "GET",
        success: (response) => {
          this.models = response.data;
          console.log(this.models)
        }
      })
    },
    getFilter() {
      this.filt = '';
      if (this.filter.model) {
        this.filt += '?model=' + this.filter.model
      }
      if (this.filter.body_type){
        if (this.filt === '') {
          this.filt += '?body_type=' + this.filter.body_type
        }
        else
          this.filt += '&body_type=' + this.filter.body_type
      }
      if (this.filter.min_price){
        if (this.filt === '') {
          this.filt += '?min_price=' + this.filter.min_price
        }
        else
          this.filt += '&min_price=' + this.filter.min_price
      }
      if (this.filter.max_price){
        if (this.filt === '') {
          this.filt += '?max_price=' + this.filter.max_price
        }
        else
          this.filt += '&max_price=' + this.filter.max_price
      }
      $.ajax({
        url: "http://127.0.0.1:8000/api/models/" + this.filt,
        contentType: 'application/vnd.api+json',
        type: "GET",
        success: (response) => {
          this.models = response.data;
          console.log(response.data + "zalupa")
        }
      })
    }
  }
}
</script>