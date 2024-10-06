/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    '../templates/allauth/**/*.html',
    '../src/**/*.html'
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

