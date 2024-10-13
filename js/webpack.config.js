const path = require('path');

module.exports = {
  entry: {
    apps: './src/apps.js',
    modules: './src/modules.js'
  },
  output: {
    filename: '[name].bundle.js',
    path: path.resolve(__dirname, '../static/js') // Adjust the path for Django static files
  },
  resolve: {
    alias: {
      '@apps': path.resolve(__dirname, './src/apps/'),
      '@modules': path.resolve(__dirname, './src/modules/'),
    },
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader'
        }
      }
    ]
  },
  mode: 'production'
};
