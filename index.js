const express = require('express');
const { ApolloServer } = require('apollo-server-express');
const cors = require('cors'); // Import CORS package
const typeDefs = require('./schema');
const resolvers = require('./resolvers');

async function startServer() {
  const app = express();

  // Apply CORS middleware to accept requests from your frontend
  app.use(cors({
    origin: 'http://localhost:3000',  // This should match the URL of your frontend, adjust if different
    credentials: true  // This allows cookies and headers to be included in cross-origin requests
  }));

  const server = new ApolloServer({
    typeDefs,
    resolvers,
  });

  await server.start();

  // Here, disable Apollo's built-in CORS to use Express' CORS
  server.applyMiddleware({ app, path: '/graphql', cors: false });

  app.listen({ port: 4000 }, () =>
    console.log(`🚀 Server ready at http://localhost:4000${server.graphqlPath}`)
  );
}

startServer();
