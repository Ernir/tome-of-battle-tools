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
import { ManeuverType } from "@/types";

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
    maneuversFiltered: function(): ManeuverType[] {
      const maneuvers: ManeuverType[] = [...this.allManeuvers];
      return maneuvers.filter(
        maneuver =>
          this.nameFilter(maneuver, this.searchManeuverName) &&
          (this.searchRequirements.length === 0 ||
            this.searchRequirements.includes(maneuver.requirements)) &&
          (this.searchLevels.length === 0 ||
            this.searchLevels.includes(maneuver.level)) &&
          (this.searchDisciplines.length === 0 ||
            this.searchDisciplines.includes(maneuver.discipline.name)) &&
          (this.searchManeuverTypes.length === 0 ||
            this.searchManeuverTypes.includes(maneuver.maneuverType.name))
      );
    },

    levels: function(): number[] {
      const maneuvers: ManeuverType[] = [...this.allManeuvers];
      return [...new Set(maneuvers.map(({ level }) => level))].sort();
    },

    disciplines: function(): string[] {
      const maneuvers: ManeuverType[] = [...this.allManeuvers];
      return [...new Set(maneuvers.map(m => m.discipline.name))].sort();
    },

    requirements: function(): number[] {
      const maneuvers: ManeuverType[] = [...this.allManeuvers];
      return [
        ...new Set(maneuvers.map(({ requirements }) => requirements))
      ].sort();
    },

    maneuverTypes: function(): string[] {
      const maneuvers: ManeuverType[] = [...this.allManeuvers];
      return [...new Set(maneuvers.map(m => m.maneuverType.name))].sort();
    }
  },

  data: function(): {
    searchManeuverName: string;
    searchLevels: number[];
    searchDisciplines: string[];
    searchRequirements: number[];
    searchManeuverTypes: string[];
    allManeuvers: ManeuverType[];
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
    nameFilter(maneuver: ManeuverType, queryText: string) {
      const maneuverName = maneuver.name.toLowerCase();
      const comparisonText = queryText ? queryText.toLowerCase() : "";
      return maneuverName.indexOf(comparisonText) > -1;
    }
  }
});
</script>
