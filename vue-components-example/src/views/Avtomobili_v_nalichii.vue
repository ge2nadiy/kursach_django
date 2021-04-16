<template>
  <div>
    <div class="container mb-8 ml-2">
<<<<<<< HEAD

=======
>>>>>>> 2eb59d554e7cfd740cf8bad9d45c07e79167c6ca
      <form action="#" method="post" class="flex flex-row ml-4">
        <div class="mr-2">
          <select class="border px-4 py-2 w-full rounded bg-gray-200">
            <option value="" disabled selected>По марке</option>
<<<<<<< HEAD
            <option>Audi A4</option>
            <option>Audi A3</option>
            <option>Audi A8</option>
          </select>
        </div>
        <div class="mr-2">
          <select class="border px-4 py-2 w-full rounded bg-gray-200">
            <option value="" disabled selected>По типу кузова</option>
            <option>Седан</option>
            <option>Кроссовер</option>
            <option>Купе</option>
          </select>
        </div>
        <div class="mr-2">
          <input class="border px-4 py-2 w-40 rounded bg-gray-200" placeholder="Цена от" type="number">
        </div>
        <div class="mr-2">
          <input class="border px-4 py-2 w-40 rounded bg-gray-200" placeholder="Цена до" type="number">
        </div>
        <div class="form-group mb-4">
          <button type="submit" class="bg-blue-500 hover:bg-blue-700 text-white px-4 py-2 rounded w-full">Показать</button>
        </div>
      </form>
      <div class="flex justify-center mb-8">
        <a href="/en/contact">
          <img src="@/assets/media/audiA4.jpg" alt="logo">
        </a>
        <div class="ml-4 mx-auto">
          <p class="mb-4 font-bold">Модель:{{}}</p>
          <p class="mb-4 font-bold">Тип кузова {{}}</p>
          <p class="mb-4 font-bold">Мощность {{}}</p>
          <p class="mb-4 font-bold">Год выпуска {{}}</p>
          <p class="mb-4 font-bold">Цена {{}}</p>
        </div>
      </div>
      <div class="flex justify-center mb-8">
        <a href="/en/contact">
          <img src="@/assets/media/audiA4.jpg" alt="logo">
        </a>
        <div class="ml-4 mx-auto">
          <p class="mb-4 font-bold">Модель:{{}}</p>
          <p class="mb-4 font-bold">Тип кузова {{}}</p>
          <p class="mb-4 font-bold">Мощность {{}}</p>
          <p class="mb-4 font-bold">Год выпуска {{}}</p>
          <p class="mb-4 font-bold">Цена {{}}</p>
=======
            <option v-for="currency in models">{{currency.attributes.model}}</option>
          </select>
        </div>
        <div class="mr-2">
          <select class="border px-4 py-2 w-full rounded bg-gray-200">
            <option value="" disabled selected>По типу кузова</option>
            <option v-for="currency in models">{{currency.attributes.body_type}}</option>
          </select>
        </div>
        <div class="mr-2">
          <input class="border px-4 py-2 w-40 rounded bg-gray-200" placeholder="Цена от" type="number">
        </div>
        <div class="mr-2">
          <input class="border px-4 py-2 w-40 rounded bg-gray-200" placeholder="Цена до" type="number">
        </div>
        <div class="form-group mb-4">
          <button type="submit" class="bg-blue-500 hover:bg-blue-700 text-white px-4 py-2 rounded w-full">Показать</button>
        </div>
      </form>
      <div class="flex justify-center mb-8" v-for="currency in models">
        <a href="/en/contact">
          <img :src="currency.attributes.logo" alt="logo">
        </a>
        <div class="ml-4 mx-auto">
          <p class="mb-4 font-bold">Модель:{{currency.attributes.model}}</p>
          <p class="mb-4 font-bold">Тип кузова: {{currency.attributes.body_type}}</p>
          <p class="mb-4 font-bold">Мощность: {{currency.attributes.power}}</p>
          <p class="mb-4 font-bold">Год выпуска: {{currency.attributes.year_of_issue}}</p>
          <p class="mb-4 font-bold">Цена: {{currency.attributes.price}}</p>
>>>>>>> 2eb59d554e7cfd740cf8bad9d45c07e79167c6ca
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import $ from 'jquery'
  export default {
    data() {
      return {
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
      }
    }
  }
</script>