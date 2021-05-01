<template>
  <div>
    <div class="flex justify-center mb-8 p-absolute wow slideInLeft ">
      <img :src="formModel.logo" alt="logo">
    </div>
<template v-if="username === 'admin'">
    <form @submit.prevent="setAuto" class=" ml-20 br-20 flex justify-center ">
      <div class="form-group mb-4">
        <label for="username" class="block font-normal uppercase tracking-wide text-xs mb-1">Model</label>
        <input type="text" v-model="formModel.model" id="username" name="username" class="border px-4 py-2 w-full rounded bg-gray-200" ref="username" @keydown.shift.tab.prevent="">
      </div>
      <div class="form-group mb-4x">
        <label for="first_name" class="block font-normal uppercase tracking-wide text-xs mb-1">Power</label>
        <input type="text" v-model="formModel.power" id="first_name" name="first_name" class="border px-4 py-2 w-full rounded bg-gray-200" ref="first_name" @keydown.shift.tab.prevent="">
      </div>
      <div class="form-group mb-4">
        <label for="last_name" class="block font-normal uppercase tracking-wide text-xs mb-1">Engine volume</label>
        <input type="text" v-model="formModel.engine_volume" id="last_name" name="last_name" class="border px-4 py-2 w-full rounded bg-gray-200" ref="last_name" @keydown.shift.tab.prevent="">
      </div>
      <div class="form-group mb-4">
        <label for="email" class="block font-normal uppercase tracking-wide text-xs mb-1">Number of gears</label>
        <input type="text" v-model="formModel.number_of_gears" id="email" name="email" class="border px-4 py-2 w-full rounded bg-gray-200" ref="email" @keydown.shift.tab.prevent="">
      </div>
      <div class="form-group mb-4">
        <label for="phone" class="block font-normal uppercase tracking-wide text-xs mb-1">Price</label>
        <input type="text" v-model="formModel.price" id="phone" name="phone" class="border px-4 py-2 w-full rounded bg-gray-200" ref="phone" @keydown.shift.tab.prevent="">
      </div>
      <div class="form-group mb-4">
        <label for="phone" class="block font-normal uppercase tracking-wide text-xs mb-1">Body Type</label>
        <input type="text" v-model="formModel.body_type" id="phone" name="phone" class="border px-4 py-2 w-full rounded bg-gray-200" ref="phone" @keydown.shift.tab.prevent="">
      </div>
      <div class="form-group mb-4">
        <label for="phone" class="block font-normal uppercase tracking-wide text-xs mb-1">Years of issue</label>
        <input type="text" v-model="formModel.year_of_issue" id="phone" name="phone" class="border px-4 py-2 w-full rounded bg-gray-200" ref="phone" @keydown.shift.tab.prevent="">
      </div>
      <div class="form-group mb-4">
        <label class="block font-normal uppercase tracking-wide text-xs mb-1">Фото</label>
        <input type="file" @change="onFileSelected">
      </div>
      <div class="form-group mb-4">
        <button type="submit" class="bg-blue-500 hover:bg-blue-700 text-white px-4 py-2 rounded w-full">Изменить</button>
      </div>
      <div class="form-group mb-4 ">
        <button @click="deleteCar" type="submit" class="bg-red-500 hover:bg-red-700 text-white px-4 py-2 rounded w-full">Удалить</button>
      </div>
    </form>

</template>
 <div v-else>
    <div class="block pb-16 flex justify-evenly bg-gray-300 mb-8">
        <div class="mt-10">
          <p class="mb-4 font-bold">Кол-во передач:{{formModel.number_of_gears}}</p>
        </div>
        <div class="mt-10">
          <p class="mb-4 font-bold">Мощность:{{formModel.power}} л/c</p>
        </div>
        <div class="mt-10">
          <p class="font-bold">Объем двигателя:{{formModel.engine_volume}}</p>
        </div>
    </div>
<!--    <div class="sketchfab-embed-wrapper flex justify-center mb-4 ">-->
<!--      <iframe frameborder="2" loading = "lazy"  webkitallowfullscreen="true" allow="fullscreen; vr" xr-spatial-tracking execution-while-out-of-viewport execution-while-not-rendered web-share width="1240" height="820" src="https://sketchfab.com/models/f14648e379654ec4835c98bbf677444f/embed?autostart=1&preload=1&ui_theme=dark">-->
<!--      </iframe>-->
<!--    </div>-->
   <div class="mx-auto py-8 md:flex md:justify-between md:flex-wrap">
     <selectable-plan
     ></selectable-plan>
   </div>
 </div>
