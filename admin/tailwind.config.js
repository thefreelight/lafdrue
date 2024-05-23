/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}"
  ],
  theme: {
    extend: {
      colors: {
        // 定义紫色和蓝色的渐变色
        purple: {
          light: '#a569bd',  // 浅紫色
          DEFAULT: '#8e44ad', // 默认紫色
          dark: '#5e3370'     // 深紫色
        },
        blue: {
          light: '#5dade2',  // 浅蓝色
          DEFAULT: '#3498db', // 默认蓝色
          dark: '#217dbb'     // 深蓝色
        },
        // 保持原有的蓝色配置，以备不时之需
        'original-blue': {
          light: '#85d7ff',  // 浅蓝色
          DEFAULT: '#1fb6ff', // 默认蓝色
          dark: '#009eeb'     // 深蓝色
        },
        // 定义背景和文本颜色
        theme: {
          'background': '#212f3d', // 背景色
          'text': '#ffffff', // 文本色
          'muted': '#7f8c8d', // 灰色文本或次要文本色
        },
      },
      // 添加渐变背景色的定制
      backgroundImage: {
        'gradient-nav': 'linear-gradient(to right, #8e44ad, #3498db)', // 添加自定义渐变背景
        'gradient-to-r': 'linear-gradient(to right, var(--tw-gradient-stops))',
      },
      // 如果需要，还可以添加字体大小、边距、阴影等其他定制
    },
  },
  plugins: [],
}
