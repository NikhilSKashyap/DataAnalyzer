const { gql } = require('apollo-server-express');

const typeDefs = gql`
  type Query {
    executeGemini(question: String!): String
  }
`;

module.exports = typeDefs;
