/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        cream: '#F5F3EE',
        'cream-dark': '#EBE8E1',
        terracotta: {
          DEFAULT: '#C97E5D',
          light: '#D99A7E',
          dark: '#A8624A',
        },
        sage: {
          DEFAULT: '#8B9D83',
          light: '#A5B39E',
          dark: '#6E8066',
        },
        charcoal: {
          DEFAULT: '#36454F',
          light: '#4A5C68',
          dark: '#252F36',
        },
        sand: '#D4C5A9',
      },
      fontFamily: {
        serif: ['Newsreader', 'Georgia', 'serif'],
        sans: ['Space Grotesk', '-apple-system', 'system-ui', 'sans-serif'],
      },
      animation: {
        'fade-in': 'fadeIn 0.8s both',
        'fade-in-up': 'fadeInUp 0.8s both',
        'fade-in-up-d1': 'fadeInUp 0.8s 0.15s both',
        'fade-in-up-d2': 'fadeInUp 0.8s 0.3s both',
        'fade-in-up-d3': 'fadeInUp 0.8s 0.45s both',
      },
      keyframes: {
        fadeIn: {
          from: { opacity: '0' },
          to: { opacity: '1' },
        },
        fadeInUp: {
          from: { opacity: '0', transform: 'translateY(24px)', filter: 'blur(8px)' },
          to: { opacity: '1', transform: 'translateY(0)', filter: 'blur(0)' },
        },
      },
    },
  },
  plugins: [],
};