<!--    <div class="container mx-auto mt-10 pb-12">-->
<!--      <pricing-table></pricing-table>-->
<!--      <div class="mt-16">Lorem ipsum dolor sit amet consectetur adipisicing elit. Minus ipsa, veniam similique in obcaecati quam sunt laboriosam? Provident sunt a suscipit iure, corporis nemo doloremque nihil earum iste dolor. Sapiente voluptates, eveniet corrupti iste et obcaecati! Aspernatur quia adipisci, facere enim nam architecto perferendis iusto similique natus, fuga dolorem. Ut earum corporis, illo officiis fuga iusto neque debitis rerum obcaecati velit sed qui quam? Aut maiores fugit, voluptatibus et numquam perferendis tempore totam, voluptatem magni similique aspernatur? Ut, molestias. Sunt sint nihil cum reprehenderit harum? Exercitationem distinctio minus eum quidem reprehenderit recusandae architecto, inventore eligendi perspiciatis asperiores tempora velit nam animi error illo porro nemo dolorum dolore ab, veritatis saepe hic eius, ea modi! Distinctio soluta, excepturi accusantium dicta magnam quo saepe tenetur neque deleniti officiis vero ad iure non necessitatibus recusandae consequatur reiciendis quas numquam. Tempora reiciendis minima quia ducimus dolores repudiandae nesciunt exercitationem tempore beatae eos amet obcaecati ut sequi facere quibusdam ipsum porro, excepturi assumenda deserunt delectus magni quasi, officiis corrupti vel. Labore saepe voluptates tempora quaerat aperiam, in consectetur dolorum? Quaerat aliquam mollitia odio quasi ducimus, libero explicabo perferendis illum ipsam. Reiciendis, eaque voluptatem alias nemo rerum aut ipsum dolorem aliquid pariatur atque minus, dolorum quis inventore quos deserunt dolor corporis sunt iste quo. Neque nulla dolorum quaerat provident praesentium doloremque natus facere optio, maxime architecto minima quia excepturi molestiae non odio tempore temporibus magni? Quam mollitia rem omnis temporibus soluta. Mollitia perferendis, dolorum reiciendis soluta quae id, fugiat impedit culpa error voluptatibus tenetur tempora. Iure totam accusamus obcaecati excepturi nemo id dolor ratione. Porro commodi quo unde amet ab error facilis, suscipit reiciendis consectetur, sequi impedit! Obcaecati, provident ad eum asperiores beatae cum dolores adipisci sint eveniet inventore quam dolorum totam fuga dicta dolore consequuntur enim eos quisquam ab laborum corporis doloribus dolorem? Porro ducimus totam molestias quibusdam dolorum, optio consequatur quaerat magni culpa dolore nihil vitae dolor neque nobis molestiae. Ducimus, fugit. Repellat sed nulla voluptatem necessitatibus consequatur beatae placeat similique, recusandae rem, sequi tempore temporibus ab enim eos obcaecati inventore culpa accusamus omnis, excepturi consectetur ea! Vero ex alias quaerat inventore obcaecati doloribus magni qui temporibus porro nesciunt, iure animi provident odio! Repellendus libero saepe natus, odio quidem cupiditate est magni odit! Tenetur possimus animi iste odio quibusdam ab enim quae fuga iure. Eius voluptatibus repudiandae tenetur, dolorum deserunt blanditiis veritatis reiciendis, temporibus harum obcaecati optio vero distinctio sapiente omnis maiores accusamus beatae.</div>-->
<!--    </div>-->
 </div>
</template>

<script>
import $ from "jquery";
import axios from "axios";
import SelectablePlan from '@/components/SelectablePlan.vue'
import PricingTable from '@/components/PricingTable.vue'
export default {
  components: {
    SelectablePlan,
    PricingTable,
  },
  name: "Car",
  data() {
    return {
      username:'',
      id_model: null,
    //  marka: 1,
      formModel:{
        model:'',
        power:'',
        engine_volume:'',
        logo:'',
        number_of_gears:'',
        price:'',
        body_type:'',
        year_of_issue:''
      }

    }
  },
  mounted() {
    this.loadMod()
    this.loadUser()
  },
  methods: {
    loadMod() {
      $.ajax({
        url: `http://127.0.0.1:8000/api/models/${this.$route.params.id}`,
        contentType: 'application/vnd.api+json',
        type: "GET",
        success: (response) => {
          this.formModel = response.data.attributes;
          this.id_model = response.data.id;
        }
      })
    },
    loadUser() {
      $.ajax({
        url: "http://127.0.0.1:8000/auth/users/me/",
        contentType: 'application/vnd.api+json',
        headers: {'Authorization': 'Token ' + localStorage.getItem('auth_token')},
        type: "GET",
        success: (response) => {
          this.username = response.data.attributes.username;
        }
      })
    },
    // setAuto() {
    //   $.ajax({
    //     url: "http://127.0.0.1:8000/api/models/" + this.id_model,
    //     // contentType: 'application/vnd.api+json',
    //     type: "PUT",
    //     data: this.formModel,
    //     success: (response) => {
    //       console.log('Данные обновились')
    //     },
    //     error: (response) => {
    //       console.log(error())
    //     }
    //   })
    // },
    onFileSelected(event){
      this.formModel.logo = event.target.files[0]
    },
    setAuto(){
      const fd = new FormData();
      fd.append('logo',this.formModel.logo, this.formModel.logo.name )
      fd.append('body_type',this.formModel.body_type )
      //fd.append('marka',this.marka)
      fd.append('model',this.formModel.model)
      fd.append('price',this.formModel.price)
      fd.append('year_of_issue',this.formModel.year_of_issue)
      fd.append('power',this.formModel.power)
      fd.append('engine_volume',this.formModel.engine_volume)
      fd.append('number_of_gears',this.formModel.number_of_gears)
      axios.put('http://127.0.0.1:8000/api/models/' + this.id_model,fd)
          .then(res => {
            console.log(res)
          })
    },
    deleteCar(){
      $.ajax({
        url: "http://127.0.0.1:8000/api/models/destroy/" + this.id_model,
        type: "DELETE",
        success: (response) => {
          console.log("SUCCESS",response)
        },
        error: (response) => {
          if (response.status === 400) {
            alert('Что-то нетак')
          }
        }
      })
    }


  }
}
</script>

<style scoped>

</style>