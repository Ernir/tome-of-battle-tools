<template>
  <v-card>
    <v-card-title>Tome of Battle Links</v-card-title>
    <v-list v-for="link in linkDefinitions" :key="link.description">
      <v-list-item link>
        <v-list-item-content>
          <a :href="link.target">{{ link.description }}</a>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </v-card>
</template>

<script lang="ts">
import Vue from "vue";
import Component from "vue-class-component";

class LinkDefinition {
  target: string;
  description: string;

  constructor(target: string, description: string) {
    this.target = target;
    this.description = description;
  }
}

@Component
export default class Links extends Vue {
  data() {
    return {
      linkDefinitions: [
        new LinkDefinition(
          "http://archive.wizards.com/default.asp?x=dnd/we/20061225a",
          "Tome of Battle Maneuvers in card format"
        ),
        new LinkDefinition(
          "http://brilliantgameologists.com/boards/index.php?topic=13292.0",
          "The Unofficial Tome of Battle Errata"
        ),
        new LinkDefinition(
          "http://www.amazon.com/Tome-Battle-Dungeons-Dragons-Roleplaying/dp/0786939222",
          "The Tome of Battle on Amazon.com"
        ),
        new LinkDefinition(
          "http://rpg.stackexchange.com/questions/tagged/tome-of-battle",
          "The Tome of Battle on rpg.stackexchange.com"
        )
      ]
    };
  }
}
</script>
