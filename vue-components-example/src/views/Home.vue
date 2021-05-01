<template>
  <div>
    <div class="container mx-auto mt-4 ">
      <div class="flex flex-row">
  <div class="mr-2">
    <p class="mb-4 text-2xl font-bold">Сервис AUDI</p>
    <img src="@/assets/media/servis.jpg" alt="logo" class="">
    <button class=" mt-2 bg-white hover:bg-gray-100 text-gray-800 font-semibold py-2 px-4 border border-gray-600 rounded shadow">
      Подробнее
    </button>
  </div>
        <div class="mr-2" >
          <p class="mb-4 text-2xl font-bold">Новые машины в наличии</p>
          <img  src="@/assets/media/audi-sq8-.jpg" alt="logo" class="">
          <router-link :to="`/avtomobili_v_nalichii`" class="font-bold text-xl flex items-end">
          <button class=" mt-2 bg-white hover:bg-gray-100 text-gray-800 font-semibold py-2 px-4 border border-gray-600 rounded shadow">
            Посмотреть
          </button>
          </router-link>
        </div>
</div>

        <p class="mb-4 mt-12 text-2xl font-bold">Специальные предложения сервиса</p>
      <div class="pb-16 flex flex-row">
        <a
            href="/contact"
            class="flex group"
        >
        <div class="mr-2">
          <img src="@/assets/media/service-car1.jpg" alt="logo" class="w-200">
          <p class="mb-4 mt-4 text-1xl ">какой-то текст про сервис какой-то текст про сервис какой-то текст про сервис</p>
        </div>
        <div class="mr-2">
          <img src="@/assets/media/service-car2.jpg" alt="logo" class="w-200">
          <p class="mb-4 mt-4 text-1xl ">какой-то текст про сервис какой-то текст про сервис какой-то текст про сервис</p>
        </div>
        <div class="mr-2">
          <img src="@/assets/media/service-car3.jpg" alt="logo" class="w-200">
          <p class="mb-4 mt-4 text-1xl ">какой-то текст про сервис какой-то текст про сервис какой-то текст про сервис</p>
        </div>
        </a>
      </div>
      <div class="flex flex-row">
        <div class="mr-2">
          <div class="mb-4 text-2xl font-bold">Склад автомобилей с пробегом</div>
          <img src="@/assets/media/probeg.jpg" alt="logo" class="w-200">
          <button class=" mt-1 bg-white hover:bg-gray-100 text-gray-800 font-semibold py-2 px-4 border border-gray-600 rounded shadow">
            в Audi Центр
          </button>
        </div>
        <div>
          <div class="mb-4 text-2xl font-bold">Новое поколение Audi A5 уже в Audi Центр</div>
          <img src="@/assets/media/service-car4.jpg" alt="logo" class="w-200">
          <button class=" mt-1 bg-white hover:bg-gray-100 text-gray-800 font-semibold py-2 px-4 border border-gray-600 rounded shadow">
            Подробнее
          </button>
        </div>
      </div>
      <div class="pb-16">
        <div class="mb-4 text-2xl font-bold">This is a title</div>
        <p>Lorem ipsum dolor sit amet <a href="#" class="text-blue-600 hover:text-blue-800">consectetur</a> adipisicing elit. Aut dicta incidunt ea ut commodi quidem temporibus illo quia. Et itaque deleniti veniam tempore facere ipsum animi totam culpa minima vel voluptatem adipisci natus blanditiis similique sunt expedita, ex dicta doloremque repellat vitae temporibus. Quisquam quia, accusantium blanditiis architecto facilis saepe! Lorem ipsum dolor sit amet consectetur adipisicing elit. Ad unde laborum ut suscipit iure aliquam sapiente doloribus exercitationem nam sint.</p>
      </div>
    </div>
  </div>
</template>

<script>
// import SelectablePlan from '@/components/SelectablePlan.vue'
// import PricingTable from '@/components/PricingTable.vue'

export default {
  components: {
    // SelectablePlan,
    // PricingTable,
  },
  data() {
    return {
      activePlan: '',
    }
  }
}
</script>
