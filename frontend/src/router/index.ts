import Vue from "vue";
import VueRouter, { RouteConfig } from "vue-router";
import About from "@/views/About.vue";
import Search from "@/views/Search.vue";
import Links from "@/views/Links.vue";

Vue.use(VueRouter);

const routes: Array<RouteConfig> = [
  {
    path: "/",
    name: "Search",
    component: Search
  },
  {
    path: "/about",
    name: "About",
    component: About
  },
  {
    path: "/links",
    name: "Links",
    component: Links
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
