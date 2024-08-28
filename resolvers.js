const { exec } = require('child_process');

const resolvers = {
  Query: {
    executeGemini: async (_, { question }) => {
      return new Promise((resolve, reject) => {
        exec(`python execute_gemini_result.py "${question}"`, (error, stdout, stderr) => {
          if (error) {
            reject(`Execution error: ${stderr}`);
          } else {
            resolve(stdout);
          }
        });
      });
    }
  }
};

module.exports = resolvers;
