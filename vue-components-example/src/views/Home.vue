<template>
  <div>
    <div class="container mx-auto ">
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

<!--      <div class="mx-auto pt-8 pb-6 md:flex md:justify-between items-end border-b-2 border-gray-300">-->
<!--        <div class="text-2xl mb-4 md:mb-0">Change Plan</div>-->
<!--        <div>-->
<!--          <a href="#" class="no-underline hover:underline">Cancel your plan</a>-->
<!--        </div>-->
<!--      </div>-->
<!--      <div class="mx-auto py-8 md:flex md:justify-between md:flex-wrap">-->
<!--        <selectable-plan-->
<!--          plan-name="Hobby"-->
<!--          plan-gigs="1"-->
<!--          plan-dollars="5"-->
<!--          v-model="activePlan"-->
<!--        ></selectable-plan>-->
<!--        <selectable-plan-->
<!--          plan-name="Growth"-->
<!--          plan-gigs="5"-->
<!--          plan-dollars="10"-->
<!--          v-model="activePlan"-->
<!--        ></selectable-plan>-->
<!--        <selectable-plan-->
<!--          plan-name="Business"-->
<!--          plan-gigs="10"-->
<!--          plan-dollars="15"-->
<!--          v-model="activePlan"-->
<!--        ></selectable-plan>-->
<!--        <selectable-plan-->
<!--          plan-name="Enterprise"-->
<!--          plan-gigs="20"-->
<!--          plan-dollars="20"-->
<!--          v-model="activePlan"-->
<!--        ></selectable-plan>-->
<!--      </div>-->
    </div>

<!--    <div class="container mx-auto mt-10 pb-12">-->
<!--      <pricing-table></pricing-table>-->
<!--      <div class="mt-16">Lorem ipsum dolor sit amet consectetur adipisicing elit. Minus ipsa, veniam similique in obcaecati quam sunt laboriosam? Provident sunt a suscipit iure, corporis nemo doloremque nihil earum iste dolor. Sapiente voluptates, eveniet corrupti iste et obcaecati! Aspernatur quia adipisci, facere enim nam architecto perferendis iusto similique natus, fuga dolorem. Ut earum corporis, illo officiis fuga iusto neque debitis rerum obcaecati velit sed qui quam? Aut maiores fugit, voluptatibus et numquam perferendis tempore totam, voluptatem magni similique aspernatur? Ut, molestias. Sunt sint nihil cum reprehenderit harum? Exercitationem distinctio minus eum quidem reprehenderit recusandae architecto, inventore eligendi perspiciatis asperiores tempora velit nam animi error illo porro nemo dolorum dolore ab, veritatis saepe hic eius, ea modi! Distinctio soluta, excepturi accusantium dicta magnam quo saepe tenetur neque deleniti officiis vero ad iure non necessitatibus recusandae consequatur reiciendis quas numquam. Tempora reiciendis minima quia ducimus dolores repudiandae nesciunt exercitationem tempore beatae eos amet obcaecati ut sequi facere quibusdam ipsum porro, excepturi assumenda deserunt delectus magni quasi, officiis corrupti vel. Labore saepe voluptates tempora quaerat aperiam, in consectetur dolorum? Quaerat aliquam mollitia odio quasi ducimus, libero explicabo perferendis illum ipsam. Reiciendis, eaque voluptatem alias nemo rerum aut ipsum dolorem aliquid pariatur atque minus, dolorum quis inventore quos deserunt dolor corporis sunt iste quo. Neque nulla dolorum quaerat provident praesentium doloremque natus facere optio, maxime architecto minima quia excepturi molestiae non odio tempore temporibus magni? Quam mollitia rem omnis temporibus soluta. Mollitia perferendis, dolorum reiciendis soluta quae id, fugiat impedit culpa error voluptatibus tenetur tempora. Iure totam accusamus obcaecati excepturi nemo id dolor ratione. Porro commodi quo unde amet ab error facilis, suscipit reiciendis consectetur, sequi impedit! Obcaecati, provident ad eum asperiores beatae cum dolores adipisci sint eveniet inventore quam dolorum totam fuga dicta dolore consequuntur enim eos quisquam ab laborum corporis doloribus dolorem? Porro ducimus totam molestias quibusdam dolorum, optio consequatur quaerat magni culpa dolore nihil vitae dolor neque nobis molestiae. Ducimus, fugit. Repellat sed nulla voluptatem necessitatibus consequatur beatae placeat similique, recusandae rem, sequi tempore temporibus ab enim eos obcaecati inventore culpa accusamus omnis, excepturi consectetur ea! Vero ex alias quaerat inventore obcaecati doloribus magni qui temporibus porro nesciunt, iure animi provident odio! Repellendus libero saepe natus, odio quidem cupiditate est magni odit! Tenetur possimus animi iste odio quibusdam ab enim quae fuga iure. Eius voluptatibus repudiandae tenetur, dolorum deserunt blanditiis veritatis reiciendis, temporibus harum obcaecati optio vero distinctio sapiente omnis maiores accusamus beatae.</div>-->
<!--    </div>-->
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
