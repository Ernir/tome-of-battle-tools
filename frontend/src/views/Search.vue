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
            v-model="searchManeuverName"
          ></v-autocomplete>
          <v-select
            v-model="searchLevels"
            :items="levels"
            chips
            label="Level"
            multiple
          ></v-select>
          <v-select
            v-model="searchDisciplines"
            :items="disciplines"
            chips
            label="Disciplines"
            multiple
          ></v-select>
          <v-select
            v-model="searchRequirements"
            :items="requirements"
            chips
            label="Requirements"
            multiple
          ></v-select>
          <v-select
            v-model="searchManeuverTypes"
            :items="maneuverTypes"
            chips
            label="Type"
            multiple
          ></v-select>
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
          slug
        }
      }
    `
  },

  computed: {
    maneuversFiltered: function() {
      const filtered = [];
      for (const maneuver of [...this.allManeuvers]) {
        const nameMatch = this.nameFilter(maneuver, this.searchManeuverName);
        if (nameMatch) {
          filtered.push(maneuver);
        }
      }
      return filtered;
    },

    levels: function() {
      const levels = [];
      for (const { level } of [...this.allManeuvers]) {
        levels.push(level);
      }
      return Array.from(new Set(levels)).sort();
    },

    disciplines: function() {
      const disciplines = new Set();
      for (const { discipline } of [...this.allManeuvers]) {
        disciplines.add(discipline.name);
      }
      return Array.from(new Set(disciplines)).sort();
    },

    requirements: function() {
      const requirementsArray = [];
      for (const { requirements } of [...this.allManeuvers]) {
        requirementsArray.push(requirements);
      }
      return Array.from(new Set(requirementsArray)).sort();
    },

    maneuverTypes: function() {
      const maneuverTypes = new Set();
      for (const { maneuverType } of [...this.allManeuvers]) {
        maneuverTypes.add(maneuverType.name);
      }
      return Array.from(new Set(maneuverTypes)).sort();
    }
  },

  data: function(): {
    searchManeuverName: string;
    searchLevels: number[];
    searchDisciplines: string[];
    searchRequirements: number[];
    searchManeuverTypes: string[];
    allManeuvers: any[];
  } {
    return {
      searchManeuverName: "",
      searchLevels: [],
      searchDisciplines: [],
      searchRequirements: [],
      searchManeuverTypes: [],

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
