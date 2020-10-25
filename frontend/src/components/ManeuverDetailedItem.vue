<template>
  <div>
    <h2>
      {{ maneuver.name }}
      <small>p. {{ maneuver.page }}</small>
    </h2>

    <p>
      {{ maneuver.discipline.name }}
      <span v-if="maneuver.type && maneuver.type.name !== 'Other'">
        ({{ maneuver.type }})
      </span>
      <span
        v-for="descriptor in maneuver.descriptor"
        v-bind:key="descriptor.id"
      >
        [{{ descriptor }}]
      </span>
    </p>

    <div>
      <strong>Level:</strong>
      <span
        v-for="(initiatorClass, index) in maneuver.discipline.initiatorClasses"
        v-bind:key="index"
      >
        <span>{{ initiatorClass.name }} {{ maneuver.level }}</span
        ><span v-if="index + 1 < maneuver.discipline.initiatorClasses.length"
          >,
        </span>
      </span>
    </div>

    <div v-if="maneuver.requirements">
      <strong>Prerequisite:</strong> {{ maneuver.requirements }}
      {{ maneuver.discipline }}
      maneuvers
    </div>

    <div><strong>Initiation Action:</strong> {{ maneuver.action }}</div>

    <div><strong>Range:</strong> {{ maneuver.range }}</div>

    <div v-if="maneuver.target">
      <strong>Target:</strong> {{ maneuver.target }}
    </div>

    <div v-if="maneuver.area"><strong>Area:</strong> {{ maneuver.area }}</div>

    <div v-if="maneuver.effect">
      <strong>Effect:</strong> {{ maneuver.effect }}
    </div>

    <div v-if="maneuver.duration">
      <strong>Duration:</strong> {{ maneuver.duration }}
    </div>

    <div v-if="maneuver.savingThrow">
      <strong>Saving throw:</strong> {{ maneuver.savingThrow.description }}
    </div>

    <div v-html="maneuver.htmlDescription" />

    <div v-if="maneuver.alternateVersion">
      This maneuver has been updated by errata. See
      {{ maneuver.alternateVersion.slug }}/{{ maneuver.alternateVersion.name }}
      for details.
    </div>
  </div>
</template>
<script lang="ts">
export default {
  name: "ManeuverDetailedItem",
  props: {
    maneuver: {}
  }
};
</script>
