<!--<template>-->
<!--  <div>-->
<!--    <div class="px-20 py-8">-->
<!--      <h2 class="mb-4 uppercase tracking-wide text-xl">Добавить автомобиль</h2>-->
<!--      <form @submit.prevent="addAuto">-->
<!--        <div class="form-group mb-4">-->
<!--          <label for="model" class="block font-normal uppercase tracking-wide text-xs mb-1">Модель</label>-->
<!--          <input v-model="form.model" type="text" id="model" name="model" class="border px-4 py-2 w-full rounded bg-red-700" ref="model" @keydown.shift.tab.prevent="">-->
<!--        </div>-->
<!--        <div class="form-group mb-4">-->
<!--          <label for="year_of_issue" class="block font-normal uppercase tracking-wide text-xs mb-1">Год выпуска</label>-->
<!--          <input v-model="form.year_of_issue" type="number" id="year_of_issue" name="year_of_issue" class="border px-4 py-2 w-full rounded bg-red-200" ref="year_of_issue" @keydown.shift.tab.prevent="">-->
<!--        </div>-->
<!--        <div class="form-group mb-4">-->
<!--          <label for="body_type" class="block font-normal uppercase tracking-wide text-xs mb-1">Тип кузова</label>-->
<!--          <input v-model="form.body_type" type="text" id="body_type" name="body_type" class="border px-4 py-2 w-full rounded bg-red-200" ref="body_type" @keydown.shift.tab.prevent="">-->
<!--        </div>-->
<!--        <div class="form-group mb-4">-->
<!--          <label for="power" class="block font-normal uppercase tracking-wide text-xs mb-1">Мощность</label>-->
<!--          <input v-model="form.power" type="number" id="power" name="power" class="border px-4 py-2 w-full rounded bg-red-200" ref="power" @keydown.shift.tab.prevent="">-->
<!--        </div>-->
<!--        <div class="form-group mb-4">-->
<!--          <label for="engine_volume" class="block font-normal uppercase tracking-wide text-xs mb-1">Объем</label>-->
<!--          <input v-model="form.engine_volume" type="number" id="engine_volume" name="engine_volume" class="border px-4 py-2 w-full rounded bg-red-200" ref="engine_volume" @keydown.shift.tab.prevent="">-->
<!--        </div>-->
<!--        <div class="form-group mb-4">-->
<!--          <label for="number_of_gears" class="block font-normal uppercase tracking-wide text-xs mb-1">Кол-во передач</label>-->
<!--          <input v-model="form.number_of_gears" type="number" id="number_of_gears" name="number_of_gears" class="border px-4 py-2 w-full rounded bg-red-200" ref="number_of_gears" @keydown.shift.tab.prevent="">-->
<!--        </div>-->
<!--        <div class="form-group mb-4">-->
<!--          <label for="price" class="block font-normal uppercase tracking-wide text-xs mb-1">Цена</label>-->
<!--          <input v-model="form.price" type="number" id="price" name="price" class="border px-4 py-2 w-full rounded bg-red-200" ref="price" @keydown.shift.tab.prevent="">-->
<!--        </div>-->
<!--        <div class="form-group mb-4">-->
<!--          <label class="block font-normal uppercase tracking-wide text-xs mb-1">Цена</label>-->
<!--          <input type="file" @change="onFileSelected" class="border px-4 py-2 w-full rounded bg-red-200" >-->
<!--        </div>-->
<!--        <div class="form-group mb-4">-->
<!--          <button type="submit" class="bg-red-500 hover:bg-red-700 text-white px-4 py-2 rounded w-full">Отправить</button>-->
<!--        </div>-->
<!--      </form>-->
<!--    </div>-->
<!--  </div>-->
<!--</template>-->

<!--<script>-->
<!--import $ from "jquery";-->

<!--export default {-->
<!--  name: "AdminCar",-->
<!--  data() {-->
<!--    return {-->
<!--      form: {-->
<!--        marka: 1,-->
<!--        model: '',-->
<!--        year_of_issue: null,-->
<!--        body_type: '',-->
<!--        power: null,-->
<!--        price: null,-->
<!--        engine_volume: null,-->
<!--        number_of_gears: null,-->
<!--        logo: null-->
<!--      }-->
<!--    }-->
<!--  },-->
<!--  methods: {-->
<!--    addAuto() {-->
<!--      console.log(this.form)-->
<!--      $.ajax({-->
<!--        url: "http://127.0.0.1:8000/api/models/new/",-->
<!--        //contentType: 'multipart/form-data; boundary=&#45;&#45;&#45;&#45;WebKitFormBoundary7MA4YWxkTrZu0gW',-->
<!--        type: "POST",-->
<!--        data: this.form,-->
<!--        success: (response) => {-->
<!--          console.log('Данные добавились')-->
<!--        },-->
<!--        error: (response) => {-->
<!--          console.log(error(),'zalupa')-->
<!--        }-->
<!--      })-->
<!--    },-->
<!--    onFileSelected(event){-->
<!--      this.logo = event.target.files[0]-->
<!--      console.log(this.logo)-->
<!--    }-->
<!--  }-->
<!--}-->
<!--</script>-->

