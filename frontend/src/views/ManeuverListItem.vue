<template>
  <v-list-item-content>
    <v-list-item-title v-text="maneuver.name"></v-list-item-title>
    <v-list-item-subtitle
      >Level {{ maneuver.level }} {{ maneuver.discipline.name }}
      <span v-if="maneuver.maneuverType.name !== 'Other'">
        {{ maneuver.maneuverType.name }}
      </span>
      <span v-else>
        maneuver
      </span></v-list-item-subtitle
    >
  </v-list-item-content>
</template>
<script lang="ts">
export default {
  name: "ManeuverListItem",
  props: {
    maneuver: {}
  }
};
</script>
