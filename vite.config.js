import { defineConfig } from 'vite'
import { resolve } from 'path'

export default defineConfig({
  base: './',
  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
        markalar: resolve(__dirname, 'markalar.html'),
        gunes: resolve(__dirname, 'gunes-gozlukleri.html'),
        optik: resolve(__dirname, 'optik-cerceveler.html')
      }
    }
  }
})
