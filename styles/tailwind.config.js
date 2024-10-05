/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    '../src/templates/allauth/**/*.html'
  ],
  theme: {
    extend: {
      backgroundImage: {
        'login': "url('/static/images/bg-login.webp')",
      }
    },
  },
  plugins: [],
}

