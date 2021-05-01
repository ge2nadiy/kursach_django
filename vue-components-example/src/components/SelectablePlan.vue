<template>

<div>
  <div>
    <img :src='img'/>
  </div>
  <div class="mx-auto py-8 md:flex md:justify-between md:flex-wrap">
    <button id="0" v-on:click="getAnswer($event)">
    <div class=" mr-8 w-48 bg-white rounded-lg shadow-md px-6 py-4 cursor-pointer mb-8 hover:bg-green-200 focus:outline-none focus:shadow-outline-green" >
      <div class="flex justify-between items-center mb-3">
        <h1 class="uppercase text-base tracking-wide text-gray-700 font-bold my-2">Радар</h1>
        <div>
          <svg class="w-6 h-6" width="100" height="100" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg"><g fill-rule="nonzero" fill="none"><path d="M31.144 171.84A99.502 99.502 0 1 1 171.841 31.145c37.708 39.043 37.17 101.103-1.212 139.485-38.382 38.381-100.442 38.92-139.485 1.212z" fill="#97EBDC"/><path fill="#00836D" d="M66.667 89.453l22.885 22.985 42.786-42.786 13.93 14.13-56.716 56.517-36.816-36.816 13.93-14.13z"/></g></svg>
        </div>
      </div>
    </div>
    </button>
    <button id="1" v-on:click="getAnswer($event)">
    <div class=" mr-8 w-48 bg-white rounded-lg shadow-md px-6 py-4 cursor-pointer mb-8 hover:bg-green-200 focus:outline-none focus:shadow-outline-green" >
      <div class="flex justify-between items-center mb-3">
        <h1 class="uppercase text-base tracking-wide text-gray-700 font-bold my-2">Сканер</h1>
        <div>
          <svg class="w-6 h-6" width="100" height="100" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg"><g fill-rule="nonzero" fill="none"><path d="M31.144 171.84A99.502 99.502 0 1 1 171.841 31.145c37.708 39.043 37.17 101.103-1.212 139.485-38.382 38.381-100.442 38.92-139.485 1.212z" fill="#97EBDC"/><path fill="#00836D" d="M66.667 89.453l22.885 22.985 42.786-42.786 13.93 14.13-56.716 56.517-36.816-36.816 13.93-14.13z"/></g></svg>
        </div>
      </div>
    </div>
    </button>
    <div class="mr-8 w-48 bg-white rounded-lg shadow-md px-6 py-4 cursor-pointer mb-8 hover:bg-green-200 focus:outline-none focus:shadow-outline-green" >
      <div class="flex justify-between items-center mb-3">
        <h1 class="uppercase text-base tracking-wide text-gray-700 font-bold my-2">Радар</h1>
        <div>
          <svg class="w-6 h-6" width="100" height="100" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg"><g fill-rule="nonzero" fill="none"><path d="M31.144 171.84A99.502 99.502 0 1 1 171.841 31.145c37.708 39.043 37.17 101.103-1.212 139.485-38.382 38.381-100.442 38.92-139.485 1.212z" fill="#97EBDC"/><path fill="#00836D" d="M66.667 89.453l22.885 22.985 42.786-42.786 13.93 14.13-56.716 56.517-36.816-36.816 13.93-14.13z"/></g></svg>
        </div>
      </div>
    </div>
    <div class="w-48 bg-white rounded-lg shadow-md px-6 py-4 cursor-pointer mb-8 hover:bg-green-200 focus:outline-none focus:shadow-outline-green">
      <div class="flex justify-between items-center mb-3">
        <h1 class="uppercase text-base tracking-wide text-gray-700 font-bold my-2">Радар</h1>
        <div>
          <svg class="w-6 h-6" width="100" height="100" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg"><g fill-rule="nonzero" fill="none"><path d="M31.144 171.84A99.502 99.502 0 1 1 171.841 31.145c37.708 39.043 37.17 101.103-1.212 139.485-38.382 38.381-100.442 38.92-139.485 1.212z" fill="#97EBDC"/><path fill="#00836D" d="M66.667 89.453l22.885 22.985 42.786-42.786 13.93 14.13-56.716 56.517-36.816-36.816 13.93-14.13z"/></g></svg>
        </div>
      </div>
    </div>
  </div>

  <div>
    <label v-for="item in items" :key="item">
      <input type="radio" :value="item" v-model="selectedItem">
      {{ item }}
    </label>
  </div>
  <img :src="itemImage" :alt="selectedItem">




</div>
</template>

<script>
export default {
  name: "SelectablePlan",
  data(){
    return{
      selectedItem: "",
      items: ["radar", "ultra", "scaner"]
    }
  },
  computed: {
    itemImage() {
      if (!this.selectedImage) {
        return
      }
      const fileName = this.selectedImage.toLowerCase();
      return require(`@/assets/media/radar.jpeg`);
    }
  }
}
</script>

