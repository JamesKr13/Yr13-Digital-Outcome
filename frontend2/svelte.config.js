import adapter from '@sveltejs/adapter-auto';
import preprocess from 'svelte-preprocess';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	// Consult https://github.com/sveltejs/svelte-preprocess
	// for more information about preprocessors
	preprocess: preprocess(),
	output: {
        	sourcemap: true,
        	format: 'iife',
        	name: 'app',
        	file: '../myapp/static/frontend/bundle.js' // <-- here
    },
	kit: {
		adapter: adapter(),
		vite: { optimizeDeps: { include: ['lodash.get', 'lodash.isequal', 'lodash.clonedeep'] } }
	}
};

export default config;

