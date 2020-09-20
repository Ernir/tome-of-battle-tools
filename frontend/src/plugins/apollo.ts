import { ApolloClient } from "apollo-client";
import { createHttpLink } from "apollo-link-http";
import { InMemoryCache } from "apollo-cache-inmemory";

// HTTP connection to the API
const httpLink = createHttpLink({
  uri: "http://localhost:8000/graphql"
});

// Cache implementation
const cache = new InMemoryCache();

// Create the apollo client
export default new ApolloClient({
  link: httpLink,
  cache
});