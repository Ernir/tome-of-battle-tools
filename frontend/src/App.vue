<template>
  <v-app id="tob-tools">
    <v-main>
      <router-view />
    </v-main>
    <Footer />
  </v-app>
</template>

<script lang="ts">
import Vue from "vue";
import Footer from "@/components/Footer.vue";

export default Vue.extend({
  name: "App",

  components: { Footer },

  data: () => ({
    //
  })
});
</script>
