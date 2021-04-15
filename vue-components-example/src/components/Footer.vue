<template>
  <footer class="text-gray-100 bg-gray-800">
    <div class="max-w-4xl mx-auto py-6">
<!--      <h1 class="text-center text-lg lg:text-2xl">-->
<!--        Join 31,000+ other and never miss <br> out on new tips, tutorials, and more.-->
<!--      </h1>-->

      <div class="flex mt-6">
        <div class="flex flex-row">
          <div class=" justify-between md:flex-row">

            <button class="w-full m- p-2 text-sm bg-gray-800 uppercase lg:w-auto hover:bg-gray-700">
              <img src="@/assets/media/icons/contacts.png" alt="logo" >
              Контакты
            </button>
          </div>
          <div class="">

            <button class="w-full m- p-2 text-sm bg-gray-800 uppercase lg:w-auto hover:bg-gray-700">  <img src="@/assets/media/icons/prokat.png" alt="logo" >Запись на тест-драйв</button>
          </div>
          <div>

            <button class="w-full m- p-2 text-sm bg-gray-800 uppercase lg:w-auto hover:bg-gray-700"><img src="@/assets/media/icons/nal.png" alt="logo" >Автомобили в наличии</button>
          </div>
          <div>

            <button class="w-full m- p-2 text-sm bg-gray-800 uppercase lg:w-auto hover:bg-gray-700">  <img src="@/assets/media/icons/car-service.png" alt="logo" >Официальный сервис</button>
          </div>
        </div>
      </div>

      <hr class="h-px mt-6 bg-gray-700 border-none">

      <div class="flex flex-col items-center justify-between mt-6 md:flex-row">
        <div>
          <a href="#" class="text-xl font-bold text-gray-100 hover:text-gray-400">© 2021 AUDI AG. Все права защищены</a>
        </div>

        <div class="flex mt-4 md:m-0">
          <div class="-mx-4">
            <a href="#" class="px-4 text-sm text-gray-100 font-medium hover:text-gray-400">About</a>
            <a href="#" class="px-4 text-sm text-gray-100 font-medium hover:text-gray-400">Blog</a>
            <a href="#" class="px-4 text-sm text-gray-100 font-medium hover:text-gray-400">Contact</a>
          </div>
        </div>
      </div>
    </div>
  </footer>
</template>
<script>
export default {
  name: "Footer"
}
</script>
