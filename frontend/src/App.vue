<template>
  <v-app id="tob-tools">
    <Navigation />
    <v-main>
      <router-view />
    </v-main>
    <Footer />
  </v-app>
</template>

<script lang="ts">
import Vue from "vue";
import Footer from "@/components/Footer.vue";
import Navigation from "@/components/Navigation.vue";

export default Vue.extend({
  name: "App",

  components: { Navigation, Footer },

  data: () => ({
    //
  })
});
</script>
