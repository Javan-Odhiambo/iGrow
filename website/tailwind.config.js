/** @type {import('tailwindcss').Config} */
import daisyui from "daisyui"

module.exports = {
  content: [
    './templates/**/*.{html,js}',
    "./**/forms.py",
  ],
  theme: {
    extend: {},
  },
  plugins: [
    daisyui
  ],
};
