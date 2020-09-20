import Vue from "vue";
import VueApollo from "vue-apollo";
import App from "./App.vue";
import router from "./router";
import apolloClient from "./plugins/apollo";
import vuetify from "./plugins/vuetify";

const apolloProvider = new VueApollo({
  defaultClient: apolloClient
});

Vue.config.productionTip = false;
Vue.use(VueApollo);

new Vue({
  router,
  apolloProvider,
  vuetify,
  render: h => h(App)
}).$mount("#app");
