<template>
  <v-container>
    <v-row>
      <v-col cols="12" sm="4">
        <v-card class="pa-2" outlined tile>
          One of three columns
        </v-card>
      </v-col>
      <v-col cols="12" sm="4">
        <v-card class="pa-2" outlined tile>
          <div v-if="$apollo.loading">
            <div class="text-center">
              <v-progress-circular indeterminate></v-progress-circular>
            </div>
          </div>
          <v-list dense>
            <v-list-item-group>
              <v-list-item v-for="maneuver in allManeuvers" :key="maneuver.id">
                <ManeuverListItem :maneuver="maneuver" />
              </v-list-item>
            </v-list-item-group>
          </v-list>
        </v-card>
      </v-col>
      <v-col cols="12" sm="4">
        <v-card class="pa-2" outlined tile>
          One of three columns
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import Vue from "vue";
import Component from "vue-class-component";
import gql from "graphql-tag";
import ManeuverListItem from "@/views/ManeuverListItem.vue";

@Component({
  components: { ManeuverListItem },
  apollo: {
    allManeuvers: () => gql`
      {
        allManeuvers {
          id
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
