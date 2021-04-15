<template>
  <div
    class="relative"
    @mouseover="showMenu"
    @mouseleave="hideMenu"
  >
    <a
      href="/#features"
      class="text-copy-primary hover:text-gray-600 "
      @focus="showMenu"
      @keydown.shift.tab="hideMenu"
      @keydown.esc.exact="hideMenu"
      @keydown.up.exact.prevent="startArrowKeys"
      @keydown.down.exact.prevent="startArrowKeys"
    >
      {{model}}
    </a>

    <div class="absolute w-full">&nbsp;</div>
    <transition name="mega-menu-fade">
      <div v-show="isVisible" class=" mega-menu absolute normal-case  font-normal bg-white shadow-md rounded-lg overflow-hidden border mt-4 w-full lg:w-160 z-30 lg:z-10 left-0 lg:-left-16">
        <div class="flex flex-col lg:flex-row px-8 py-6 border-b -mx-4 ">
          <ul class="w-full lg:w-1/2 px-4">
            <li class="mb-8">
              <a
                href="#"
                class="flex group"
                @keydown.esc.exact="hideMenu"
                @keydown.tab.exact="focusNext(false)"
                @keydown.down.exact.prevent="focusNext(true)"
                @keydown.up.exact.prevent=""
              >
                <span class="ml-2">
                  <span class="block font-bold text-blue-800 group-hover:text-blue-800 flex items-center">
                    <span>{{type_model}}</span>
<!--                    <span class="ml-2 bg-yellow-500 text-yellow-800 px-2 py-1 rounded-full uppercase font-bold text-xxs">New</span>-->
                  </span>
<!--                  <span class="block text-sm text-gray-600 group-hover:text-blue-800">Measure actions users take</span>-->
                </span>
              </a>
            </li>
            <li class="mb-8">
              <a
                  href="#"
                  class="flex group"
                  @keydown.esc.exact="hideMenu"
                  @keydown.tab.exact="focusNext(false)"
                  @keydown.down.exact.prevent="focusNext(true)"
                  @keydown.up.exact.prevent=""
              >
                <span class="ml-2">
                  <span class="block font-bold text-blue-800 group-hover:text-blue-800 flex items-center">
                    <span>{{type_model}}</span>
                    <!--                    <span class="ml-2 bg-yellow-500 text-yellow-800 px-2 py-1 rounded-full uppercase font-bold text-xxs">New</span>-->
                  </span>
                  <!--                  <span class="block text-sm text-gray-600 group-hover:text-blue-800">Measure actions users take</span>-->
                </span>
              </a>
            </li>
<!--            <li class="mb-8">-->
<!--              <a-->
<!--                href="#"-->
<!--                class="flex group"-->
<!--                @keydown.esc.exact="hideMenu"-->
<!--                @keydown.tab.exact="focusNext(false)"-->
<!--                @keydown.shift.tab="focusPrevious(false)"-->
<!--                @keydown.up.exact.prevent="focusPrevious(true)"-->
<!--                @keydown.down.exact.prevent="focusNext(true)"-->
<!--              >-->
<!--                <svg fill="currentColor" class="text-blue-500 group-hover:text-blue-800" xmlns="http://www.w3.org/2000/svg" width="24" height="24"><path class="heroicon-ui" d="M12 22a10 10 0 1 1 0-20 10 10 0 0 1 0 20zm0-2a8 8 0 1 0 0-16 8 8 0 0 0 0 16zm1-8.41l2.54 2.53a1 1 0 0 1-1.42 1.42L11.3 12.7a1 1 0 0 1-.3-.7V8a1 1 0 0 1 2 0v3.59z"/></svg>-->
<!--                <span class="ml-2">-->
<!--                  <span class="block font-bold text-blue-800 group-hover:text-blue-800">Test Missle Alert</span>-->
<!--                  <span class="block text-sm text-gray-600 group-hover:text-blue-800">Probably meant to click this one</span>-->
<!--                </span>-->
<!--              </a>-->
<!--            </li>-->
          </ul>
          <ul class="w-300 lg:w-1/2 px-4 ">
            <li class="mb-8 " >
              <a
                  href="#"
                  class="flex group"
                  @keydown.esc.exact="hideMenu"
                  @keydown.tab.exact="focusNext(false)"
                  @keydown.down.exact.prevent="focusNext(true)"
                  @keydown.up.exact.prevent=""
              >
                <span class="ml-2">
                  <span class="block font-bold text-blue-800 group-hover:text-blue-800">
                    <div>
                       <img src="@/assets/media/AudiA3.png" alt="logo" class="w-200">
                    </div>
                  </span>
                </span>
              </a>
            </li>
          </ul>
        </div>

      </div>
    </transition>
  </div>
</template>

<script>
export default {
  props : {
    model : String,
    type_model : String
  },
  mounted() {
    this.menuItems = document.querySelectorAll('.mega-menu a')
  },
  data() {
    return {
      isVisible: false,
      menuItems: null,
      focusedIndex: 0,
    }
  },
  methods: {
    showMenu() {
      this.isVisible = true
    },
    hideMenu() {
      this.isVisible = false
      this.focusedIndex = 0
    },
    startArrowKeys() {
      this.menuItems[0].focus()
    },
    focusPrevious(isArrowKey) {
      this.focusedIndex = this.focusedIndex - 1

      if (isArrowKey) {
        this.focusItem()
      }
    },
    focusNext(isArrowKey) {
      this.focusedIndex = this.focusedIndex + 1

      if (isArrowKey) {
        this.focusItem()
      }
    },
    focusItem() {
      this.menuItems[this.focusedIndex].focus()
    }
  }
}
</script>

<style scoped>
  .mega-menu-fade-enter-active, .mega-menu-fade-leave-active {
    transition: all .3s ease-in-out;
  }
  .mega-menu-fade-enter, .mega-menu-fade-leave-to {
    opacity: 0;
    transform: translateY(-12px);
  }
</style>
