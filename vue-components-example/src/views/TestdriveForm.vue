<template>
  <div class="container flex flex-row">
    <div class="px-20 py-8">
      <h2 class="mb-4 uppercase tracking-wide text-xl">Запись на тест-драйв</h2>
      <form action="#" method="post">
        <div class="form-group mb-4">
        <select class="border px-4 py-2 w-full rounded bg-gray-200">
          <option>Audi A4</option>
          <option>Audi A3</option>
          <option>Audi A8</option>
        </select>
        </div>
        <div class="form-group mb-4">
        <input type="date" class="border px-4 py-2 w-full rounded bg-gray-200"/>
        </div>
        <div class="form-group mb-4">
          <button type="submit" class="bg-blue-500 hover:bg-blue-700 text-white px-4 py-2 rounded w-full">Отправить</button>
        </div>
      </form>
    </div>
    <div class="mb-5 ml-10">
      <img src="@/assets/media/test.jpg" alt="logo" class="w-200">
    </div>
  </div>
</template>

<script>
export default {
  name: "TestdriveForm"
}
</script>

<style scoped>

</style>