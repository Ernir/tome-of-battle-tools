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
import { Dictionary } from "vue-router/types/router";

const nameParam = "n";
const levelsParam = "l";
const disciplinesParam = "d";
const requirementsParam = "r";
const maneuverTypesParam = "t";

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

    levels(): number[] {
      const maneuvers: ManeuverType[] = [...this.allManeuvers];
      return [...new Set(maneuvers.map(({ level }) => level))].sort();
    },

    disciplines(): string[] {
      const maneuvers: ManeuverType[] = [...this.allManeuvers];
      return [...new Set(maneuvers.map(m => m.discipline.name))].sort();
    },

    requirements(): number[] {
      const maneuvers: ManeuverType[] = [...this.allManeuvers];
      return [
        ...new Set(maneuvers.map(({ requirements }) => requirements))
      ].sort();
    },

    maneuverTypes(): string[] {
      const maneuvers: ManeuverType[] = [...this.allManeuvers];
      return [...new Set(maneuvers.map(m => m.maneuverType.name))].sort();
    }
  },

  data(): {
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
    nameFilter(maneuver: ManeuverType, queryText: string): boolean {
      const maneuverName = maneuver.name.toLowerCase();
      const comparisonText = queryText ? queryText.toLowerCase() : "";
      return maneuverName.indexOf(comparisonText) > -1;
    },
    /**
     * Extracts a Vue router query parameter to a target array.
     *
     * @param queryParam a query parameter from this.$route.query, potentially multiple, represented as an array
     * @param target an array to populate
     * @param mapper mapping function to transform each query parameter
     */
    extractParams<T>(
      queryParam: string | (string | null)[],
      target: T[],
      mapper: (arg: string) => T
    ) {
      if (Array.isArray(queryParam)) {
        queryParam.forEach(l => {
          if (l != null) {
            target.push(mapper(l));
          }
        });
      } else {
        if (queryParam != null) {
          target.push(mapper(queryParam));
        }
      }
    }
  },

  created() {
    const nameQuery = this.$route.query[nameParam];
    if (nameQuery && !Array.isArray(nameQuery)) {
      this.searchManeuverName = decodeURIComponent(nameQuery);
    }
    this.extractParams(
      this.$route.query[levelsParam],
      this.searchLevels,
      parseInt
    );
    this.extractParams(
      this.$route.query[disciplinesParam],
      this.searchDisciplines,
      decodeURIComponent
    );
    this.extractParams(
      this.$route.query[requirementsParam],
      this.searchRequirements,
      parseInt
    );
    this.extractParams(
      this.$route.query[maneuverTypesParam],
      this.searchManeuverTypes,
      decodeURIComponent
    );
  },

  updated() {
    // TODO check whether this type definition can be parameterized
    const query: Dictionary<string | string[]> = {};
    if (this.searchManeuverName) {
      query[nameParam] = encodeURIComponent(this.searchManeuverName);
    }
    query[levelsParam] = this.searchLevels?.map(level => level.toString());
    query[disciplinesParam] = this.searchDisciplines?.map(d =>
      encodeURIComponent(d)
    );
    query[requirementsParam] = this.searchRequirements?.map(r => r.toString());
    if (this.searchManeuverTypes) {
      query[maneuverTypesParam] = this.searchManeuverTypes;
    }
    this.$router.push({ query: query });
  }
});
</script>
