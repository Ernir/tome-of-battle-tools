<template>
  <v-container>
    <v-row>
      <v-col cols="12" sm="4">
        <v-card class="pa-2" outlined tile>
          <v-autocomplete
            :items="allManeuvers"
            :filter="nameFilter"
            item-text="name"
            label="Name"
            v-model="maneuverSearchName"
          ></v-autocomplete>
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
              <v-list-item
                v-for="maneuver in maneuversFiltered"
                :key="maneuver.id"
              >
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
import gql from "graphql-tag";
import ManeuverListItem from "@/views/ManeuverListItem.vue";

export default Vue.component("Search", {
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
  },

  computed: {
    maneuversFiltered: function() {
      const filtered = [];
      for (const maneuver of [...this.allManeuvers]) {
        const nameMatch = this.nameFilter(maneuver, this.maneuverSearchName);
        if (nameMatch) {
          filtered.push(maneuver);
        }
      }
      return filtered;
    }
  },

  data: function() {
    return {
      maneuverSearchName: "",
      allManeuvers: []
    };
  },

  methods: {
    nameFilter(maneuver: { name: string }, queryText: string) {
      const maneuverName = maneuver.name.toLowerCase();
      const comparisonText = queryText ? queryText.toLowerCase() : "";
      return maneuverName.indexOf(comparisonText) > -1;
    }
  }
});
</script>
