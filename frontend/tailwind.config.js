/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          50: '#fff0f6',
          100: '#ffe0ed',
          200: '#ffc2db',
          300: '#ff94be',
          400: '#FF6B9D',
          500: '#FF2D78',
          600: '#e01260',
          700: '#c00d50',
          800: '#9d0f44',
          900: '#83113c',
        },
        secondary: {
          50: '#eef2ff',
          100: '#e0e7ff',
          200: '#c7d2fe',
          300: '#a5b4fc',
          400: '#818cf8',
          500: '#667EEA',
          600: '#4F46E5',
          700: '#4338ca',
          800: '#3730a3',
          900: '#312e81',
        },
        accent: {
          50: '#fff7ed',
          100: '#ffedd5',
          200: '#fed7aa',
          300: '#fdba74',
          400: '#FF8C42',
          500: '#f97316',
          600: '#ea580c',
          700: '#c2410c',
          800: '#9a3412',
          900: '#7c2d12',
        },
        kid: {
          pink: '#FF6B9D',
          magenta: '#FF2D78',
          blue: '#4F46E5',
          lightblue: '#667EEA',
          orange: '#FF8C42',
          yellow: '#FBBF24',
          green: '#34D399',
          purple: '#A855F7',
        }
      },
      fontFamily: {
        sans: ['Nunito', 'Quicksand', 'ui-sans-serif', 'system-ui', '-apple-system', 'sans-serif'],
        display: ['Fredoka One', 'Nunito', 'sans-serif'],
      },
      borderRadius: {
        '4xl': '2rem',
      },
      animation: {
        'bounce-slow': 'bounce 2s infinite',
        'pulse-slow': 'pulse 3s infinite',
        'wiggle': 'wiggle 1s ease-in-out infinite',
        'float': 'float 3s ease-in-out infinite',
        'gradient-shift': 'gradient-shift 3s ease infinite',
      },
      keyframes: {
        wiggle: {
          '0%, 100%': { transform: 'rotate(-3deg)' },
          '50%': { transform: 'rotate(3deg)' },
        },
        float: {
          '0%, 100%': { transform: 'translateY(0px)' },
          '50%': { transform: 'translateY(-10px)' },
        },
        'gradient-shift': {
          '0%, 100%': { backgroundPosition: '0% 50%' },
          '50%': { backgroundPosition: '100% 50%' },
        },
      },
    },
  },
  plugins: [],
}
