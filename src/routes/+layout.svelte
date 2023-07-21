<script lang="ts">
	import Header from './Header.svelte';
	import './styles.css';
	import { setContext } from 'svelte';
    import { writable } from 'svelte/store';


	export let data;
</script>

<div class="app">

	<Header ></Header>
	<br>
	<slot></slot>
</div>

<style>
	
</style>
