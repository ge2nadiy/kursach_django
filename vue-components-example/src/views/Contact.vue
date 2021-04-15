<template>
  <div class="container mx-auto  ">
    <div class="flex flex-row">
      <div class="mr-2">
        <img src="@/assets/media/audi-service.jpg" alt="logo" class="">
        <p class="mb-4 text-1xl">Вам и вашему Audi нужно нечто большее, чем просто автосервис.</p>
        <button class=" mt-2 bg-white hover:bg-gray-100 text-gray-800 font-semibold py-2 px-4 border border-gray-600 rounded shadow">
          Подробнее
        </button>
      </div>
      <div class="mr-2" >
        <img  src="@/assets/media/audi-service-kuzow.jpg" alt="logo" class="">
        <p class="mb-4 text-1xl">Ваше ощущение от владения автомобиля во многом зависит от состояния кузова.</p>
        <router-link :to="`/avtomobili_v_nalichii`" class="font-bold text-xl flex items-end">
          <button class=" mt-2 bg-white hover:bg-gray-100 text-gray-800 font-semibold py-2 px-4 border border-gray-600 rounded shadow">
            Посмотреть
          </button>
        </router-link>
      </div>
      <div class="mr-2" >
        <p class="mb-4 text-1xl font-bold">Audi Центр Минск</p>
        <img  src="@/assets/media/audi-service-centr.jpg" alt="logo" class="">
        <p class="mb-4 text-1xl">г. Минск, пр. Независимости,<br> +375 29 191 88 88<br> +375 17 311 88 88</p>
        <router-link :to="`/serviceform`" class="font-bold text-xl flex items-end">
          <button class=" mt-2 bg-white hover:bg-red-600 font-semibold py-2 px-4 border border-gray-600 rounded shadow">
            Записаться на сервис
          </button>
        </router-link>
      </div>
    </div>

  </div>

</template>
