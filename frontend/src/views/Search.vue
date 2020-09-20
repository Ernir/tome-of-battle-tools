<template>
  <v-container>
    <v-row>
      <v-col v-for="n in 3" :key="n" cols="12" sm="4">
        <v-card class="pa-2" outlined tile>
          One of three columns
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import Vue from "vue";
import Component from "vue-class-component";

@Component
export default class Search extends Vue {}
</script>
