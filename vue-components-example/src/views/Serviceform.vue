<template>
  <div class="container flex flex-row">
      <div class="px-20 py-8">
        <h2 class="mb-4 uppercase tracking-wide text-xl">Register</h2>
        <form action="#" method="post">
          <div class="form-group mb-4">
            <label for="email" class="block font-normal uppercase tracking-wide text-xs mb-1">FirstName</label>
            <input type="input" id="firstname" name="firstname" class="border px-4 py-2 w-full rounded bg-gray-200" ref="firstname" @keydown.shift.tab.prevent="">
          </div>
          <div class="form-group mb-4">
            <label for="lastname" class="block font-normal uppercase tracking-wide text-xs mb-1">LastName</label>
            <input type="lastname" id="lastname" name="lastname" class="border px-4 py-2 w-full rounded bg-gray-200" ref="lastname" @keydown.shift.tab.prevent="">
          </div>
          <div class="form-group mb-4">
            <label for="email" class="block font-normal uppercase tracking-wide text-xs mb-1">Email</label>
            <input type="email" id="email" name="email" class="border px-4 py-2 w-full rounded bg-gray-200" ref="email" @keydown.shift.tab.prevent="">
          </div>
          <div class="form-group mb-4">
            <label for="password" class="block font-normal uppercase tracking-wide text-xs mb-1">Password</label>
            <input type="password" id="password" name="password" class="border px-4 py-2 w-full rounded bg-gray-200">
          </div>
          <div class="form-group mb-8">
            <label for="confirm_password" class="block font-normal uppercase tracking-wide text-xs mb-1">Confirm Password</label>
            <input type="password" id="confirm_password" name="confirm_password" class="border px-4 py-2 w-full rounded bg-gray-200">
          </div>
          <div class="form-group mb-4">
            <button type="submit" class="bg-blue-500 hover:bg-blue-700 text-white px-4 py-2 rounded w-full">Отправить</button>
          </div>
        </form>
      </div>
  </div>
</template>

<script>
export default {
  name: "Serviceform"
}
</script>

<style scoped>

</style>