<template>
  <v-container>
    <v-row>
      <v-col v-for="n in 3" :key="n" cols="12" sm="4">
        <v-card class="pa-2" outlined tile>
          One of three columns
        </v-card>
      </v-col>
    </v-row>
    <div v-if="$apollo.loading">Loading...</div>
    <div v-else>{{ allManeuvers }}</div>
  </v-container>
</template>

<script lang="ts">
import Vue from "vue";
import Component from "vue-class-component";
import gql from "graphql-tag";

@Component({
  apollo: {
    allManeuvers: () => gql`
      {
        allManeuvers {
          name
          discipline {
            name
          }
          maneuverType {
            name
          }
          level
          requirements
        }
      }
    `
  }
})
export default class Search extends Vue {}
</script>
