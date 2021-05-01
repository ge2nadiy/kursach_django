<template>
  <div id="app" class="font-sans text-gray-800">
    <header class="border-t-4 border-red-700 bg-white z-10 absolute w-full shadow-md">
      <nav class="container mx-auto px-8 flex flex-wrap justify-between items-start py-8  ">
        <div class="mb-0 lg:mb-6 xl:mb-0 ">
          <router-link :to="`/`" class="font-bold text-xl flex items-end">
            <img src="@/assets/media/audi.jpg" alt="logo" class="w-12">
          </router-link>
        </div>
        <div class="block lg:hidden">
          <button @click="toggleMenu" class="flex items-center px-3 py-2 border rounded border-gray-500 hover:text-gray-600 hover:border-gray-600">
            <svg class="current-color h-3 w-3" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path d="M0 3h20v2H0V3zm0 6h20v2H0V9zm0 6h20v2H0v-2z" fill="gray" /></svg>
          </button>
        </div>
        <ul
          class="uppercase tracking-wide font-bold w-full block flex-grow lg:flex lg:flex-initial lg:w-auto items-center mt-8 lg:mt-0 "
          :class="menuOpen ? 'block': 'hidden' "
        >

          <li class="mr-8 mb-6 lg:mb-0">
            <mega-menu model="A3" type_model="Audi A3 Sportback" />
          </li>
          <li class="mr-8 mb-6 lg:mb-0">
            <mega-menu model="A4" />
          </li>
          <li class="mr-8 mb-6 lg:mb-0">
            <mega-menu model="A5" />
          </li>
          <li class="mr-8 mb-6 lg:mb-0">
            <mega-menu model="A6" />
          </li>
          <li class="mr-8 mb-6 lg:mb-0">
            <mega-menu model="A7" />
          </li>
          <li class="mr-8 mb-6 lg:mb-0">
            <mega-menu model="A8" />
          </li>
          <li class="mr-8 mb-6 lg:mb-0">
            <mega-menu model="Q3" />
          </li>
          <li class="mr-8 mb-6 lg:mb-0">
            <mega-menu model="Q5"  />
          </li>
          <li class="mr-8 mb-6 lg:mb-0">
            <mega-menu model="Q7" />
          </li>
          <li class="mr-8 mb-6 lg:mb-0">
            <mega-menu model="Q8" />
          </li>
          <li class="mr-12 mb-6 lg:mb-0">
            <search-component />
          </li>
<!--          <div v-if="auth != null"> </div>-->
          <li class="mr-8 mb-6 lg:mb-0" >
            <modal-login />
          </li>

          <li class="mr-8 mb-6 lg:mb-0">
            <modal-register />
          </li>
          <li>
            <dropdown-menu />
          </li>
        </ul>
      </nav>
    </header>

    <div class="bg-gray-100 min-h-screen pt-40 text-lg">
      <router-view/>
    </div>
      <Footer />
  </div>

</template>

<script>
import DropdownMenu from '@/components/DropdownMenu.vue'
import MegaMenu from '@/components/MegaMenu.vue'
import ModalLogin from '@/components/ModalLogin.vue'
import ModalRegister from '@/components/ModalRegister.vue'
// import LanguageSwitcher from '@/components/LanguageSwitcher.vue'
import SearchComponent from '@/components/SearchComponent.vue'
import Footer from '@/components/Footer.vue'

export default {
  name: 'app',
  data(){
    return{
      auth: this.localStorage.getItem("token")
    }
  },
  created() {
    if(localStorage.getItem("token")) {
      $.ajaxSetup({
        headers: {'Authorization': "Token " + localStorage.getItem("token")},
      });
    }
  },
  components: {
    DropdownMenu,
    MegaMenu,
    Footer,
    ModalLogin,
    ModalRegister,
    // LanguageSwitcher,
    SearchComponent,
  },
  data() {
    return {
      menuOpen: false,
    }
  },
  methods: {
    toggleMenu() {
      this.menuOpen = !this.menuOpen
    }
  }
}
</script>

<style src="@/assets/css/tailwind.css" />