<!--<style scoped>-->

<!--</style>-->









<template>
  <div>
    <div class="form-group mb-4 mt-8">
                <label for="model" class="block font-normal uppercase tracking-wide text-xs mb-1">Модель</label>
                <input v-model="model" type="text" id="model" name="model" class="border px-4 py-2 w-full rounded bg-red-700" ref="model" @keydown.shift.tab.prevent="">
              </div>
              <div class="form-group mb-4">
                <label for="year_of_issue" class="block font-normal uppercase tracking-wide text-xs mb-1">Год выпуска</label>
                <input v-model="year_of_issue" type="number" id="year_of_issue" name="year_of_issue" class="border px-4 py-2 w-full rounded bg-red-200" ref="year_of_issue" @keydown.shift.tab.prevent="">
              </div>
              <div class="form-group mb-4">
                <label for="body_type" class="block font-normal uppercase tracking-wide text-xs mb-1">Тип кузова</label>
                <input v-model="body_type" type="text" id="body_type" name="body_type" class="border px-4 py-2 w-full rounded bg-red-200" ref="body_type" @keydown.shift.tab.prevent="">
              </div>
              <div class="form-group mb-4">
                <label for="power" class="block font-normal uppercase tracking-wide text-xs mb-1">Мощность</label>
                <input v-model="power" type="number" id="power" name="power" class="border px-4 py-2 w-full rounded bg-red-200" ref="power" @keydown.shift.tab.prevent="">
              </div>
              <div class="form-group mb-4">
                <label for="engine_volume" class="block font-normal uppercase tracking-wide text-xs mb-1">Объем</label>
                <input v-model="engine_volume" type="number" id="engine_volume" name="engine_volume" class="border px-4 py-2 w-full rounded bg-red-200" ref="engine_volume" @keydown.shift.tab.prevent="">
              </div>
              <div class="form-group mb-4">
                <label for="number_of_gears" class="block font-normal uppercase tracking-wide text-xs mb-1">Кол-во передач</label>
                <input v-model="number_of_gears" type="number" id="number_of_gears" name="number_of_gears" class="border px-4 py-2 w-full rounded bg-red-200" ref="number_of_gears" @keydown.shift.tab.prevent="">
              </div>
              <div class="form-group mb-4">
                <label for="price" class="block font-normal uppercase tracking-wide text-xs mb-1">Цена</label>
                <input v-model="price" type="number" id="price" name="price" class="border px-4 py-2 w-full rounded bg-red-200" ref="price" @keydown.shift.tab.prevent="">
              </div>
        <div class="form-group mb-4">
          <label class="block font-normal uppercase tracking-wide text-xs mb-1">Фото</label>
          <input type="file" @change="onFileSelected">
          <button @click="onUpload">Добавить</button>
        </div>
  </div>
</template>

<script>
import $ from "jquery";
import axios from "axios"

export default {
  name: "AdminCar",
  data() {
    return {
      marka: 1,
      model: '',
      year_of_issue: null,
      body_type: '',
      power: null,
      price: null,
      engine_volume: null,
      number_of_gears: null,
      logo: null
    }
  },
  methods: {
    onFileSelected(event){
      this.logo = event.target.files[0]
    },
    onUpload(){
      const fd = new FormData();
      fd.append('logo',this.logo, this.logo.name )
      fd.append('body_type',this.body_type )
      fd.append('marka',this.marka)
      fd.append('model',this.model)
      fd.append('price',this.price)
      fd.append('year_of_issue',this.year_of_issue)
      fd.append('power',this.power)
      fd.append('engine_volume',this.engine_volume)
      fd.append('number_of_gears',this.number_of_gears)
      axios.post('http://127.0.0.1:8000/api/models/new/',fd)
      .then(res => {
        console.log(res)
        alert("добавили")
      })
    }
  }
}
</script>

<style scoped>

</style>















