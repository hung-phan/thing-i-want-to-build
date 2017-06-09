"use strict";

var join = require("path").join;
var CheckerPlugin = require("awesome-typescript-loader").CheckerPlugin;

module.exports = {
  context: __dirname,
  entry: join(__dirname, "src", "index"),
  output: {
    path: join(__dirname, "public/assets"),
    filename: "app.js",
    libraryTarget: "umd",
    umdNamedDefine: true
  },
  resolve: {
    extensions: [".ts", ".tsx", ".js", ".jsx"]
  },
  module: {
    loaders: [
      {
        test: /\.(ts|tsx)$/,
        loader: "awesome-typescript-loader"
      }
    ]
  },
  plugins: [
    new CheckerPlugin()
  ]
};